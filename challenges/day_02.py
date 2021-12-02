class InputParser:

    def __init__(self, raw_input):
        self.raw_input = raw_input
        self.current_number = ''
        self.current_array = []

    def append_number(self):    
        self.current_array.append(int(self.current_number))
        self.current_number = ''

    def parse(self):
        for char in self.raw_input:
            if(char == 'x'):
                self.append_number()

            elif(char == '\n'):
                self.append_number()
                yield self.current_array
                self.current_array = []

            else:
                self.current_number += char

        self.append_number()
        yield self.current_array

class Part1_Solution:

    def run(self, raw_input):
        total_sum = 0
        parser = InputParser(raw_input)

        for dimension_arr in parser.parse():
            faces_arr = self._calculate_faces_areas(dimension_arr)
            smallest_face = faces_arr[0]

            for face_size in faces_arr:
                total_sum += face_size * 2

                if(face_size < smallest_face):
                    smallest_face = face_size

            total_sum += smallest_face

        return total_sum

    def _calculate_faces_areas(self, dimensions_array):
        return [
            dimensions_array[0] * dimensions_array[1],
            dimensions_array[0] * dimensions_array[2],
            dimensions_array[1] * dimensions_array[2]
        ]

class Part2_Solution:
    
    def run(self, raw_input):
        total_sum = 0
        parser = InputParser(raw_input)

        for dimension_arr in parser.parse():
            total_sum += self._calculate_cubic_volume(dimension_arr)
            total_sum += self._calculate_shortest_perimeter(dimension_arr)

        return total_sum

    def _calculate_shortest_perimeter(self, dimensions_array):
        dimensions_array.sort()
        [dim1, dim2, _] = dimensions_array
        return 2*dim1 + 2*dim2

    def _calculate_cubic_volume(self, dimensions_array):
        return dimensions_array[0] *  dimensions_array[1] *  dimensions_array[2]
        
if __name__ == '__main__':
    raw_input = open('inputs/02.txt', 'r').read()

    print(Part1_Solution().run(raw_input))
    print(Part2_Solution().run(raw_input))
