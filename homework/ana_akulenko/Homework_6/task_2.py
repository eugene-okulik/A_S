test_input = range(1, 101)

for value in test_input:

    if value % 3 == 0 and value % 5 == 0:
        print('FuzzBuzz')

    elif value % 3 == 0:
        print('Fuzz')

    elif value % 5 == 0:
        print('Buzz')

    else:
        print(value)
