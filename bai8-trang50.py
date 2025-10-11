n = int(input("Nhập số nguyên có 4 chữ số: "))
if (1000 <= n <= 9999):
    tong = 0
    so = n
    while so > 0:
        tong += so % 10
        so //= 10
    print(f"Tổng các chữ số của {n} là: {tong}")
else:
    print("Vui lòng nhập số có đúng 4 chữ số!")
