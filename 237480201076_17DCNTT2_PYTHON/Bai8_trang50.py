n: int = int(input("Nhập số nguyên có 4 chữ số: "))
tong = 0
so = n
if(1000 <= n <= 9999):
        print(f"Tổng các chữ số của {n} là: {tong}")
        while so > 0:
            tong += so % 10
            so //= 10
else:
        print("Vui lòng nhập số có đúng 4 chữ số!")
