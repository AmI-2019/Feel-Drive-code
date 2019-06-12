import cv2
import numpy as np
from keras.models import load_model
from keras import backend
from statistics import mode
from utils.datasets import get_labels
from utils.inference import detect_faces
from utils.inference import draw_text
from utils.inference import draw_bounding_box
from utils.inference import apply_offsets
from utils.inference import load_detection_model
from utils.preprocessor import preprocess_input
from collections import OrderedDict
import threading
import time
DEBUG = True

EMOTION_MODEL_PATH = './models/emotion_model.hdf5'
# hyper-parameters for bounding boxes shape
FRAME_WINDOW = 10
EMOTION_OFFSETS = (20, 40)
SAMPLING_PERIOD = 2
MIN_SAMPLE = 3


class Fer:

    def __init__(self, camera):
        self.camera = camera
        self.stoprequst = threading.Event()
        self.ferThread = self.DetectorThread(self, stop_event=self.stoprequst)
        self.lock = threading.Lock()
        self.predictions = OrderedDict()
        backend.clear_session()

        self.emotion_labels = get_labels('fer2013')
        print(self.emotion_labels)

    def detect_emotion(self):
        face_cascade = cv2.CascadeClassifier('./models/haarcascade_frontalface_default.xml')
        emotion_classifier = load_model(EMOTION_MODEL_PATH)

        # getting input model shapes for inference
        emotion_target_size = emotion_classifier.input_shape[1:3]

        # starting lists for calculating modes
        emotion_window = []
        start_time = time.time()
        last_time = start_time
        if not DEBUG:
            # Webcam source
            cap = cv2.VideoCapture(self.camera)
            print("Opening camera stream...")
        else:
            cap = cv2.VideoCapture(0)  # Video file source

        if not cap.isOpened():
            print("Cannot open cam!")

        cv2.namedWindow('window_frame')
        while cap.isOpened():  # True:
            if self.stoprequst.isSet():
                break
            ret, bgr_image = cap.read()

            # bgr_image = video_capture.read()[1]

            gray_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2GRAY)
            rgb_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2RGB)

            faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5,
                                                  minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)

            if (time.time()-last_time > SAMPLING_PERIOD) and len(faces) > 0:
                last_time = time.time()
                face_coordinates = faces[0]
                x1, x2, y1, y2 = apply_offsets(face_coordinates, EMOTION_OFFSETS)
                gray_face = gray_image[y1:y2, x1:x2]
                try:
                    gray_face = cv2.resize(gray_face, emotion_target_size)
                except:
                    continue

                gray_face = preprocess_input(gray_face, True)
                gray_face = np.expand_dims(gray_face, 0)
                gray_face = np.expand_dims(gray_face, -1)
                emotion_prediction = emotion_classifier.predict(gray_face)
                emotion_probability = np.max(emotion_prediction)
                emotion_label_arg = np.argmax(emotion_prediction)
                emotion_text = self.emotion_labels[emotion_label_arg]
                emotion_window.append(emotion_text)

                self.lock.acquire(1)
                self.predictions[last_time] = emotion_prediction.tolist()
                self.lock.release()

                if len(emotion_window) > FRAME_WINDOW:
                    emotion_window.pop(0)
                try:
                    emotion_mode = mode(emotion_window)
                except:
                    continue

                if emotion_text == 'angry':
                    color = emotion_probability * np.asarray((255, 0, 0))
                elif emotion_text == 'sad':
                    color = emotion_probability * np.asarray((0, 0, 255))
                elif emotion_text == 'happy':
                    color = emotion_probability * np.asarray((255, 255, 0))
                elif emotion_text == 'surprise':
                    color = emotion_probability * np.asarray((0, 255, 255))
                else:
                    color = emotion_probability * np.asarray((0, 255, 0))

                color = color.astype(int)
                color = color.tolist()

                draw_bounding_box(face_coordinates, rgb_image, color)
                draw_text(face_coordinates, rgb_image, emotion_mode,
                          color, 0, -45, 1, 1)

            bgr_image = cv2.cvtColor(rgb_image, cv2.COLOR_RGB2BGR)
            cv2.imshow('window_frame', bgr_image)
            if cv2.waitKey(10) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()

    class DetectorThread(threading.Thread):
        def __init__(self, fer, stop_event):
            threading.Thread.__init__(self)
            self.fer = fer
            self.stoprequest = stop_event

        def run(self):
            self.fer.detect_emotion()

    def start_detector(self):
        self.ferThread.start()

    def close_detector(self):
        self.stoprequst.set()
        self.ferThread.join()

    def get_emotion_prediction(self):
        self.lock.acquire(1)
        local_sum = [0, 0, 0, 0, 0, 0, 0]

        if len(self.predictions) < MIN_SAMPLE:
            self.lock.release()
            return []

        #print(self.predictions)

        for i, (t, prediction) in enumerate(reversed(self.predictions.items())):
            if i >= MIN_SAMPLE:
                break
            for j, emotion in enumerate(prediction[0]):
                local_sum[j] += emotion
        #print(local_sum)
        result = [x/(MIN_SAMPLE) for x in local_sum]
        self.lock.release()
        return {k: v for k, v in zip(list(self.emotion_labels.values()), result)}
