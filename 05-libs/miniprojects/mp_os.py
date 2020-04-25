    import os

    acc = 0
    for (dirpath, dirnames, filenames) in os.walk('.'):
        for filename in filenames:
            if filename.lower().endswith('.py'):
                fullname = os.path.join(dirpath, filename)
                size = os.path.getsize(fullname) 
                acc += size
                print(fullname, size)
    print('Bytes totales:', acc)

