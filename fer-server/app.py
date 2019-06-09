from flask import Flask, request, jsonify
from fer import Fer

app = Flask(__name__)
api_endpoint = '/fer-server'
emotion_detector = None


@app.route(api_endpoint+'/start', methods=['POST'])
def start():
    global emotion_detector
    ipcamera = request.json
    print(ipcamera["address"])
    emotion_detector = Fer(ipcamera["address"])
    emotion_detector.start_detector()
    return ''

@app.route(api_endpoint+'/stop', methods=['GET'])
def stop():
    global emotion_detector
    emotion_detector.close_detector()
    del emotion_detector
    return ''

@app.route(api_endpoint+'/predictions', methods=['GET'])
def get_predictions():
    global emotion_detector
    if emotion_detector is not None:
        result = emotion_detector.get_emotion_prediction()
        return jsonify(result)
    else:
        return jsonify([])


if __name__ == '__main__':
    app.run(host='0.0.0.0')
