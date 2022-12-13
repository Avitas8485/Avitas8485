#   Prolog
#   Author: Avity Ngonyani
#   Email: avity4585@gmail.com
#   Project: Guessing game
# #


import random
import math
smaller = int(input("Enter the smaller number: "))
larger = int(input("Enter the larger number: "))
comp_guess = random.randint(smaller, larger)
count = 0
max_guess = round(math.log(larger-smaller + 1, 2))
my_num=()
while comp_guess != my_num or count != max_guess:
    count += 1
    my_num = (smaller+larger) // 2
    print("your number is", my_num)
    answer = input("Enter =, < or > : ")
    if answer == '<':
        larger = my_num - 1
    elif answer =='>':
        smaller = my_num + 1
    elif answer == '=':
        print("Ding ding!, in", count, "tries!")
        comp_guess = my_num
    elif count == max_guess:
        print('Im out, you win!')
        count = max_guess