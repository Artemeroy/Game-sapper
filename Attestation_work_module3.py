import random

class Cell:
    def __init__(self, mine=False):
        self.mine = mine
        self.rev = False
        self.adjacent = 0

    def reveal(self):
        self.rev = True

    def set_a_m(self, count):
        self.adjacent = count

    def __str__(self):
        if self.rev:  # Если клетка открыта
            if self.mine:  # Если в клетке есть мина
                return "*"  # Возвращаем символ мины
            else:  # Если в клетке нет мины
                return str(self.adjacent) if self.adjacent > 0 else "0"  # Возвращаем количество соседних мин или "0", если по соседству мин нет
        else:  # Если клетка не открыта
            return "#"  # Возвращаем символ закрытой клетки

class Game:
    def __init__(self, wid, hei, mine_n):  # Принимает ширину, высоту и количество мин
        self.wid = wid  # Ширина игрового поля
        self.hei = hei  # Высота игрового поля
        self.mine_n = mine_n  # Количество мин
        self.grid = [[Cell() for b in range(wid)] for _ in range(hei)]  # Двумерный массив клеток для игрового поля
        self.mine_p()  # Размещение мин на поле
        self.calc_a_m()  # Вычисление количества соседних мин для каждой клетки

    def mine_p(self):
        pos = random.sample(range(self.wid * self.hei), self.mine_n)  # Генерация случайных позиций для мин
        for p in pos:
            r = p // self.wid  # Вычисление номера строки для текущей позиции
            c = p % self.wid # Вычисление номера столбца для текущей позиции
            self.grid[r][c].mine = True  # Установка мины в текущей клетке

    def calc_a_m(self):  # Метод для вычисления количества соседних мин для каждой клетки
        for r in range(self.hei):
            for c in range(self.wid):
                if not self.grid[r][c].mine:  # Если в текущей клетке нет мины
                    count = 0
                    for dr in [-1, 0, 1]:
                        for dc in [-1, 0, 1]:
                            if 0 <= r + dr < self.hei and 0 <= c + dc < self.wid:  # Если соседняя клетка находится в пределах игрового поля
                                count += self.grid[r + dr][c + dc].mine  # Увеличиваем счетчик
                    self.grid[r][c].set_a_m(count)  # Устанавливаем количество соседних мин для текущей клетки

    def reveal_c(self, r, c):  # Метод для открытия клетки
        if 0 <= r < self.hei and 0 <= c < self.wid:  # Если указанные координаты находятся в пределах игрового поля
            cell = self.grid[r][c]
            if not cell.rev:  # Если клетка еще не открыта
                cell.reveal()  # Открываем клетку
                return True  # Возвращаем True, обозначая успешное открытие клетки
        return False  # Возвращаем False, если указанные координаты находятся за пределами игрового поля или клетка уже была открыта

    def __str__(self):  # Метод для представления объекта Game в виде строки
        return "\n".join(" ".join(str(self.grid[r][c]) for c in range(self.wid)) for r in range(self.hei))  # Составление строки, представляющей текущее состояние игрового поля

def play_game():
    wid = 3  # Ширина игрового поля
    hei = 3  # Высота игрового поля
    mine_num = 1  # Количество мин на игровом поле
    game = Game(wid, hei, mine_num)
    print(game)

    while True:
        r = int(input("Введите номер строки, начиная с 0: "))  # Ввод номера строки
        c = int(input("Введите номер столбца, начиная с 0: "))  # Ввод номера столбца
        if not game.reveal_c(r, c):  # Если не удалось открыть клетку
            print("Неверная операция.")
        else:
            print(game)  # Вывод обновленного состояния игрового поля
            if game.grid[r][c].mine:  # Если открытая клетка содержит мину
                print("Вы подорвались на мине :(")  # Вывод сообщения о поражении
                break  # Выход из цикла

play_game()