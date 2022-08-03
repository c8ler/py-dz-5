# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл,
# содержащий сумму многочленов. Это не просто сумма всех коэффициентов.
# Сумма многочленов равна многочлену, членами которого являются все члены данных многочленов.
# например, в 1 файле было 3*x^3 + 5*x^2+10*x+11, в другом 7*x^2+55
# то в итоге будет, 3*x^3 + 12*x^2+10*x+66

def NewPoly(poly):
    degree = len(poly)
    for i in range(len(poly)-2):
        print(f"{poly[i]}*x^{degree} +", end=" ")
        degree -= 1
    print(f"{poly[-2]}*x +", end=" ")
    print(poly[-1])


with open('file1.txt') as f:
    file1 = f.read().replace(' ', '').split('+')
with open('file2.txt') as f:
    file2 = f.read().replace(' ', '').split('+')

sum_of_poly = []
term1 = int(file1[-1]) + int(file2[-1])
term2 = int(file1[-2].replace('*x', '')) + int(file2[-2].replace('*x', ''))
term3 = int(file1[-3].replace('*x^2', '')) + int(file2[-3].replace('*x^2', ''))
term4 = int(file1[-4].replace('*x^3', '')) + int(file2[-4].replace('*x^3', ''))
term5 = int(file1[-5].replace('*x^4', '')) + int(file2[-5].replace('*x^4', ''))
term5 = int(file1[-6].replace('*x^5', '')) + int(file2[-6].replace('*x^5', ''))
sum_of_poly.append(term1)
sum_of_poly.append(term2)
sum_of_poly.append(term3)
sum_of_poly.append(term4)
sum_of_poly.append(term5)

NewPoly(sum_of_poly)


# def SumOfPoly (poly1, poly2):
#     sum_of_poly = []
#     term1 = int(file1[-1]) + int(file2[-1])
#     sum_of_poly.append(term1)
#     term2 = int(file1[-2].replace('*x', '')) + int(file2[-2].replace('*x', ''))
#     sum_of_poly.append(term2)
#     for i in range (-3, len(poly1)*-1, -1):
#         sum_of_poly.append(int(poly1[-i].replace('*x^{i}', '')) + int(poly2[-i].replace('*x^{i}', '')))
#     return sum_of_poly
# print(SumOfPoly(file1, file2))
