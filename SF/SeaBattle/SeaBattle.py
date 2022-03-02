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
    length = 0

    @property
    def coord_start(self):
        return self.coord_start

    @coord_start.setter
    def coord_start(self, value):
        self.coord_start = value

    @property
    def length(self):
        return self.length

    @length.setter
    def length(self, value):
        return self.length
