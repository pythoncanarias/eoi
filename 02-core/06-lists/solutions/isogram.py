word = 'six-year-old'

seen_letters = []
for letter in word:
    if letter in seen_letters:
        print('⛔️ No es un isograma!')
        break
    if letter.isalpha():
        seen_letters.append(letter)
else:
    print('✅ Sí es un isograma!')
