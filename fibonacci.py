n = int(input("How many Fibonacci numbers need? "))
fib = []

a, b = 0, 1
for _ in range(n):
    fib.append(a)
    a, b = b, a + b

print("Fibonacci series:")
print(fib)
