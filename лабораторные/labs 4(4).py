a = {1: 'Левая палочка твикс', 2: 'Правая палочка твикс' }
key = int(input('Набери 1 или 2 и узнай на чьей стороне ты'))
def get_value(dictionary):
    value = dictionary.get(key)
    print(value)
get_value(a)