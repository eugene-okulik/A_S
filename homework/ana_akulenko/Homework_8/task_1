# solution 1 without a loop:

# from random import randint, choice
# salary = int(input('Whats your salary: '))
# bonus = bool(choice([True, False]))
# bonus_amount = randint(1, 1000)
# count = salary + bonus_amount
#
#
# def test():
#     if bonus is True:
#         print(f'{salary}, {bonus} - ${count}')
#     else:
#         print(f'{salary}, {bonus} - ${salary}')
#
#
# test()


# issues:
# 1. defaults to True - kinda fixed.
# 2. Should continue a loop for salary input - idk, don't see a beautiful solution.
# 3 - incorrect amount calc - kinda fixed

# solution 2 with a loop:

def test():
    from random import randint, choice
    while True:
        salary = int(input('Whats your salary: '))
        bonus = bool(choice([True, False]))
        bonus_amount = randint(1, 1000)
        count = salary + bonus_amount
        if bonus is True:
            print(f'{salary}, {bonus} - ${count}')
        else:
            print(f'{salary}, {bonus} - ${salary}')


test()
