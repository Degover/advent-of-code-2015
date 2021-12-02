def part1_solution(input):
    switch = {
        "(": +1,
        ")": -1
    }
    final_floor = 0
    for char in input:
        final_floor += switch.get(char)
    
    return final_floor

def part2_solution(input):
    switch = {
        "(": +1,
        ")": -1
    }
    current_floor = 0
    index = 0
    for char in input:
        current_floor += switch.get(char)
        index += 1

        if(current_floor == -1):
            break
    
    return index

if __name__ == '__main__':
    input = open('inputs/01.txt', 'r').read()

    print(part1_solution(input))
    print(part2_solution(input))
