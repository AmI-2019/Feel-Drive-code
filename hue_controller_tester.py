from lights import HueLights
from huecontroller import HueController
import requests

BASE_URL =  'http://localhost:80'
USERNAME = 'newdeveloper'
# USERNAME = "GtmODLN6GK9MXxcoxkvRJuIhQvdjzXSOPW77IRGL"


if __name__ == '__main__':

    base_uri = 'http://192.168.1.68:5000/fer-server'

    predictions = requests.get(base_uri+'/predictions').json()
    hue_controller = HueController()
    lights = HueLights()
    hue = hue_controller.compute_hue(predictions)
    lights.custom(hue, 85)
