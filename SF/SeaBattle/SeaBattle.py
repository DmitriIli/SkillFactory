class GameDesk:
    description = 'игровое поле'
    __pole = []

    def __init__(self, desc):
        self.description = desc
        print(self.description)
        self.__pole = [[0 for j in range(6)] for i in range(6)]

    def print_pole(self):
        count = 1
        print(' ', *(1, 2, 3, 4, 5, 6), sep='|')
        for line in self.__pole:
            print(count, *line, sep='|')
            count += 1
    # def add_ship(self, ):


class Ship:
    __coord_start = (0, 0)
    __length = 0

    def __init__(self, c_value, l_value):
        self.__coord_start = c_value
        self.__length = l_value

    @property
    def coord_start(self):
        return self.__coord_start

    @coord_start.setter
    def coord_start(self, value):
        self.__coord_start = value

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, value):
        self.__length = value


class Player:
    name = ''
    list_of_move = []
    desk = []

    def __init__(self, name):
        self.name = name
        self.desk = GameDesk(self.name)

    def make_move(self):
        while 1:
            print('ввести координаты (x,y) от 1 до 6 через пробел: ')
            try:
                coor_input = input().split()[:2]
            except


player1 = Player('игрок')
player1.desk.print_pole()
