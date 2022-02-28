def new_game():
    return [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]


def print_game_pole(game_pole):
    count = 0
    print(' ', *[1, 2, 3])
    for line in game_pole:
        count += 1
        print(count, *line, end='\n')


def make_move():
    while True:
        print('Make your move. X or O:')
        print('X coordinate:1,2,3')
        x = int(input().split()[:1][0])
        print('Y coordinate:1,2,3')
        y = int(input().split()[:1][0])
        move = [x, y]

        if x in (1, 2, 3) and y in (1, 2, 3) and is_available(move):
            break
        else:
            print('Non correct input')

    return move


def is_available(move):
    if str(game_pole[move[1] - 1][move[0] - 1]) == '-':
        return True
    else:
        return False


def append_move(move, sign):
    game_pole[move[1] - 1][move[0] - 1] = sign
    if game_pole[move[1] - 1][move[0] - 1] == game_pole[move[1] - 2][move[0] - 2] \
            == game_pole[move[1] - 3][move[0] - 3]:
        return 'win'
    if game_pole[move[1] - 1][move[0] - 1] == game_pole[move[1] - 1][move[0] - 2] \
            == game_pole[move[1] - 1][move[0] - 3]:
        return 'win'
    if game_pole[move[1] - 1][move[0] - 1] == game_pole[move[1] - 2][move[0] - 1] \
            == game_pole[move[1] - 3][move[0] - 1]:
        return 'win'


print('Start new game: Y/N?')
if input().upper() == 'Y':
    game_pole = new_game()
    print_game_pole(game_pole)
    flag = 1
else:
    print('end')
    flag = 0

while flag:
    X_move = make_move()
    append_move(X_move, 'x')
    print_game_pole(game_pole)
    O_move = make_move()
    append_move(O_move, 'o')
    print_game_pole(game_pole)
