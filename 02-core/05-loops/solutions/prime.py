n = 11

for i in range(n // 2, 1, -1):
    if n % i == 0:
        print(i)
        print("It's not prime")
        break
else:
    print('Yeah! We have a prime number')
