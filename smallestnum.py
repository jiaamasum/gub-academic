num = list(map(int, input("Input the numbers(1 2 3 4): ").split()))

small = num[0]
for n in num:
    if n < small:
        small = n

print("Small number is:", small)

