# Nhập số nguyên dương n từ người dùng
try:
    n = int(input("Nhập vào số nguyên dương n: "))
    if n <= 1:
        print("n phải lớn hơn 1.")
    else:
        S = 0
        k = 0
        # Vòng lặp sẽ tiếp tục khi tổng S cộng với số tiếp theo (k+1) vẫn nhỏ hơn n
        while S + (k + 1) < n:
            k += 1
            S += k

        print(f"Số k lớn nhất tìm được là: {k}")
        print(f"Khi đó tổng S(k) = 1 + ... + {k} = {S}")

except ValueError:
    print("Vui lòng nhập một số nguyên hợp lệ.")