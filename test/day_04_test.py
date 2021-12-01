import unittest
from challenges.day_04 import *

class Day04_Part01_Tests(unittest.TestCase):

    def test_RunSolution_ShouldResolve(self):
        test_cases = [
            ('abcdef', 609043),
            ('pqrstuv', 1048970)
        ]
        for (input, output) in test_cases:
            result = part1_solution(input)
            self.assertEqual(result, output)