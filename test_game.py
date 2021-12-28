import random


def monster_f():
    monster_health = random.randint(5, 15)
    monster_power = random.randint(5, 16)
    result = f'Вы встретили чудовище с {monster_health} жизнями и с силой удара {monster_power}.'
    return result, monster_health, monster_power


def apple_f():
    apple_health = random.randint(5, 10)
    result = f'Вы нашли яблоко и съели его, яблоко прибавило {apple_health} к здоровью.'
    return result, apple_health


def sword_f():
    sword_power = random.randint(10, 25)
    result = f'Вы нашли меч с силой атаки {sword_power}.'
    return result, sword_power


def main_f():
    knight_health = 10
    knight_sword = 10
    win_count = 0
    print('Вы рыцарь сказачного королевства, рыцарю нужно убить десять монстров что-бы спасти королевство.\n'
          f'Изначально у рыцаря {knight_health} здоровья и меч с силой удара {knight_sword}.\n'
          'Если у монстра сила атаки больше или равна здоровью рыцаря, рыцарь проиграет.\n'
          'Что-бы победить монстра сила меча рыцаря должна быть больше или равна здоровью монстра.\n')
    print('Введите любой символ для начало игры')
    input()
    while win_count < 10:
        event_id = random.randint(0, 2)
        if event_id == 0:
            monster_txt, monster_health, monster_power = monster_f()
            print(monster_txt)
            action = 0
            while not action:
                action = input('Введите цифру для действия: ' '1 - атаковать монстра. 2 - убежать от монстра.\n'
                               f'Сила атаки мечя рыцаря: {knight_sword}. Здоровье рыцаря: {knight_health}. ')
                if action != str(1) and action != str(2):
                    action = 0
                    print('\nВы ввели не верно значение. Введите 1 или 2.\n')
            if action == str(1):
                if knight_health <= monster_power:
                    print('Монстр Вас победил, Вы проиграли!')
                    break
                else:
                    monster_health = monster_health - knight_sword
                    knight_health = knight_health - monster_power
                    win_count += 1
                    print(f'Вы победили монстра у Вас осталось {knight_health} здоровья.\n'
                          f'Число Ваших побед: {win_count}.')
                    if win_count == 10:
                        print('Поздравляем Вы спасли королевство!')
            if action == str(2):
                print('Вы убежали от монстра.')
        if event_id == 1:
            apple_txt, apple_health = apple_f()
            knight_health = knight_health + apple_health
            print(apple_txt)
            print(f'Здоровье рыцаря равно: {knight_health}')
        if event_id == 2:
            sword_txt, sword_power = sword_f()
            print(sword_txt)
            action = 0
            while not action:
                action = input('Введите цифру для действия: 1 - взять меч. 2 - не брать меч.\n'
                               f'Сила атаки мечя рыцаря: {knight_sword}. ')
                if action != str(1) and action != str(2):
                    action = 0
                    print('\nВы ввели не верно значение. Введите 1 или 2.\n')
            if action == str(1):
                knight_sword = sword_power
                print(f'Вы взяли меч с силой атаки {sword_power}. ')
                print(f'Сила атаки вашего мяча равна: {knight_sword}. ')
            if action == str(2):
                print('Вы прошли мимо мечя.')


if __name__ == "__main__":
    main_f()
