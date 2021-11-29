# -- Common -- #
def parse_raw_input(raw_input):
    current_number = ''
    current_array = []

    def append_number():
        nonlocal current_array
        nonlocal current_number
        current_array.append(int(current_number))
        current_number = ''

    for char in raw_input:
        if(char == 'x'):
            append_number()
        elif(char == '\n'):
            append_number()
            yield current_array
            current_array = []
        else:
            current_number += char

    append_number()
    yield current_array

# -- Part 01 solutions -- #
class Part1_Solution01:
    def run(self, raw_input):
        total_sum = 0
        for dimension_arr in parse_raw_input(raw_input):
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

# -- Part 02 solutions -- #
class Part2_Solution01:
    def run(self, raw_input):
        total_sum = 0
        for dimension_arr in parse_raw_input(raw_input):
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

    print(Part1_Solution01().run(raw_input))
    print(Part2_Solution01().run(raw_input))
