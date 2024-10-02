number = 4
while True:
    test_input = int(input('введите число: '))
    if test_input != number:
        print('попробуйте снова')
        continue
    else:
        print('Поздравляю! Вы угадали!')
    break
