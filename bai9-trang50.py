tien = int(input("Nhập số tiền (VNĐ): "))
to_menh_gia = [50000, 20000, 10000, 5000, 2000, 1000]
print("\nSố tờ tiền tương ứng:")
for menh_gia in to_menh_gia:
    so_to = tien // menh_gia
    tien %= menh_gia
    if so_to > 0:
        print(f"{menh_gia:>6,} VNĐ : {so_to} tờ")
