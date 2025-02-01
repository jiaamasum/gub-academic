num = list(map(int, input("Input the numbers(1 2 3 4): ").split()))

un_num = list(set(num))

if len(un_num) < 2:
    print("Not enough numberrs")
else:
    un_num.sort()
    s_high = un_num[-2]
    print("The second highest number is:", s_high)