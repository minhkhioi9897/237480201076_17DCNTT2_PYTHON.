print("=== XÉT ĐẬU CHUYÊN ===")

# Nhập điểm từng môn
toan = float(input("Nhập điểm Toán: "))
van = float(input("Nhập điểm Văn: "))
anh = float(input("Nhập điểm Tiếng Anh: "))

# Tính điểm trung bình
dtb = (toan + van + anh) / 3
print(f"Điểm trung bình: {dtb:.2f}")

# Xét điều kiện
if dtb >= 8.5 and toan >= 9 and toan > van and toan > anh:
    print("→ Đậu chuyên Toán.")
elif dtb >= 8.5 and van >= 9 and van >= anh:
    print("→ Đậu chuyên Văn.")
elif dtb >= 8.5 and anh >= 8.0:
    print("→ Đậu chuyên Tiếng Anh.")
elif dtb >= 8.5:
    print("→ Đậu chuyên Tin học.")
else:
    print("→ Không đậu chuyên.")
