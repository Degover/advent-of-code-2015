import unittest
from challenges.day_01 import *

test_cases_part1 =[
        ("(())", 0),
        ("()()", 0),
        ("(((", 3),
        ("(()(()(", 3),
        ("))(((((", 3),
        ("())", -1),
        ("))(", -1),
        (")))", -3),
        (")())())", -3)
    ]

test_cases_part2 =[
        ("))(((((", 1),
        ("())", 3),
        ("))(", 1),
        (")))", 1),
        (")())())", 1),
        (")", 1),
        ("()())", 5)
    ]    

class Day01_Part01_Tests(unittest.TestCase):

    def test_solution01_correctResults(self):
        for test_case in test_cases_part1:
            self.assertEqual(part_1_solution_01(test_case[0]), test_case[1])

    def test_solution02_correctResults(self):
        for test_case in test_cases_part1:
            self.assertEqual(part_1_solution_02(test_case[0]), test_case[1])

class Day01_Part02_Tests(unittest.TestCase):

    def test_solution01_correctResults(self):
        for test_case in test_cases_part2:
            self.assertEqual(part_2_solution_01(test_case[0]), test_case[1])

