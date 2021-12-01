import hashlib

# -- Common -- #
class HashCrawler:

    def __init__(self, key):
        self.key = key
        self.current_index = 0

    def get_next(self):
        self.current_index += 1
        str_to_hash = self.key + str(self.current_index)
        hash = hashlib.md5(str_to_hash.encode('utf-8')).hexdigest()
        return (self.current_index, hash)

    def generate_hashes(self):
        while(True):
            yield self.get_next()

# -- Part 1 -- #
def part1_solution(input):
    crawler = HashCrawler(input)
    for [index, hash] in crawler.generate_hashes():
        if(hash.startswith('00000')):
            return index

# -- Part 2 -- #
def part2_solution(input):
    crawler = HashCrawler(input)
    for [index, hash] in crawler.generate_hashes():
        if(hash.startswith('000000')):
            return index

if __name__ == '__main__':
    input = open('inputs/04.txt', 'r').read()

    print(part1_solution(input))
    print(part2_solution(input))
