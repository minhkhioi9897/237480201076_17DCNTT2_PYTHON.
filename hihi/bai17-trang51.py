n = int(input("Nhập số nguyên dương n: "))

tong_le = 0
tong_chan = 0

for i in range(1, n):
    if i % 2 == 0:
        tong_chan += i
    else:
        tong_le += i

print(f"Tổng các số lẻ nhỏ hơn {n}: {tong_le}")
print(f"Tổng các số chẵn nhỏ hơn {n}: {tong_chan}")
