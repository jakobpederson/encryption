from math import sqrt, ceil, floor


class Encryption():

    def encrypt_message(self, message):
        print('start')
        area = len(message)
        print('area', area)
        sq_root = sqrt(area)
        print('sqrt', sq_root)
        bottom = floor(sq_root)
        top = ceil(sq_root)
        print('floor {} ceil {}'.format(bottom, top))
        dimensions = [
            (row, column) for row in range(0, area)
            for column in range(0, area)
            if row * column >= area and row < column
            and column <= top and row <= bottom
        ]
        rows = dimensions[0][0]
        columns = dimensions[0][1]
        grid = [list(message[x: x + columns]) for x in range(0, area, columns)]
        rotated_grid = self.row_column_swap(grid)
        stringified_grid = self.list_to_string(rotated_grid)
        return ' '.join(stringified_grid)

    def row_column_swap(self, grid):
        from itertools import zip_longest
        result = [
            [i for i in element if i is not None]
            for element in list(zip_longest(*grid))]
        return result

    def list_to_string(self, list_of_list_of_strings):
        new_list = []
        for x in list_of_list_of_strings:
            new_list.append(''.join(x))
        return new_list
