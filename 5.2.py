class Point:
    def __init__(self, x, y): # задаем xy
        self._x = x
        self._y = y 

    def set_x(self, n): # работа с x
        self._x = n  

    def set_y(self, z): # работа с y
        self._y = z  

    def get_info(self):
        return [self._x, self._y]

# подпрограмма выбора пользователем действий 
def workxy(x, y): 
    P = Point(x, y)
    # вывод значений на экран
    print("Значение x,y: " + str(P.get_info()))
    while True:
    	# выбор операции
        quest = input('Какую операцию желаете провести?\n'
                      '1. Изменить x;\n'
                      '2. Изменить y;\n'
                      '3. Изменить x и y;\n'
                      '4. Уменьшить x.\n'
                      '5. Увеличить x;\n'
                      '6. Уменьшить y;\n'
                      '7. Увеличить y;\n'
                      '8. Показать x,y;\n'
                      '9. Закончить работу\n'
                       '(укажите цифру операции): ')
        # действия с x y :
        if quest == '1':
            x = int(input('Укажите новый x: '))
            P.set_x(x)
        elif quest == '2':
            y = int(input('Укажите новый y: '))
            P.set_y(y)
        elif quest == '3':
            x = int(input('Укажите новый x: '))
            y = int(input('Укажите новый y: '))
            P.set_x(x)
            P.set_y(y)
        elif quest == '4':
            newx = int(input('На сколько уменьшить x?: '))
            x -= newx
            P.set_x(x)
        elif quest == '5':
            newx = int(input('На сколько увеличить x?: '))
            x += newx
            P.set_x(x)
        elif quest == '6':
            newy = int(input('На сколько уменьшить y?: '))
            y -= newy
            P.set_y(y)
        elif quest == '7':
            newy = int(input('На сколько увеличить y?: '))
            y += newy
            P.set_y(y)
        elif quest == '8':
            print(P.get_info())
        elif quest == '9':
            break
        else:
            print('Неверный выбор операции')

mes1 = int(input('Введите значение x: ')) # задаем x
mes2 = int(input('Введите значение y: ')) # задаем y
 
workxy(mes1, mes2) 
 