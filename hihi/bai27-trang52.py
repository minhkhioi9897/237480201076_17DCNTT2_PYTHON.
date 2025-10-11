# Nhập số m từ người dùng
try:
    m = float(input("Nhập vào số m: "))

    S = 0.0
    n = 0

    # Lặp cho đến khi tổng S > m
    while S <= m:
        n += 1
        S += 1 / n

    print(f"Số n nguyên dương nhỏ nhất để tổng lớn hơn {m} là: {n}")
    print(f"Tại n = {n}, tổng S = {S:.4f}")  # Làm tròn tổng đến 4 chữ số thập phân

except ValueError:
    print("Vui lòng nhập một số hợp lệ.")