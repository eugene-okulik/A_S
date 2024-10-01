words = {'I': 3, 'love': 5, 'Python': 1, '!': 50}


def wow(key):
    res = ''
    value = words[key]
    res = key * value
    print(res)


wow('I')
wow('love')
wow('Python')
wow('!')
