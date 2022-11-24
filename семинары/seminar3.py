def line(x):
    global argument1
    argument1 = 3+5
    y = 2 + 3*x
    return y

argument1 = int(input('Введите икс\n'))
print(line(argument1))
print(argument1)