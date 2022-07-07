import random
import time

print(" Правила игры простые: у тебя и у Ашота есть по пять рандомных предметов."
      "Ашот кидает кубик и твоя задача угадать, какое число выпало на кубике."
      "Если ты угадаешь, какое число выпало - Ашот отдает тебе свой рандомный предмет."
      "Если ты не угадаешь число, отдаешь Ашоту свой рандомный предмет."
      "Игра продолжается до тех пор, пока у тебя или у Ашота не останется предметов.")
print("              - - - - - - - - - - - - - - - -  - - -- - - - - -"
      "               - - - -- - - - - - - - - - - - - - - - - - - - -")
ashot_bags = ['ключ', 'нож', 'зажигалка', 'отвертка', 'старый мобильник']
user_bag = []
current_bags = []
num = 0
while num < 5:
    user_bags = input("Введите название ваших предметов, которые вы ставите на кон: ")
    user_bag.append(user_bags)
    num = num + 1
    if num == 5:
        break
print(user_bag)
start = input("Все предметы ты поставил, готов играть? y/n ?")
active = True
while active == True:
    if start == 'y':
        print('Ашот кидает кубик')
        time.sleep(3)
        print('*Колдует по-ашотовски*')
        time.sleep(3)
        print('кубик упал, какое число?')
        time.sleep(3)
    answer = int(input('Угадайте число, которое выпало на кубике: '))
    coube = random.randint(1,6)
    if answer == coube:
        print('Ай маладес, ай абманул Ашота, будет Ашот с табой теперь внимательней')
        current_bags = ashot_bags.pop()
        user_bag.append(current_bags)
        print("У тебя есть: ", len(user_bag),'предметов: ' , user_bag)
    else:
        print('Слющай, я тебе одну вещь скажу, только ты не обижайся: "Деньги не главное"')
        current_bags = user_bag.pop()
        ashot_bags.append(current_bags)
        print("У тебя есть: ", len(user_bag), 'предметов: ' , user_bag)

    if ashot_bags == [] or user_bag == []:
        active = False
    
    
