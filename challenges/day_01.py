# -- Part 01 solutions -- #
def part_1_solution_01(input):
    switch = {
        "(": +1,
        ")": -1
    }
    final_floor = 0
    for char in input:
        final_floor += switch.get(char)
    
    return final_floor

def part_1_solution_02(input):
    final_floor = 0
    for char in input:
        if(char == "("):
            final_floor += 1
        else:
            final_floor -= 1
    
    return final_floor

# -- Part 02 solutions -- #
def part_2_solution_01(input):
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

    print(part_1_solution_01(input))
    print(part_2_solution_01(input))
