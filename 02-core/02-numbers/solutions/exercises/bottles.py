SMALL_REFUND = 0.10
LARGE_REFUND = 0.25

num_small_bottles = int(input('Number of 1 litter or less bottles: '))
num_large_bottles = int(input('Number of more that 1 litter bottles: '))

total_refund = (SMALL_REFUND * num_small_bottles +
                LARGE_REFUND * num_large_bottles)

print('Total refund:', total_refund, '€')
