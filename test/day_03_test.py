import unittest
from challenges.day_03 import *

class Day03_Common_Tests(unittest.TestCase):

    def test_GiftCurrentHouse_WithNewHouse_ShouldBeCorrect(self):
        walker = Day_03_Walker()
        walker._current_x = 1
        walker._current_y = 1
        walker.gift_current_house()

        gift_count = walker._houses_gifted[(1, 1)]
        self.assertEqual(gift_count, 1)

    def test_GiftCurrentHouse_WithExistingHouse_ShouldBeCorrect(self):
        walker = Day_03_Walker()
        walker.gift_current_house()

        gift_count = walker._houses_gifted[(0, 0)]
        self.assertEqual(gift_count, 2)

    def test_Walk_WithSingleInstruction_ShouldBeCorrect(self):
        test_cases = [
            ("^", (0, 1)),
            ("v", (0, -1)),
            (">", (1, 0)),
            ("<", (-1, 0))
        ]
        for (input, output) in test_cases:
            walker = Day_03_Walker()
            walker.walk(input)
            self.assertEqual(walker.get_current_coord(), output)

class Day03_Part01_Tests(unittest.TestCase):

    def test_RunSolution_ShouldBeCorrect(self):
        test_cases = [
            ('>', 2),
            ('^>v<', 4),
            ('^v^v^v^v^v', 2)
        ]
        for (input, output) in test_cases:
            result = day_03_part_1_solution(input)
            self.assertEqual(result, output)

class Day03_Part02_Tests(unittest.TestCase):

    def test_RunSolution_ShouldBeCorrect(self):
        test_cases = [
            ('^v', 3),
            ('^>v<', 3),
            ('^v^v^v^v^v', 11)
        ]
        for (input, output) in test_cases:
            result = day_03_part_2_solution(input)
            self.assertEqual(result, output)
