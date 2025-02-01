def larg(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

largest = larg(a, b)
print("The largest number is:", largest)
