# Дан список чисел. Создайте список, в который попадают числа, описываемые возрастающую последовательность. 
# Порядок элементов менять нельзя.

# Пример:

# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 7]
# [1, 5, 2, 3, 4, 1, 7] => [1, 5]

list_of_numbers = [2, 9, 8, 7, 6, 3, 2, 4, 10, 7, 5, 15, 11, 4]

def FindLst(lst):
    min = lst[0]
    max = lst[0]
    for i in range(1, len(lst)):
        for j in range(1, len(lst)):
            if lst[j] < min:
                min = lst[j]
            elif lst[j] == max + 1:
                max = lst[j]
    lst2 = [min, max]
    return lst2

print(f"{list_of_numbers} => {FindLst(list_of_numbers)}")