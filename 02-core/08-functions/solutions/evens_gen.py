def my_evens_gen():
    '''Generator for even numbers'''
    i = 0
    for _ in range(0, 100):
        i += 2
        yield i


gen = my_evens_gen()
for even_number in gen:
    print(even_number)
