""" Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

Пример:

- пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4) """

def ListOfProduct(num):
    sum = 1
    list = []
    for i in range (2, num+2):
        list.append(sum)
        sum *= i
    return list

number = input('Введите число: ')

try:
    number = int(number)
    print(ListOfProduct(number))
except:
    print('Введите целое число!')

