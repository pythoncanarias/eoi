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
    ic()
    first()
    if expression():
        ic()
        second()
    else:
        ic()
        third()

if __name__ == "__main__":
    main()
