import math


class Encryption():

    def encrypt_message(self, message):
        area = len(message)
        test = [(x, y) for x in range(2, int(area/2)) for y in range(2, int(area/2) + 1)
                if x < y and x * y == area and x >= math.floor(math.sqrt(area)) and y <= math.ceil(math.sqrt(area))]
        print(area)
        print(math.floor(math.sqrt(10)))
        print(math.ceil(math.sqrt(10)))
        rows = test[0][0]
        cols = test[0][1]
        n = cols
        grid = [list(message[x: x + n]) for x in range(0, area, n)]
        print(grid)
        answer = []
        for x in range(0, cols):
            for y in range(0, rows):
                answer.append(grid[y][x])
        new_answer = [''.join(answer[i:i+rows]) for i in range(0, len(answer), rows)]
        print(new_answer)
        return ' '.join(new_answer)
