n = int(input("Nhập số nguyên dương n: "))

dem = 0
tam = n
while tam > 0:
    tam //= 10
    dem += 1

print(f"Số {n} có {dem} chữ số.")
