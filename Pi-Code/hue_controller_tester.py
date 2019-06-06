from lights import HueLights
from huecontroller import HueController
import requests
from config import FER_SERVER, HUE_BASE_URL, HUE_USERNAME




if __name__ == '__main__':
    predictions = requests.get(FER_SERVER+'/predictions').json()
    hue_controller = HueController()
    lights = HueLights(HUE_BASE_URL, HUE_USERNAME)
    hue = hue_controller.compute_hue(predictions)
    lights.set(hue, 85)
