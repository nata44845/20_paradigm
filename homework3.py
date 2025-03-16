# Домашнее задание 3. Крестики-нолики

# Вероятнее всего, вы с детства знакомы с этой игрой. Пришло время реализовать её. 
# Два игрока по очереди ставят крестики и нолики на игровое поле. 
# Игра завершается когда кто-то победил, либо наступила ничья, либо игроки отказались играть.
# Задача
# Написать игру в “Крестики-нолики”. Можете использовать любые парадигмы, 
# которые посчитаете наиболее подходящими. Можете реализовать доску как угодно - 
# как одномерный массив или двумерный массив (массив массивов).

# Можете использовать как правила, так и хардкод, на своё усмотрение. 
# Главное, чтобы в игру можно было поиграть через терминал с вашего компьютера.

class GameXO:
    
    # Задаем таблицу сетки
    table = list(range(1,10))

    # Рисуем таблицу сетки
    def table_grid(self):

        for i in range(3):
            print ("|", self.table[0+i*3], "|", self.table[1+i*3], "|",self.table[2+i*3], "|")

    # Сделать ход
    def make_move(self, step):
        valid = False
        while not valid:
            value = int(input("Введите номер клетки куда поставить значение " + step +"? "))
            if value >= 1 and value <= 9:
                if (str(self.table[value-1]) not in "XO"):
                    self.table[value-1] = step
        
                    valid = True
                else:
                    print ("Эта клетка занята")
            else:
                print("Некорректный ввод!")

    # Условия победы
    def winner(self):
        win = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
        for x in win:
            if self.table[x[0]] == self.table[x[1]] == self.table[x[2]]:
                return self.table[x[0]]
        return False

    # Запуск игры
    def play(self):
        count = 0
        win = False
        while not win:
            self.table_grid()
            if count % 2 == 0:
                self.make_move("X")
            else:
                self.make_move("O")
            count += 1
            if count > 4:
                m = self.winner()
                if m:
                    print (m, "Победил!")
                    win = True
                    break
            if count == 9:
                print ("Ничья!")
                break
        self.table_grid()

if __name__ == '__main__':
    game = GameXO()
    game.play()