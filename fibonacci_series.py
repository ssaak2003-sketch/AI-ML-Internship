terms = int(input("Enter the number of terms: "))

a = 0
b = 1

print("\nFibonacci Series:")

for i in range(terms):
    print(a, end=" ")
    next_term = a + b
    a = b
    b = next_term