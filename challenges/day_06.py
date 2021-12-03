import re as regex

class LightGrid:

    def __init__(self):
        self.grid = [ [ False for _ in range (1000) ] for _ in range (1000) ]

    def execute_command(self, command, coor_a, coor_b):
        lambda_fn = None
        if command == 'toggle':
            lambda_fn = lambda state: not state
        elif command == 'turn on':
            lambda_fn = lambda _: True
        else: # turn off
            lambda_fn = lambda _: False
        
        for x in range(coor_a[0], coor_b[0] + 1):
            for y in range(coor_a[1], coor_b[1] + 1):
                isLightOn = self.grid[x][y]
                self.grid[x][y] = lambda_fn(isLightOn)

    def read_file_input(file_input):
        coord_regex = regex.compile('(\d+),(\d+) through (\d+),(\d+)')

        for line in file_input:
            match = coord_regex.search(line)
            coord_a = match.group(1, 2)
            coord_b = match.group(3, 4)