month = input('Какой сейчас месяц?\n')
year = int(input('Какой сейчас год?'))

if month == 'Январь' or month =='Март' or month =='Май':
    print(31)
elif month == 'Февраль' and (year % 4 == 0 and year % 100 != 0 or year %400 == 0):
    print(29)
elif month == 'Февраль' and not (year % 4 != 0 and year % 100 == 0 or year %400 != 0):
    print(28)
else:
    print(30)