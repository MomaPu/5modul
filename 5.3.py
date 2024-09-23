from random import randint

class Voin:
    def __init__(self):  # инициализация показателей
        self.health = 100
        self.armory = 100
        self.stamina = 100

    def Damage_with_armory(self):  # первый удар по броне
        if self.armory > 0:
            if self.stamina > 0:
                damage = randint(0, 20)
                self.health -= damage
                self.armory -= randint(0, 10)
            else:
                damage = randint(0, 10)
                self.health -= damage
                self.armory -= randint(0, 10)
        else:
            if self.stamina > 0:
                self.health -= randint(10, 30)
            else: 
                self.health -= randint(0, 10)

    def Clear_damage(self):  # второй удар друг по другу
        if self.stamina > 0:
            self.health -= randint(10, 30)
        else: 
            self.health -= randint(0, 10)

    def Tired(self):
        self.stamina -= 10

first_warrior = Voin()
second_warrior = Voin()

while True: 
    # Пока здоровье > 0 бьемся
    while first_warrior.health > 0 and second_warrior.health > 0:
        attack_one = randint(1, 2)  # случайный выбор атаки или защиты
        attack_two = randint(1, 2)

        if attack_one == 2 and attack_two == 2:
            print('Оба воина пошли в атаку')
            first_warrior.Clear_damage()
            first_warrior.Tired()
            print('Здоровье 1 воина: ' + str(first_warrior.health))
            second_warrior.Clear_damage()
            second_warrior.Tired()
            print('Здоровье 2 воина: ' + str(second_warrior.health))
        elif attack_one == 2 and attack_two == 1:
            print('Первый воин пошел в атаку')
            first_warrior.Damage_with_armory()
            first_warrior.Tired()
            print('Здоровье 2 воина: ' + str(second_warrior.health))
        elif attack_one == 1 and attack_two == 2:
            print('Второй воин пошел в атаку')
            second_warrior.Damage_with_armory()
            second_warrior.Tired()
            print('Здоровье 1 воина: ' + str(first_warrior.health))

        # Проверка здоровья после каждого раунда атаки
        if first_warrior.health <= 0 or second_warrior.health <= 0:
            break

    if first_warrior.health <= 0 and second_warrior.health <= 0:
        print('Патовая ситуация, воины без сил сражаться далее')
        break
    # Проверка состояния первого воина
    if first_warrior.health <= 0:
        mes = input("Убить ли первого воина? (1 - Палец вверх, 2 - Палец вниз): ")
        if mes == '1':
            print('Воин остается в живых')
        elif mes == '2':
            print('Воин убит')
        else:
            print('Вас не поняли, воин убит')
        break

    # Проверка состояния второго воина
    if second_warrior.health <= 0:
        mes = input("Убить ли второго воина? (1 - Палец вверх, 2 - Палец вниз): ")
        if mes == '1':
            print('Воин остается в живых')
        elif mes == '2':
            print('Воин убит')
        else:
            print('Вас не поняли, воин убит')
        break
