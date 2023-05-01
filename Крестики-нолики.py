from random import randint

class Board:
    def __init__(self, height=3, width=3):
        self.height = height
        self.width = width
        self.cells = [[' '] * self.width for i in range(self.height)]

    def put(self, x, y, symb):
        self.cells[y][x] = symb

    def check(self, x, y):
        return self.cells[y][x] == ' '

    def print(self):
        title = '   '
        for i in range(self.width):
            title += f'   {i + 1}  '
        print(title)
        border = '   ' + '+-----' * self.width + '+'
        print(border)
        for i in range(self.height):
            row = f' {i + 1} |'
            for j in range(self.width):
                row += f'  {self.cells[i][j]}  |'
            print(row)
            print(border)

    def checker(self, symb):
        for i in range(self.height):
            for j in range(self.width):
                if (i == 0 or i == self.height - 1) and 0 < j < self.width - 1:
                    if self.cells[i][j - 1] == self.cells[i][j] == self.cells[i][j + 1] == symb: #горизонтальная линия
                        return True
                if (j == 0 or j == self.width - 1) and 0 < i < self.height - 1:
                    if self.cells[i - 1][j] == self.cells[i][j] == self.cells[i + 1][j] == symb: #вертикальная линия
                        return True
                if i > 0 and j > 0 and i < self.height - 1 and j < self.width - 1:
                    if self.cells[i][j - 1] == self.cells[i][j] == self.cells[i][j + 1] == symb: #горизонтальная линия
                        return True
                    if self.cells[i - 1][j] == self.cells[i][j] == self.cells[i + 1][j] == symb: #вертикальная линия
                        return True
                    if self.cells[i - 1][j - 1] == self.cells[i][j] == self.cells[i + 1][j + 1] == symb: #главная диагональ
                        return True
                    if self.cells[i + 1][j - 1] == self.cells[i][j] == self.cells[i - 1][j + 1] == symb: #обратная диагональ
                        return True
        return False

class Player:
    def __init__(self, symbol):
        self.symb = symbol

    def coordinates(self, other):
        board.print()
        x, y = map(int, input('Куда вы бы хотели сходить? \n').split())
        while not other.check(x - 1, y - 1):
            print('Данная клетка занята...')
            x, y = map(int, input('Куда вы бы хотели сходить? \n').split())
        else:
            return (x - 1, y - 1)

class Bot(Player):
    def __init__(self, symbol):
        self.symb = symbol

    def choose(self, other):
        x = randint(0, other.width - 1)
        y = randint(0, other.height - 1)
        while not other.check(x, y):
            print('Бот думает...')
            x = randint(0, other.width - 1)
            y = randint(0, other.height - 1)
        else:
            return (x, y)

if __name__ == "__main__":
    symbol = input('Выберите знак, которым будете играть: \n')
    while symbol == ' ' or len(symbol) != 1:
        print('Символ должен быть длиной в один знак...')
        symbol = input('Выберите знак, которым будете играть: \n')

    width, height = map(int, input('Назовите размерность поля: (Квадратное) \n').split())
    while width < 3 or height < 3:
        print('Минимальный размер поля - 3X3')
        width, height = map(int, input('Назовите размерность поля: (Квадратное) \n').split())
    
    board = Board(height, width)
    player = Player(symbol)

    if symbol != 'X':
        symbol1 = 'X'
    else:
        symbol1 = 'O'

    bot = Bot(symbol1)

    win = False
    actions = 0
    max_actions = height * width
    winner = 'Никто'
    while not win:
        location_1 = player.coordinates(board)
        board.put(location_1[0], location_1[1], player.symb)
        
        actions += 1
        if actions == max_actions:
            break

        if board.checker(player.symb):
           winner = 'player'
           break

        location_2 = bot.choose(board)
        board.put(location_2[0], location_2[1], bot.symb)

        actions += 1
        if actions == max_actions:
            break

        if board.checker(bot.symb):
           winner = 'bot'
           break
    
    board.print()
    print(f'Победитель: {winner}')
