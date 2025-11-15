import math
# --- PHẦN 1: CÁC HÀM KIỂM TRA SỐ HỌC (Arithmetic Check Functions) ---
def kiem_tra_so_chan(n):
    """Kiểm tra xem số n có phải là số chẵn không."""
    return n % 2 == 0
def kiem_tra_so_hoan_hao(n):
    """Kiểm tra xem số n có phải là số hoàn hảo không."""
    if n <= 1:
        return False
    # Tính tổng các ước số thật (từ 1 đến n/2)
    tong_uoc = 0
    for i in range(1, int(n / 2) + 1):
        if n % i == 0:
            tong_uoc += i
    return tong_uoc == n
def kiem_tra_so_nguyen_to(n):
    """Kiểm tra xem số n có phải là số nguyên tố không."""
    if n <= 1:
        return False
    # Chỉ cần kiểm tra từ 2 đến căn bậc hai của n
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
def kiem_tra_so_chinh_phuong(n):
    """Kiểm tra xem số n có phải là số chính phương không."""
    if n < 0:
        return False
    # Tính căn bậc hai và kiểm tra xem có phải là số nguyên không
    can_bac_hai = int(math.sqrt(n))
    return can_bac_hai * can_bac_hai == n
# --- PHẦN 2: CÁC HÀM TÍNH TOÁN (Calculation Functions) ---
def tim_ucln(a, b):
    """Tìm ước chung lớn nhất (GCD) của hai số a và b bằng thuật toán Euclid."""
    # Đảm bảo làm việc với giá trị tuyệt đối
    a = abs(a)
    b = abs(b)

    while b:
        # Cấu trúc hoán đổi: a mới là b cũ, b mới là phần dư của a cũ chia b cũ
        a, b = b, a % b
    return a


def tim_bcnn(a, b):
    """Tìm bội chung nhỏ nhất (LCM) của hai số a và b."""
    if a == 0 or b == 0:
        return 0
    # Công thức: BCNN(a, b) = (|a * b|) / ƯCLN(a, b)
    ucln = tim_ucln(a, b)
    bcnn = abs(a * b) // ucln
    return bcnn
def kiem_tra_nguyen_to_cung_nhau(a, b):
    """Kiểm tra xem hai số a và b có nguyên tố cùng nhau không (ƯCLN = 1)."""
    return tim_ucln(a, b) == 1
# --- PHẦN 3: GIAO DIỆN NHẬP LIỆU VÀ KẾT QUẢ ---
def thuc_hien_bai_10():
    """Chạy chương trình chính, nhận input và hiển thị kết quả đầy đủ."""
    # --- Nhập số cho các phép kiểm tra (số đơn) ---
    try:
        so_can_kiem_tra = int(input("Nhập MỘT số nguyên N để kiểm tra: "))
    except ValueError:
        print("Lỗi: Vui lòng nhập số nguyên hợp lệ.")
        return
    print("\n" + "=" * 50)
    print(f"--- KẾT QUẢ KIỂM TRA SỐ N = {so_can_kiem_tra} ---")
    print("=" * 50)
    # Hiển thị kết quả kiểm tra
    print(f"1. Kiểm tra số chẵn: **{kiem_tra_so_chan(so_can_kiem_tra)}**")
    print(f"2. Kiểm tra số hoàn hảo: **{kiem_tra_so_hoan_hao(so_can_kiem_tra)}**")
    print(f"3. Kiểm tra số nguyên tố: **{kiem_tra_so_nguyen_to(so_can_kiem_tra)}**")
    print(f"4. Kiểm tra số chính phương: **{kiem_tra_so_chinh_phuong(so_can_kiem_tra)}**")
    # --- Nhập hai số cho các phép tính (hai số) ---
    try:
        a = int(input("\nNhập số nguyên thứ nhất A: "))
        b = int(input("Nhập số nguyên thứ hai B: "))
    except ValueError:
        print("Lỗi: Vui lòng nhập số nguyên hợp lệ.")
        return
    print("\n" + "=" * 50)
    print(f"--- KẾT QUẢ TÍNH TOÁN CHO HAI SỐ A={a} VÀ B={b} ---")
    print("=" * 50)
    # Hiển thị kết quả tính toán và kiểm tra quan hệ
    ucln_ket_qua = tim_ucln(a, b)
    bcnn_ket_qua = tim_bcnn(a, b)
    print(f"5. Tìm ƯCLN({a}, {b}): **{ucln_ket_qua}**")
    print(f"6. Tìm BCNN({a}, {b}): **{bcnn_ket_qua}**")
    print(f"7. Kiểm tra hai số có nguyên tố cùng nhau (ƯCLN=1): **{ucln_ket_qua == 1}**")
# Chạy chương trình
if __name__ == "__main__":
    thuc_hien_bai_10() #thuc hien cái name chính