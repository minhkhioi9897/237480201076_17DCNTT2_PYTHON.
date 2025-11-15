n = int(input("Nhập số nguyên dương n: "))

if n % 5 == 0 and n % 7 == 0:
    print(f"{n} chia hết cho cả 5 và 7.")
else:
    print(f"{n} không chia hết cho cả 5 và 7.")
