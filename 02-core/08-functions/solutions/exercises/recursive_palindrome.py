def palindrome(word):
    if word == '':
        return True
    if word[0] != word[-1]:
        return False
    return palindrome(word[1:-1])


print(palindrome('arepera'))
