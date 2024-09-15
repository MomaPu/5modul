import random # импортируем для случайного выбора
from random import randint

# Задаем воина
class Voin:
    def __init__(self): # иницилизация показателей
        self.health = 100
        self.armory = 100
        self.stamina = 100

    def hit1(self): # первый удар по броне
        if self.armory > 0:
            if self.stamina > 0:
                damage = random.randint(0, 20)
                self.health -= damage
                self.armory -= random.randint(0, 10)
            else:
                damage = random.randint(0, 10)
                self.health -= damage
                self.armory -= random.randint(0, 10)
        else:
            if self.stamina > 0:
                self.health -= random.randint(10, 30)
            else: 
                self.health -= random.randint(0, 10)

    def hit2(self): # второй удар друг по другу
        if self.stamina > 0:
            self.health -= random.randint(10, 30)
        else: 
            self.health -= random.randint(0, 10)

    def tired(self):
        self.stamina -= 10

v1 = Voin()
v2 = Voin()
war = True

while war: 
    at1 = randint(1, 2) # случайный выбор атаки или защиты
    at2 = randint(1, 2)

    while v1.health > 10 and v2.health > 10: # пока здоровье больше 10- бьемся
        if at1 == 2 and at2 == 2:
            print('Оба воина пошли в атаку')
            v1.hit2()
            v1.tired()
            print('Здоровье 1 воина: ' + str(v1.health))
            v2.hit2()
            v2.tired()
            print('Здоровье 2 воина: ' + str(v2.health))
        elif at1 == 2 and at2 == 1:
            print('Первый воин пошел в атаку')
            v1.hit1()
            v1.tired()
            print('Здоровье 2 воина: ' + str(v2.health))
        elif at1 == 1 and at2 == 2:
            print('Второй воин пошел в атаку')
            v2.hit1()
            v2.tired()
            print('Здоровье 1 воина: ' + str(v1.health))

        # Проверка здоровья после каждого раунда атаки
        if v1.health <= 10 or v2.health <= 10:
            break

    # Проверка состояния первого воина
    if v1.health <= 10:
        mes = input("Убить ли первого воина? (1 - Палец вверх, 2 - Палец вниз): ")
        if mes == '1':
            print('Воин остается в живых')
        elif mes == '2':
            print('Воин убит')
            war = False
        else:
            print('Вас не поняли, воин убит')
            war = False

    # Проверка состояния второго воина
    if v2.health <= 10:
        mes = input("Убить ли второго воина? (1 - Палец вверх, 2 - Палец вниз): ")
        if mes == '1':
            print('Воин остается в живых')
        elif mes == '2':
            print('Воин убит')
            war = False
        else:
            print('Вас не поняли, воин убит')
            war = False
