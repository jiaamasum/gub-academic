n = int(input("Enter a non-negative integer: "))

if n < 0:
    print("Factorial can't be find for negative numbers.")
else:
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    print("Factorial of", n, "is:", fact)
