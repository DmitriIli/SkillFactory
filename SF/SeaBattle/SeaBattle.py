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
    ships = []
    count_cell = 11
    count_3cells = 0
    count_2sells = 0
    count_1cell = 0

    def __init__(self, name):
        self.name = name
        self.desk = GameDesk(self.name)

    def input_value(self):
        while 1:
            print('ввести координаты первой клетки коробля(x,y) от 1 до 6 и размер коробля от 1 до 3. Расстояние между '
                  'короблями должно состоявлять не менее одной клетки: ')
            try:
                print('x: ')
                x = int(input().split()[:1][0])
                print('y: ')
                y = int(input().split()[:1][0])
                print('len: ')
                l = int(input().split()[:1][0])
                if not (x in (1, 2, 3, 4, 5, 6) and y in (1, 2, 3, 4, 5, 6) and l in (1, 2, 3)):
                    raise ValueError

            except ValueError:
                print('некорректный ввод')
            else:
                return x, y, l


player1 = Player('игрок')
player1.desk.print_pole()
move = player1.input_value()
print(type(move), move)
