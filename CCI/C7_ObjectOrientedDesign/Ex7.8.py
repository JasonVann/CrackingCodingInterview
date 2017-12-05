class Game():
    def __init__(self, size):
        self.size = size
        self.pieces1 = [piece('W')] * size
        self.pieces2 = [piece('B')] * size
        self.board = []

    def move(self, i, j):
        if move_valid(i, j):
            piece.capture()

    def move_valid(self, i, j):
        pass

    def score(self):
        count1 = 0
        for p in self.pieces1:
            if p.color == 'W':
                count1 += 1
        for p in self.pieces2:
            if p.color == 'W':
                count1 += 1
        count2 = self.size * 2 - count1
        if count1 > count2:
            print('Player 1 wins')
        elif count1 == count2:
            print("It's a draw")
        else:
            print('Player 2 wins')

class Piece():
    def __init__(self, color):
        self.color = color

    def capture(self):
        if self.color == 'W':
            self.color = 'B'
        else:
            self.color = 'W'
