result_1 = 'результат операции: 42'

result_2 = 'результат операции: 514'

result_3 = 'результат работы программы: 9'

idx1 = result_1.index(': ')

idx2 = result_2.index(': ')

idx3 = result_3.index(': ')

print(int(result_1[idx1 + 1:]) + 10)

print(int(result_2[idx2 + 1:]) + 10)

print(int(result_3[idx3 + 1:]) + 10)
