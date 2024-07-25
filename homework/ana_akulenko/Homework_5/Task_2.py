result = 'результат операции: 42 результат операции: 514 результат работы программы: 9'

result_list = result.split()

print(result_list)

print(result_list.index('операции:'))

print(result_list.index('работы'))

print(len(result_list))

print(int(result_list[2]) + 10)

print(int(result_list[5]) + 10)

print(int(result_list[-1]) + 10)
