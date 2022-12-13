import random

TryCount = 0

print("Привет я Акинатор!")
print("В игре тебе неоходимо отгадать число в выбранном диапозоне, но количество попыток ограниченно")
print("Ну... Давай начинать!")



print("Уровень 1, у тебя есть 3 попытки")
level = random.randint(0, 5)
while (True):
    if TryCount > 3:
        print("Похоже ты проиграл, не расстраивайся, у тебя всё получиться!")
        exit(0)
    catch = int(input("Введи число в диапозоне от 0 до 5: "))
    if catch == level:
        print("Молодец ты прошол первый уровень!")
        break
    else:
        TryCount +=1


print("Уровень 2, у тебя есть 3 попытки")
level = random.randint(0, 10)
while (True):
    if TryCount > 3:
        print("Похоже ты проиграл, не расстраивайся, у тебя всё получиться!")
        exit(0)
    catch = int(input("Введи число в диапозоне от 0 до 10: "))
    if catch == level:
        print("Молодец ты прошол первый уровень!")
        break
    else:
        TryCount +=1

print("Уровень 3, у тебя есть 5 попыток")
level = random.randint(0, 20)
while (True):
    if TryCount > 5:
        print("Похоже ты проиграл, не расстраивайся, у тебя всё получиться!")
        exit(0)
    catch = int(input("Введи число в диапозоне от 0 до 20: "))
    if catch == level:
        print("Молодец ты прошол первый уровень!")
        break
    else:
        TryCount +=1
