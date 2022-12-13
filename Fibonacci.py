#   Prolog
#   Author: Avity Ngonyani
#   Email: avity4585@gmail.com
#   Project: Get Fibonacci sequence

def fibonacci():
    f = open('fibonacci.txt', 'w')
    numbers = int(input('Enter the max sequence number you want: '))
    count = -1
    original = 1
    first = 0
    num_list = []
    for i in range(original, numbers+1):
        sequence = original + first
        original = first
        first = sequence
        num_list.append(sequence)
        
    for number in num_list:
        count += 1
        print(count, number)
        print(count, number, file=f)

fibonacci()
