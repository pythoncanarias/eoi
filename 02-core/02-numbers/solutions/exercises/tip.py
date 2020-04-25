TAX_RATE = 0.07
TIP_RATE = 0.05

meal_cost = float(input('Please input the cost of the meal: '))
tip = TIP_RATE * meal_cost
tax = meal_cost * TAX_RATE
total_cost = meal_cost + tip + tax

print('Raw meal cost: ', meal_cost)
print('Tip:', tip, '€')
print('Tax:', tax, '€')
print('Total cost:', total_cost, '€')
