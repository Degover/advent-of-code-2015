class HouseWalker:
    def __init__(self):
        self._current_x = 0
        self._current_y = 0
        self._houses_gifted = {
            (0, 0): 1
        }

    def gift_current_house(self):
        house_coord = self.get_current_coord()
        if(house_coord in self._houses_gifted):
            self._houses_gifted[house_coord] += 1
        else:
            self._houses_gifted[house_coord] = 1

    def walk(self, char_instruct):
        if(char_instruct == "^"):
            self._current_y += 1
        elif(char_instruct == "v"):
            self._current_y -= 1
        elif(char_instruct == ">"):
            self._current_x += 1
        else:
            self._current_x -= 1

    def get_current_coord(self):
        return (self._current_x, self._current_y)

def part1_solution(input):
    walker = HouseWalker()
    for char in input:
        walker.walk(char)
        walker.gift_current_house()
    
    return len(walker._houses_gifted)

def part2_solution(input):
    santa_walker = HouseWalker()
    robo_santa_walker = HouseWalker()

    santa_walker._houses_gifted = robo_santa_walker._houses_gifted

    santa_turn = True
    for char in input:
        if(santa_turn):
            santa_walker.walk(char)
            santa_walker.gift_current_house()
        else:
            robo_santa_walker.walk(char)
            robo_santa_walker.gift_current_house()
        santa_turn = not santa_turn
    
    return len(santa_walker._houses_gifted)

if __name__ == '__main__':
    raw_input = open('inputs/03.txt', 'r').read()

    print(part1_solution(raw_input))
    print(part2_solution(raw_input))