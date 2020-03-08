money = 347

change, money = divmod(money, 50)
if change > 0:
    print(change, 'bills of 50€')
if money > 0:
    change, money = divmod(money, 20)
    if change > 0:
        print(change, 'bills of 20€')
    if money > 0:
        change, money = divmod(money, 10)
        if change > 0:
            print(change, 'bills of 10€')
        if money > 0:
            change, money = divmod(money, 5)
            if change > 0:
                print(change, 'bills of 5€')
            if money > 0:
                change, money = divmod(money, 2)
                if change > 0:
                    print(change, 'coins of 2€')
                if money:
                    print(change, 'coins of 1€')
