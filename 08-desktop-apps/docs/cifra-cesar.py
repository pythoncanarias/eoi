

def cifra(s, clave=3):
    buff = []
    for c in s:
        num = ord(c)
        if 65 <= num < 91:
            new_num = ((num - 65 + clave) % 26) + 65
            buff.append(str(chr(new_num)))
        elif 97 <= num < 123:
            new_num = ((num - 97 + clave) % 26) + 97
            buff.append(str(chr(new_num)))
        else:
            buff.append(c)
    return ''.join(buff)

def test():
    assert cifra('Hola, Mundo', 0) == 'Hola, Mundo'
    assert cifra('ABC', 1) == 'BCD'
    assert cifra('ABC', 3) == 'DEF'
    assert cifra('XYZ', 1) == 'YZA'
    assert cifra('XYZ', 2) == 'ZAB'
    assert cifra('XYZ', 3) == 'ABC'
    assert cifra('ABC', -3) == 'XYZ'
    assert cifra('abc', 1) == 'bcd'
    assert cifra('abc', 3) == 'def'
    assert cifra('xyz', 1) == 'yza'
    assert cifra('xyz', 2) == 'zab'
    assert cifra('xyz', 3) == 'abc'
    assert cifra('abc', -3) == 'xyz'

if __name__ == '__main__':
    test()


