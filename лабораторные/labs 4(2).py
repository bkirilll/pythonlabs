any_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = []
def more(list):
    for i in range(len(list)):
        if list[i] > list[i - 1]:
            result.append(list[i])
    print(result)
more(any_list)