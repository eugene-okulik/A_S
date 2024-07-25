result_1 = 'результат операции: 42'

result_2 = 'результат операции: 514'

result_3 = 'результат работы программы: 9'

print(len(result_1))

print(len(result_2))

print(len(result_3))

print(result_1.index(': '))

print(result_2.index(': '))

print(result_3.index(': '))

print(int(result_1[20:22]) + 10)

print(int(result_2[20:23]) + 10)

print(int(result_3[27:29]) + 10)
