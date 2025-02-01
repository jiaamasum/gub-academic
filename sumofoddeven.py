num = list(map(int, input("Input the numbers(1 2 3 4): ").split()))

odd = 0
even = 0

for n in num:
    if n % 2 == 0:
        even += n
    else:
        odd += n

print("Sum of evens:", even)
print("Sum of odds:", odd)
