import numpy as np
import matplotlib as plt


class Game:

    def __init__(self):
        self.size = 4
        self.score = 0
        self.board = np.zeros([self.size, self.size], dtype=int)

        # insert 2 tiles
        self.insert_tile()
        self.insert_tile()
        #self.print_board()

    def insert_tile(self):
        if self.ended():
            return
        x, y = np.random.randint(0, self.size, 2)
        while self.board[x][y] != 0:
            x, y = np.random.randint(0, self.size, 2)

        # 20% 4, 80% 2
        value = 2 if np.random.uniform() > 0.8 else 4
        self.board[x][y] = value

    def print_board(self):
        print("************")
        for row in self.board:
            print('\t'.join(map(str, row)))
        print("Score: {}".format(self.score))
        print("************")

    def move(self, direction):
        if direction == "Left":
            if not self.check_left():
                return
            for x in range(self.size):
                for y in range(1, self.size):
                    if self.board[x][y] == 0:
                        continue
                    d = 0
                    while self.board[x][y-d-1] == 0 and y > d:
                        d += 1
                    if d != 0:
                        self.board[x][y-d] = self.board[x][y]
                        self.board[x][y] = 0

                    if y != d and self.board[x][y-d] == self.board[x][y-d-1]:
                        self.board[x][y-d] = 0
                        self.board[x][y-d-1] *= 2
                        self.score += self.board[x][y-d-1]

        elif direction == "Right":
            if not self.check_right():
                return
            for x in range(self.size):
                for y in range(self.size):
                    if self.board[x][y] == 0:
                        continue
                    d = 0
                    while y + d < self.size-1 and self.board[x][y+d+1] == 0:
                        d += 1
                    if d != 0:
                        self.board[x][y+d] = self.board[x][y]
                        self.board[x][y] = 0

                    if y+d != self.size-1 and self.board[x][y+d] == self.board[x][y+d+1]:
                        self.board[x][y+d] = 0
                        self.board[x][y+d+1] *= 2
                        self.score += self.board[x][y+d+1]

        elif direction == "Up":
            if not self.check_up():
                return
            for x in range(self.size):
                for y in range(self.size):
                    if self.board[x][y] == 0:
                        continue
                    d = 0
                    while x > d and self.board[x-d-1][y] == 0:
                        d += 1
                    if d != 0:
                        self.board[x-d][y] = self.board[x][y]
                        self.board[x][y] = 0

                    if x != d and self.board[x-d][y] == self.board[x-d-1][y]:
                        self.board[x-d][y] = 0
                        self.board[x-d-1][y] *= 2
                        self.score += self.board[x-d-1][y]

        elif direction == "Down":
            if not self.check_down():
                return
            for x in range(self.size):
                for y in range(self.size):
                    if self.board[x][y] == 0:
                        continue
                    d = 0
                    while x+d < self.size-1 and self.board[x+d+1][y] == 0:
                        d += 1
                    if d != 0:
                        self.board[x+d][y] = self.board[x][y]
                        self.board[x][y] = 0

                    if x+d != self.size-1 and self.board[x+d][y] == self.board[x+d+1][y]:
                        self.board[x+d][y] = 0
                        self.board[x+d+1][y] *= 2
                        self.score += self.board[x+d+1][y]
        else:
            print("B R U H")

        self.insert_tile()

    def check_left(self):
        for x in range(self.size):
            for y in range(self.size):
                if self.board[x][y] == 0 and y < self.size-1:
                    return True
                if y > 0 and self.board[x][y] == self.board[x][y-1]:
                    return True
        #print("Cannot go Left")
        return False

    def check_right(self):
        for x in range(self.size):
            for y in range(self.size):
                if self.board[x][y] == 0 and y > 0:
                    return True
                if y < self.size-1 and self.board[x][y] == self.board[x][y+1]:
                    return True
        #print("Cannot go Right")
        return False

    def check_up(self):
        for x in range(self.size):
            for y in range(self.size):
                if self.board[x][y] == 0 and x < self.size-1:
                    return True
                if x > 0 and self.board[x][y] == self.board[x-1][y]:
                    return True
        #print("Cannot go Up")
        return False

    def check_down(self):
        for x in range(self.size):
            for y in range(self.size):
                if self.board[x][y] == 0 and x > 0:
                    return True
                if x < self.size-1 and self.board[x][y] == self.board[x-1][y]:
                    return True
        #print("Cannot go Down")
        return False

    def ended(self):
        if self.check_left() or self.check_right() or self.check_up() or self.check_down():
            return False
        else:
            print("ended")
            return True

