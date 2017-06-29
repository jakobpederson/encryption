from itertools import zip_longest
from math import sqrt, ceil, floor


class Encryption():

    def encrypt_message(self, message):
        area = len(message)
        sq_root = sqrt(area)
        bottom = floor(sq_root)
        top = ceil(sq_root)
        dimensions = [
            (row, column) for row in range(0, area)
            for column in range(0, area)
            if row * column >= area and row < column
            and column <= top and row >= bottom
        ]
        if dimensions:
            columns = dimensions[0][1]
        else:
            columns = top
        grid = [
            list(message[x: x + columns])
            for x in range(0, area, columns)
        ]
        rotated_grid = self.row_column_swap(grid)
        stringified_grid = self.list_to_string(rotated_grid)
        return ' '.join(stringified_grid)

    def row_column_swap(self, grid):
        return [
            [i for i in element if i is not None]
            for element in list(zip_longest(*grid))
        ]

    def list_to_string(self, list_of_list_of_strings):
        return [''.join(x) for x in list_of_list_of_strings]
