import unittest
from challenges.day_02 import *

rawInput = f'''3x11x24
13x5x19
1x9x27
24x8x21
6x8x17
19x18x22'''
parsedInput = [
    [3,11,24],
    [13,5,19],
    [1,9,27],
    [24,8,21],
    [6,8,17],
    [19,18,22]
]
calculatedFaces = [
    [33, 72, 264],
    [65, 247, 95],
    [9, 27, 243],
    [192, 504, 168],
    [48, 102, 136],
    [342, 418, 396]
]
calculatedShortestPerimeters = [28, 36, 20, 58, 28, 74]
calculatedCubicVolume = [792, 1235, 243, 4032, 816, 7524]

class Day02_Part01_Tests(unittest.TestCase):

    def test_parseRawInput_ShouldParse(self):
        index = 0
        for parsedArr in parse_raw_input(rawInput):
            self.assertListEqual(parsedArr, parsedInput[index])
            index += 1

    def test_calculateFacesAreas_ShouldBeCorrect(self):
        obj = Part1_Solution01()
        for index in range(0, len(parsedInput)):
            result = obj._calculate_faces_areas(parsedInput[index])
            self.assertListEqual(result, calculatedFaces[index])

    def test_runSolution_ShouldBeCorrect(self):
        obj = Part1_Solution01()
        self.assertEqual(obj.run(rawInput), 7387)


class Day02_Part02_Tests(unittest.TestCase):

    def test_parseRawInput_ShouldParse(self):
        index = 0
        for parsedArr in parse_raw_input(rawInput):
            self.assertListEqual(parsedArr, parsedInput[index])
            index += 1

    def test_calculateShortestPerimeter_ShouldBeCorrect(self):
        obj = Part2_Solution01()
        for index in range(0, len(parsedInput)):
            copied_list = parsedInput[index].copy()
            result = obj._calculate_shortest_perimeter(copied_list)
            self.assertEqual(result, calculatedShortestPerimeters[index])

    def test_calculateCubicVolume_ShouldBeCorrect(self):
        obj = Part2_Solution01()
        for index in range(0, len(parsedInput)):
            result = obj._calculate_cubic_volume(parsedInput[index])
            self.assertEqual(result, calculatedCubicVolume[index])

    def test_runSolution_ShouldBeCorrect(self):
        obj = Part2_Solution01()
        self.assertEqual(obj.run(rawInput), 14886)
