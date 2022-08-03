""" Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

Пример:

- 6782 -> 23
- 0,56 -> 11 """


def SumOfDigit(str):
    digit = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    sum = 0
    for i in range(0, len(str)):
        if str[i] in digit:
            sum += int(str[i])
    return sum


input = input("Введите число: ")
print(SumOfDigit(input))
