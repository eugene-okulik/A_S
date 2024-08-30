text = 'Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, facilisis vitae semper at, dignissim vitae libero'

n_text = text.split()

upg_text = []

for word in n_text:
    if ',' in word:
        main_word = word[:-1]
        upg_word = main_word + 'ing,'

    elif '.' in word:
        main_word = word[:-1]
        upg_word = main_word + 'ing.'

    else:
        upg_word = word + 'ing'

    upg_text.append(upg_word)

make_list = ' '.join(upg_text)
print(make_list)
