import unittest
from challenges.day_02 import *

class Day02_Part01_Tests(unittest.TestCase):
    rawInput = f'''3x11x24
13x5x19
1x9x27
24x8x21
6x8x17
19x18x22'''
    parsedInput = [[3,11,24],[13,5,19],[1,9,27],[24,8,21],[6,8,17],[19,18,22]]
    calculatedFaces = [
        [33, 72, 264],
        [65, 247, 95],
        [9, 27, 243],
        [192, 504, 168],
        [48, 102, 136],
        [342, 418, 396]
    ]

    def test_parseRawInput_ShouldParse(self):
        obj = Part1_Solution01()
        index = 0
        for parsedArr in obj._parse_raw_input(self.rawInput):
            self.assertListEqual(parsedArr, self.parsedInput[index])
            index += 1

    def test_calculateFacesAreas_ShouldBeCorrect(self):
        obj = Part1_Solution01()
        for index in range(0, len(self.parsedInput)):
            result = obj._calculate_faces_areas(self.parsedInput[index])
            self.assertListEqual(result, self.calculatedFaces[index])

    def test_runSolution_ShouldBeCorrect(self):
        obj = Part1_Solution01()
        self.assertEqual(obj.run(self.rawInput), 7387)


