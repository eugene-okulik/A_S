import sys
import itertools

sys.set_int_max_str_digits(100000)

def fib():
    a = 0
    b = 1
    while True:
        yield b
        a, b = b, a + b

index1, index2, index3, index4 = 5, 200, 1000, 10000

lst = [
    next(itertools.islice(fib(), index1, None)),
    next(itertools.islice(fib(), index2, None)),
    next(itertools.islice(fib(), index3, None)),
    next(itertools.islice(fib(), index4, None))
]

print(lst)
