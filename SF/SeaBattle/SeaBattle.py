class GameDesk():
    descript = 'игровое поле'
    ls = []

    def __init__(self, desc):
        self.descript = desc
        print(self.descript)
        self.ls = [[0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0]]
        print(*self.ls, sep='\n')


class Ship():
    coord_start = (0, 0)
    direction = 'horizontal'
    def __init__(self):
        print('ввести координату первой клетки коробля, его длинну и направление')

    def



