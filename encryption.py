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
        print('grid', grid)
        answer = []
        complete = self.row_column_swap(grid)
        for value in range(0, columns):
            for lst in grid:
                try:
                    if lst[value]:
                        answer.extend(lst[value])
                except:
                    continue
        new_answer = [''.join(answer[i:i+rows]) for i in range(0, len(answer), rows)]
        print('new_answer', self.row_column_swap(grid))
        return ' '.join(new_answer)

    def row_column_swap(self, grid):
        from itertools import zip_longest
        result = [
            [i for i in element if i is not None]
            for element in list(zip_longest(*grid))]
        return result

