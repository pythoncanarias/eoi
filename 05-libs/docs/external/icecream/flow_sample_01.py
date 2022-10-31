from icecream import ic

def first():
    ...

def second():
    ...

def third():
    ...

def expression():
    return True

def main():
    print(0)
    first()
    if expression():
        print(1)
        second()
    else:
        print(2)
        third()

if __name__ == "__main__":
    main()
