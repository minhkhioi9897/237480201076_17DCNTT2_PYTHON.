n = int(input("Nhập số nguyên dương n: "))

chan = 0
le = 0
tam = n

while tam > 0:
    cs = tam % 10
    if cs % 2 == 0:
        chan += 1
    else:
        le += 1
    tam //= 10

print(f"Số {n} có {chan} chữ số chẵn và {le} chữ số lẻ.")
