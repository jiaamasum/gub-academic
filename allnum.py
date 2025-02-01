total = 0
for num in range(50, 101):
    if num % 3 == 0 and num % 5 != 0:
        total += num

print("Sum of numbers divisible by 3 and not divisible by 5 between 50 and 100:", total)