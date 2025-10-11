n = int(input("Nhập số nguyên dương n: "))

if n < 2:
    print(f"{n} không phải là số nguyên tố.")
else:
    dem = 0
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            dem += 1
            break
    if dem == 0:
        print(f"{n} là số nguyên tố.")
    else:
        print(f"{n} không phải là số nguyên tố.")
