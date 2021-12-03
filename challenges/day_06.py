import re as regex

class LightInstructionInterpreter:
    
    def read_file_input(self, file_input):
        coord_regex = regex.compile('(\d+),(\d+) through (\d+),(\d+)')

        for line in file_input:
            match = coord_regex.search(line)
            coord_a = tuple((int(i) for i in match.group(1, 2)))
            coord_b = tuple((int(i) for i in match.group(3, 4)))

            if line.startswith('toggle'):
                self.toggle_lights(coord_a, coord_b)
            elif line.startswith('turn on'):
                self.turn_on_lights(coord_a, coord_b)
            else:
                self.turn_off_lights(coord_a, coord_b)

    def toggle_lights(self, coord_a, coord_b): pass
    def turn_on_lights(self, coord_a, coord_b): pass
    def turn_off_lights(self, coord_a, coord_b): pass

class LightGrid(LightInstructionInterpreter):

    def __init__(self):
        self.grid = [ [ False for _ in range (1000) ] for _ in range (1000) ]

    def execute_command(self, command_fn, coor_a, coor_b):
        for x in range(coor_a[0], coor_b[0] + 1):
            for y in range(coor_a[1], coor_b[1] + 1):
                isLightOn = self.grid[x][y]
                self.grid[x][y] = command_fn(isLightOn)

    def toggle_lights(self, coord_a, coord_b):
        self.execute_command(lambda state: not state, coord_a, coord_b)

    def turn_on_lights(self, coord_a, coord_b):
        self.execute_command(lambda _: True, coord_a, coord_b)

    def turn_off_lights(self, coord_a, coord_b):
        self.execute_command(lambda _: False, coord_a, coord_b)

class BrightnessCalculator(LightInstructionInterpreter):

    def __init__(self):
        self.total_brightness = 0

    def increase_brightness(self, quantity, coord_a, coord_b):
        diff_x = coord_b[0] - coord_a[0] + 1
        diff_y = coord_b[1] - coord_a[1] + 1
        self.total_brightness += quantity * (diff_x * diff_y)

    def toggle_lights(self, coord_a, coord_b):
        self.increase_brightness(2, coord_a, coord_b)

    def turn_on_lights(self, coord_a, coord_b):
        self.increase_brightness(1, coord_a, coord_b)

    def turn_off_lights(self, coord_a, coord_b):
        self.increase_brightness(-1, coord_a, coord_b)

def part1_solution(file_input):
    light_grid = LightGrid()
    light_grid.read_file_input(file_input)

    result = sum([ sum([ 1 for isOn in array if isOn ]) for array in light_grid.grid ])
    return result

def part2_solution(file_input):
    calculator = BrightnessCalculator()
    calculator.read_file_input(file_input)

    return calculator.total_brightness

if __name__ == '__main__':
    with open('inputs/06.txt', 'r') as file:
        print(part1_solution(file))

    with open('inputs/06.txt', 'r') as file:
        print(part2_solution(file))
