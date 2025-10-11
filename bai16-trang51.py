print("Các số chẵn chia hết cho 3 nhỏ hơn 50 là:")
for i in range(2, 50, 2):  # duyệt các số chẵn
    if i % 3 == 0:
        print(i, end=" ")
