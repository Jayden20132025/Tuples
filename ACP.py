# Define the tuples
tup1 = (4, 3, 2, 2, -1, 18)
tup2 = (2, 4, 8, 8, 3, 2, 9)

# Function to calculate product of numbers in a tuple
def calculate_product(tup):
    product = 1
    for num in tup:
        product *= num
    return product

# Calculate and print results
print("Product of tup1:", calculate_product(tup1))
print("Product of tup2:", calculate_product(tup2))
