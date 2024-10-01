result_1 = 'результат операции: 42'

result_2 = 'результат операции: 514'

result_3 = 'результат работы программы: 209'

result_4 = 'результат: 2'


def func2(entr1):
    entr2 = entr1.index(': ')
    return int(entr1[entr2 + 1:]) + 10


print(func2(result_1))
print(func2(result_2))
print(func2(result_3))
print(func2(result_4))
