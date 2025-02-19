import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl


class HueController:

    def __init__(self):
        self.happy = ctrl.Antecedent(np.arange(0, 1, 0.01), 'happy')
        self.sad = ctrl.Antecedent(np.arange(0, 1, 0.01), 'sad')
        self.angry = ctrl.Antecedent(np.arange(0, 1, 0.01), 'angry')
        self.neutral = ctrl.Antecedent(np.arange(0, 1, 0.01), 'neutral')
        self.lsr = ctrl.Antecedent(np.arange(0, 1, 0.01), 'lsr')

        self.hue = ctrl.Consequent(np.arange(0, 65280, 1), 'hue')
        self.brightness = ctrl.Consequent(np.arange(0, 100, 1), 'brightness')
        self.sat = ctrl.Consequent(np.arange(220, 254, 1), 'sat')

        self.hue['blue'] = fuzz.trimf(self.hue.universe, [46620, 46920, 47320])
        self.hue['green'] = fuzz.trimf(self.hue.universe, [21900, 22000, 22100])
        self.hue['red'] = fuzz.trimf(self.hue.universe, [64780, 65280, 65280])
        self.lsr['bright'] = fuzz.trimf(self.lsr.universe, [0.50, 1, 1])
        self.lsr['dark'] = fuzz.trimf(self.lsr.universe, [0, 0, 0.50])
        self.brightness['bright'] = fuzz.trimf(self.brightness.universe, [60, 100, 100])
        self.brightness['dark'] = fuzz.trimf(self.brightness.universe, [25, 25, 60])
        self.sat['good'] = fuzz.trimf(self.sat.universe, [242, 254, 254])
        self.sat['average'] = fuzz.trimf(self.sat.universe, [220, 220, 242])

        self.happy.automf(3)
        self.sad.automf(3)
        self.angry.automf(3)
        self.neutral.automf(3)

        self.rule1 = ctrl.Rule(self.angry['good'] | self.angry['average'], self.hue['blue'])
        self.rule2 = ctrl.Rule(self.sad['good'] | self.sad['average'], self.hue['red'])

        self.rule3 = ctrl.Rule(self.happy['good'] | self.happy['average'] | self.neutral['good'], self.hue['green'])
        self.rule4 = ctrl.Rule(self.lsr['dark'], self.brightness['dark'])
        self.rule5 = ctrl.Rule(self.lsr['bright'], self.brightness['bright'])
        self.rule6 = ctrl.Rule(self.angry['good'] | self.sad['good'], self.sat['good'])
        self.rule7 = ctrl.Rule(self.angry['average'] | self.sad['average'],  self.sat['average'])

        self.hue_controller = ctrl.ControlSystemSimulation(ctrl.ControlSystem([self.rule1, self.rule2, self.rule3,
                                                                               self.rule4, self.rule5, self.rule6, self.rule7]))

    def compute_hue(self, emotions, lsr):
        self.hue_controller.input['happy'] = emotions['happy']
        self.hue_controller.input['sad'] = emotions['sad']
        self.hue_controller.input['angry'] = emotions['angry']
        self.hue_controller.input['neutral'] = emotions['neutral']
        self.hue_controller.input['lsr'] = lsr
        self.hue_controller.compute()
        return self.hue_controller.output['hue'], self.hue_controller.output['brightness'], self.hue_controller.output['sat']
