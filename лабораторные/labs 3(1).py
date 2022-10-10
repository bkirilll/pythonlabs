print('#1 задание, берет массив из 10 чисел и выводит их сумму')

numbers = []

for i in range(1,11):
    
    for i in input('Введите число ').split():
        numbers.append(int(i))
print(numbers)

print(sum(numbers))
