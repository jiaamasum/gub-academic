def sums(*args):
    total = 0
    for num in args:
        total += num
    return total

print("Sum of numbers 1, 2, 3, 4, 5 is:", sums(1, 2, 3, 4, 5))


