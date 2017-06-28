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
        print(grid)
        answer = []
        for value in range(0, columns):
            for lst in grid:
                try:
                    if lst[value]:
                        answer.append(lst[value])
                except:
                    continue
                # answer.append(grid[row][column])
        new_answer = [''.join(answer[i:i+rows]) for i in range(0, len(answer), rows)]
        print('new_answer', new_answer)
        return ' '.join(new_answer)
