import unittest
from challenges.day_05 import *

class Day05_Tests(unittest.TestCase):

    def testFirstChecker_ResetStringChecker_WithNormalValues_ShouldBeDefault(self):
        checker = FirstStringChecker()
        checker.last_char = 'a'
        checker.vowel_count = 20
        checker.is_naughty = True
        checker.has_three_vowels = True
        checker.has_double_letters = True

        checker.reset()
        self.assertEqual(checker.last_char, '')
        self.assertEqual(checker.vowel_count, 0)
        self.assertEqual(checker.is_naughty, False)
        self.assertEqual(checker.has_three_vowels, False)
        self.assertEqual(checker.has_double_letters, False)

    def testFirstChecker_CheckNextChar_WithNaughtyWords_ShouldBeNaughty(self):
        naughty_strings = ['ab', 'cd', 'pq', 'xy']
        for [first_char, second_char] in naughty_strings:
            checker = FirstStringChecker()
            checker.last_char = first_char
            checker.check_next_char(second_char)

            self.assertTrue(checker.is_naughty)

    def testFirstChecker_CheckNextChar_WithDoubledChars_ShouldHasDoubled(self):
        naughty_strings = ['a', 'b', 'c', 'd']
        for char in naughty_strings:
            checker = FirstStringChecker()

            for _ in range(2):
                checker.check_next_char(char)

            self.assertTrue(checker.has_double_letters)

    def testFirstChecker_CheckNextChar_WithVowels_ShouldIncrementVowelCount(self):
        vowels = ['a', 'e', 'i', 'o', 'u']
        for char in vowels:
            checker = FirstStringChecker()
            checker.check_next_char(char)

            self.assertEqual(checker.vowel_count, 1)

    def testFirstChecker_CheckNextChar_WithVowelsAndCount2_ShouldHaveThreeVowels(self):
        vowels = ['a', 'e', 'i', 'o', 'u']
        for char in vowels:
            checker = FirstStringChecker()
            checker.vowel_count = 2
            checker.check_next_char(char)

            self.assertTrue(checker.has_three_vowels)

    def testFirstChecker_CheckNextChar_WithNiceStrings_ShouldBeNice(self):
        nice_strings = [
            'ugknbfddgicrmopn',
            'aaa'
        ]
        for string in nice_strings:
            checker = FirstStringChecker()

            for char in string:
                checker.check_next_char(char)

            self.assertTrue(checker.get_is_nice())

    def testFirstChecker_CheckNextChar_WithNaughtyStrings_ShouldNotBeNice(self):
        nice_strings = [
            'jchzalrnumimnmhp',
            'haegwjzuvuyypxyu',
            'dvszwmarrgswjxmb'
        ]
        for string in nice_strings:
            checker = FirstStringChecker()

            for char in string:
                checker.check_next_char(char)

            self.assertFalse(checker.get_is_nice())

    def testScndChecker_ResetStringChecker_WithNormalValues_ShouldBeDefault(self):
        checker = ScndStringChecker()
        self.word = 'abcde'
        self.previous_char = 'e'
        self.has_repeat_pair = True
        self.has_sparsed_letters = True

        checker.reset()
        self.assertEqual(checker.word, '')
        self.assertEqual(checker.previous_char, '')
        self.assertEqual(checker.has_repeat_pair, False)
        self.assertEqual(checker.has_sparsed_letters, False)

    def testScndChecker_CheckNextChar_WithRepeatPairs_ShouldHaveRepeatLetters(self):
        cases = [
            'qjhvhtzxzqqjkmpb',
            'xxyxx',
            'uurcxstgmygtbstg',
            'xyxy'
        ]
        for case_str in cases:
            checker = ScndStringChecker()
            
            for char in case_str:
                checker.check_next_char(char)

            self.assertTrue(checker.has_repeat_pair)

    def testScndChecker_CheckNextChar_WithInvalidRepeatPairs_ShouldNotHaveRepeatLetters(self):
        cases = [
            'aaa'
        ]
        for case_str in cases:
            checker = ScndStringChecker()
            
            for char in case_str:
                checker.check_next_char(char)

            self.assertFalse(checker.has_repeat_pair)

    def testScndChecker_CheckNextChar_WithSparsedLetters_ShouldHaveSparsedLetters(self):
        cases = [
            'qjhvhtzxzqqjkmpb',
            'qjhvhtzxzqqj',
            'xxyxx',
            'ieodomkazucvgmuy',
            'aaa'
        ]
        for case_str in cases:
            checker = ScndStringChecker()
            
            for char in case_str:
                checker.check_next_char(char)

            self.assertTrue(checker.has_sparsed_letters)

    def testScndChecker_CheckNextChar_WithNiceStrings_ShouldBeNice(self):
        cases = [
            'qjhvhtzxzqqjkmpb',
            'xxyxx'
        ]
        for case_str in cases:
            checker = ScndStringChecker()
            
            for char in case_str:
                checker.check_next_char(char)

            self.assertTrue(checker.get_is_nice())

    def testScndChecker_CheckNextChar_WithNaughtyStrings_ShouldNotBeNice(self):
        cases = [
            'uurcxstgmygtbstg',
            'ieodomkazucvgmuy'
        ]
        for case_str in cases:
            checker = ScndStringChecker()
            
            for char in case_str:
                checker.check_next_char(char)

            self.assertFalse(checker.get_is_nice())

    def testNiceStringCounter_CheckInput_WithSingleNiceStr_ShouldHaveOne(self):
        counter = NiceStringCounter(FirstStringChecker(), 'aaa')
        counter.check_input()

        self.assertEqual(counter.nice_count, 1)

    def test_RunSolution_WithPart1_ShouldResolve(self):
        raw_test_input = '''ugknbfddgicrmopn
aaa
jchzalrnumimnmhp
haegwjzuvuyypxyu
dvszwmarrgswjxmb'''
        result = part1_solution(raw_test_input)
        self.assertEqual(result, 2)

    def test_RunSolution_WithPart2_ShouldResolve(self):
        raw_test_input = '''qjhvhtzxzqqjkmpb
uurcxstgmygtbstg
ieodomkazucvgmuy
xxyxx'''
        result = part2_solution(raw_test_input)
        self.assertEqual(result, 2)
