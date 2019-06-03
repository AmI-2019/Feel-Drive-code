import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl


class HueController:

    def __init__(self):
        self.happy = ctrl.Antecedent(np.arange(0, 1, 0.01), 'happy')
        self.sad = ctrl.Antecedent(np.arange(0, 1, 0.01), 'sad')
        self.angry = ctrl.Antecedent(np.arange(0, 1, 0.01), 'angry')
        self.hue = ctrl.Consequent(np.arange(0, 65280, 1), 'hue')

        self.hue['blue'] = fuzz.trimf(self.hue.universe, [40920, 46920, 49920])
        self.hue['green'] = fuzz.trimf(self.hue.universe, [9500, 12750, 16250])
        self.hue['red'] = fuzz.trimf(self.hue.universe, [62280, 65280, 65280])

        self.happy.automf(3)
        self.sad.automf(3)
        self.angry.automf(3)

        self.rule1 = ctrl.Rule(self.angry['good'] | self.angry['average'], self.hue['red'])
        self.rule2 = ctrl.Rule(self.sad['good'], self.hue['blue'])
        self.rule3 = ctrl.Rule(self.happy['good'], self.hue['green'])

        self.hue_controller = ctrl.ControlSystemSimulation(ctrl.ControlSystem([self.rule1, self.rule2, self.rule3]))

    def compute_hue(self, emotions):
        self.hue_controller.input['happy'] = emotions['happy']
        self.hue_controller.input['sad'] = emotions['sad']
        self.hue_controller.input['angry'] = emotions['angry']
        self.hue_controller.compute()
        return self.hue_controller.output['hue']
