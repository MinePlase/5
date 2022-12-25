from random import randint
count = 0
for i in range(9):
    print("Сделай ход: 1-камень, 2-ножницы, 3-бумага")
    player = int(input("Введите цифру:"))
    if player == 1:
        print("Твой ход - камень!")
    elif player == 2:
        print("Твой ход - ножницы!")
    elif player == 3:
        print("Твой ход - бумага!")
    else:
        print("читайте условия правильно")
    comp = randint(1, 3)
    if comp == 1:
        print("ход компьютера - камень!")
    elif comp == 2:
        print("ход компьютера - ножницы")
    elif comp == 1:
        print("ход компьютера - бумага")
    if player == comp:
        print("ничья! Твои победы:", count)
    elif comp - player == 1 or player - comp == 2:
          count += 1
          print("победа! Твои победы:", count)
    elif player - comp == 1 or comp - player == 2:
          print("поражение! Твои победы:", count)
    if count == 3:
        break
