
def welcome():                                     # Приветствие
    print("КРЕСТИКИ-НОЛИКИ")
    print("-------------------")
    print(" Формат ввода: X и Y (через пробел) ")
    print(" X - номер строки  ")
    print(" Y - номер столбца ")


def playground():                                   # Визуалиция игрового поля в командной строке
    print()
    print("    | 0 | 1 | 2 | ")
    print("  --------------- ")
    for i, row in enumerate(field):
        row_str = f"  {i} | {' | '.join(row)} | "
        print(row_str)
        print("  --------------- ")
    print()

def turn():                                          # Запрашиваем у пользователя данные для хода крестиком или ноликом
    while True:
        coord = input("         Ваш ход: ").split()

        if len(coord) != 2:
            print(" Введите 2 координаты! ")
            continue

        x, y = coord

        if not (x.isdigit()) or not (y.isdigit()):
            print(" Введите числа! ")
            continue

        x, y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2:
            print(" Координаты вне диапазона! ")
            continue

        if field[x][y] != " ":
            print(" Клетка занята! ")
            continue

        return x, y

def winner():                                                                                 # Определяем победителя игры
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for coord in win_cord:
        symbols = []
        for c in coord:
            symbols.append(field[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print("Выиграл 'КРЕСТИК'!!!")
            return True
        if symbols == ["0", "0", "0"]:
            print("Выиграл 'НОЛИК'!!!")
            return True
    return False


welcome()
field = [[" "] * 3 for i in range(3)]
count = 0
while True:
    count += 1
    playground()
    if count % 2 == 1:
        print(" Ходит крестик!")
    else:
        print(" Ходит нолик!")

    x, y = turn()

    if count % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "0"

    if winner():
        break

    if count == 9:
        print(" Ничья!")
        break