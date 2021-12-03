import unittest
from challenges.day_06 import *

class Day06_Tests(unittest.TestCase):

    def testLightGrid_TurnOnLights_WithAllLightsOff_ShouldTurnOn(self):
        light_grid = LightGrid()
        light_grid.turn_on_lights((0, 0), (2, 2))

        for x, row in enumerate(light_grid.grid):
            for y, isLightOn in enumerate(row):
                if(isLightOn):
                    self.assertIn(x, [0, 1, 2])
                    self.assertIn(y, [0, 1, 2])
                else:
                    self.assertTrue(x not in [0, 1, 2] or y not in [0, 1, 2])
        
    def testLightGrid_TurnOnLights_WithAllLightsOn_ShouldDoNothing(self):
        light_grid = LightGrid()
        light_grid.grid = [ [ True for _ in range (1000) ] for _ in range (1000) ]
        light_grid.turn_on_lights((0, 0), (2, 2))

        for row in light_grid.grid:
            for isLightOn in row:
                self.assertTrue(isLightOn)
        
    def testLightGrid_TurnOffLights_WithAllLightsOn_ShouldTurnOff(self):
        light_grid = LightGrid()
        light_grid.grid = [ [ True for _ in range (1000) ] for _ in range (1000) ]
        light_grid.turn_off_lights((0, 0), (2, 2))

        for x, row in enumerate(light_grid.grid):
            for y, isLightOn in enumerate(row):
                if(not isLightOn):
                    self.assertIn(x, [0, 1, 2])
                    self.assertIn(y, [0, 1, 2])
                else:
                    self.assertTrue(x not in [0, 1, 2] or y not in [0, 1, 2])

    def testLightGrid_TurnOffLights_WithAllLightsOff_ShouldDoNothing(self):
        light_grid = LightGrid()
        light_grid.turn_off_lights((0, 0), (2, 2))

        for row in light_grid.grid:
            for isLightOn in row:
                self.assertFalse(isLightOn)
    
    def testLightGrid_ToogleLights_WithAllLightsOff_ShouldTurnOn(self):
        light_grid = LightGrid()
        light_grid.toggle_lights((0, 0), (2, 2))

        for x, row in enumerate(light_grid.grid):
            for y, isLightOn in enumerate(row):
                if(isLightOn):
                    self.assertIn(x, [0, 1, 2])
                    self.assertIn(y, [0, 1, 2])
                else:
                    self.assertTrue(x not in [0, 1, 2] or y not in [0, 1, 2])
        
    def testLightGrid_ToogleLights_WithAllLightsOn_ShouldTurnOff(self):
        light_grid = LightGrid()
        light_grid.grid = [ [ True for _ in range (1000) ] for _ in range (1000) ]
        light_grid.toggle_lights((0, 0), (2, 2))

        for x, row in enumerate(light_grid.grid):
            for y, isLightOn in enumerate(row):
                if(not isLightOn):
                    self.assertIn(x, [0, 1, 2])
                    self.assertIn(y, [0, 1, 2])
                else:
                    self.assertTrue(x not in [0, 1, 2] or y not in [0, 1, 2])

    def testLightGrid_ReadFileInput_WithTurnAllOnCommand_ShouldTurnOn(self):
        light_grid = LightGrid()
        light_grid.read_file_input(['turn on 0,0 through 999,999'])

        for row in light_grid.grid:
            for isLightOn in row:
                self.assertTrue(isLightOn)
        
    def testLightGrid_ReadFileInput_WithMultipleCommands_ShouldBeCorrect(self):
        light_grid = LightGrid()
        commands = [
            'turn on 0,0 through 5,5',
            'toggle 3,0 through 5,5',
            'turn off 0,3 through 5,5'
        ]
        light_grid.read_file_input(commands)

        for x, row in enumerate(light_grid.grid):
            for y, isLightOn in enumerate(row):
                if(isLightOn):
                    self.assertIn(x, [0, 1, 2])
                    self.assertIn(y, [0, 1, 2])
                else:
                    self.assertTrue(x not in [0, 1, 2] or y not in [0, 1, 2])

    def testBrightnessCalculator_IncreaseBrightness_WithPositiveQuantity_ShouldIncrease(self):
        calculator = BrightnessCalculator()
        calculator.increase_brightness(1, (0, 0), (3, 3))

        self.assertEqual(calculator.total_brightness, 16)

    def testBrightnessCalculator_IncreaseBrightness_WithNegativeQuantity_ShouldDecrease(self):
        calculator = BrightnessCalculator()
        calculator.increase_brightness(-1, (0, 0), (3, 3))

        self.assertEqual(calculator.total_brightness, -16)

    def testPart1_RunSolution_WithNormalCommands_ShouldBeCorrect(self):
        commands = [
            'turn on 0,0 through 999,999',
            'toggle 0,0 through 999,0',
            'turn off 499,499 through 500,500'
        ]
        expected_output = 998996
        output = part1_solution(commands)

        self.assertEqual(output, expected_output)
        
    def testPart1_RunSolution_WithOverllapingCommands_ShouldBeCorrect(self):
        commands = [
            'turn on 0,0 through 5,5',
            'toggle 3,0 through 5,5',
            'turn off 0,3 through 5,5'
        ]
        expected_output = 9
        output = part1_solution(commands)

        self.assertEqual(output, expected_output)
        
    def testPart2_RunSolution_WithSingleCommands_ShouldBeCorrect(self):
        test_cases = [
            ('turn on 0,0 through 0,0', 1),
            ('turn off 0,0 through 1,2', -6),
            ('toggle 0,0 through 999,999', 2000000)
        ]
        for input, expected_out in test_cases:
            output = part2_solution([ input ])
            self.assertEqual(output, expected_out)

    def testPart2_RunSolution_WithOverllapingCommands_ShouldBeCorrect(self):
        commands = [
            'turn on 0,0 through 5,5',
            'toggle 3,0 through 5,5',
            'turn off 0,3 through 5,5'
        ]
        expected_output = 54
        output = part2_solution(commands)

        self.assertEqual(output, expected_output)
        