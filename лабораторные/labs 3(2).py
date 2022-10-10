print(' #2 задание, берет массив, выводит количество равное нулю')

numbers = []

for i in range(1, 11):

    for i in input('Введите число ').split():
        numbers.append(int(i))
        num_of_0 = numbers.count(0)

print(num_of_0)