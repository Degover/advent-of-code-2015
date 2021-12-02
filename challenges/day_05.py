class IStringChecker:
    def reset(self): pass
    def check_next_char(self, char): pass
    def get_is_nice(self): pass

class FirstStringChecker(IStringChecker):
    VOWELS = ['a', 'e', 'i', 'o', 'u']
    NAUGHTY_STRINGS = ['ab', 'cd', 'pq', 'xy']

    def __init__(self):
        self.reset()

    def reset(self):
        self.last_char = ''
        self.vowel_count = 0

        self.is_naughty = False
        self.has_three_vowels = False
        self.has_double_letters = False

    def check_next_char(self, char):
        if self.is_naughty: return
        
        if (self.last_char + char) in self.NAUGHTY_STRINGS:
            self.is_naughty = True
            return

        if not self.has_three_vowels and char in self.VOWELS:
            self.vowel_count += 1
            self.has_three_vowels = self.vowel_count == 3
        
        if not self.has_double_letters and char == self.last_char:
            self.has_double_letters = True

        self.last_char = char

    def get_is_nice(self):
        return self.has_three_vowels and self.has_double_letters and not self.is_naughty

class ScndStringChecker(IStringChecker):

    def __init__(self):
        self.reset()

    def reset(self):
        self.word = ''
        self.previous_char = ''

        self.has_repeat_pair = False
        self.has_sparsed_letters = False

    def check_next_char(self, char):
        if self.has_repeat_pair and self.has_sparsed_letters:
            return

        if not self.has_repeat_pair and (self.previous_char + char) in self.word:
            self.has_repeat_pair = True

        if not self.has_sparsed_letters and len(self.word) > 0 and self.word[-1] == char:
            self.has_sparsed_letters = True

        self.word += self.previous_char
        self.previous_char = char

    def get_is_nice(self):
        return self.has_repeat_pair and self.has_sparsed_letters

class NiceStringCounter:

    def __init__(self, checker, raw_input):
        self.raw_input = raw_input
        self.checker = checker
        self.nice_count = 0

    def check_input(self):
        for char in self.raw_input:
            if char == '\n':
                self.count_current()
                self.checker.reset()
            
            self.checker.check_next_char(char)
        self.count_current()

    def count_current(self):
        if self.checker.get_is_nice():
            self.nice_count += 1

def part1_solution(raw_input):
    counter = NiceStringCounter(FirstStringChecker(), raw_input)
    counter.check_input()
    return counter.nice_count

def part2_solution(raw_input):
    counter = NiceStringCounter(ScndStringChecker(), raw_input)
    counter.check_input()
    return counter.nice_count

if __name__ == '__main__':
    input = open('inputs/05.txt', 'r').read()

    print(part1_solution(input))
    print(part2_solution(input))