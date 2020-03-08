sentence = 'Ella te da detalle'

sentence = sentence.lower().replace(' ', '')

if sentence == sentence[::-1]:
    print('Yeah! Palindrome')
else:
    print("It's not a palindrome")
