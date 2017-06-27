

class Encryption():

    def encrypt_message(self, message):
        area = len(message)
        test = [(x, y) for x in range(2, int(area/2)) for y in range(2, int(area/2) + 1)
                if x < y and x * y == area]
        print(area)
        print(test)
        n = 4
        grid = [[message[x: x + n]] for x in range(0, area, n)]
        print(grid)
        return 0
