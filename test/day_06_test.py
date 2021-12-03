import unittest
from challenges.day_06 import *

class Day_06_Tests(unittest.TestCase):

    def testLightGrid_ExecuteCommand_WithTurnOnCommandAndAllLightsOff_ShouldTurnOn(self):
        light_grid = LightGrid()
        light_grid.execute_command('turn on', (0, 0), (2, 2))

        for x, row in enumerate(light_grid.grid):
            for y, isLightOn in enumerate(row):
                if(isLightOn):
                    self.assertIn(x, [0, 1, 2])
                    self.assertIn(y, [0, 1, 2])
                else:
                    self.assertTrue(x not in [0, 1, 2] or y not in [0, 1, 2])
        
    def testLightGrid_ExecuteCommand_WithTurnOnCommandAndAllLightsOn_ShouldDoNothing(self):
        light_grid = LightGrid()
        light_grid.grid = [ [ True for _ in range (1000) ] for _ in range (1000) ]
        light_grid.execute_command('turn on', (0, 0), (2, 2))

        for row in light_grid.grid:
            for isLightOn in row:
                self.assertTrue(isLightOn)
        
    def testLightGrid_ExecuteCommand_WithTurnOffCommandAndAllLightsOn_ShouldTurnOff(self):
        light_grid = LightGrid()
        light_grid.grid = [ [ True for _ in range (1000) ] for _ in range (1000) ]
        light_grid.execute_command('turn off', (0, 0), (2, 2))

        for x, row in enumerate(light_grid.grid):
            for y, isLightOn in enumerate(row):
                if(not isLightOn):
                    self.assertIn(x, [0, 1, 2])
                    self.assertIn(y, [0, 1, 2])
                else:
                    self.assertTrue(x not in [0, 1, 2] or y not in [0, 1, 2])

    def testLightGrid_ExecuteCommand_WithTurnOffCommandAndAllLightsOff_ShouldDoNothing(self):
        light_grid = LightGrid()
        light_grid.execute_command('turn off', (0, 0), (2, 2))

        for row in light_grid.grid:
            for isLightOn in row:
                self.assertFalse(isLightOn)
    
    def testLightGrid_ExecuteCommand_WithToggleCommandAndAllLightsOff_ShouldTurnOn(self):
        light_grid = LightGrid()
        light_grid.execute_command('toggle', (0, 0), (2, 2))

        for x, row in enumerate(light_grid.grid):
            for y, isLightOn in enumerate(row):
                if(isLightOn):
                    self.assertIn(x, [0, 1, 2])
                    self.assertIn(y, [0, 1, 2])
                else:
                    self.assertTrue(x not in [0, 1, 2] or y not in [0, 1, 2])
        
    def testLightGrid_ExecuteCommand_WithToggleCommandAndAllLightsOn_ShouldTurnOff(self):
        light_grid = LightGrid()
        light_grid.grid = [ [ True for _ in range (1000) ] for _ in range (1000) ]
        light_grid.execute_command('toggle', (0, 0), (2, 2))

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
        commands = ['turn on 0,0 through 999,999']
        light_grid.read_file_input(commands)

        for row in light_grid.grid:
            for isLightOn in row:
                self.assertTrue(isLightOn)
        
        
        