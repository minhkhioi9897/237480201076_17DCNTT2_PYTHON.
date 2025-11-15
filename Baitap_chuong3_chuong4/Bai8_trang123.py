import re
def kiem_tra_do_manh_mat_khau():
    """
    Hàm kiểm tra độ mạnh của mật khẩu theo các tiêu chí và hiển thị hướng dẫn.
    """
    # --- PHẦN 1: HIỂN THỊ MENU/HƯỚNG DẪN ---
    print("=" * 60)
    print("        HỆ THỐNG KIỂM TRA ĐỘ MẠNH MẬT KHẨU")
    print("=" * 60)
    print("Yêu cầu về mật khẩu mạnh:")
    print("1. Độ dài tối thiểu: **Ít nhất 8** ký tự.")
    print("2. Chứa ký tự số: **Ít nhất 1** ký tự số (0-9).")
    print("3. Chứa ký tự in hoa: **Ít nhất 1** ký tự in hoa (A-Z).")
    print("4. Chứa ký tự đặc biệt: **Ít nhất 1** ký tự đặc biệt (!@#$%^&*...).")
    print("-" * 60)
    # 2. Nhập mật khẩu từ người dùng
    mat_khau = input("▶️ Vui lòng nhập mật khẩu cần kiểm tra: ")
    # 3. Khởi tạo biến theo dõi các điều kiện
    manh_hay_khong = True
    danh_sach_loi = []
    # --- PHẦN 2: KIỂM TRA ĐIỀU KIỆN ---
    # 1. Kiểm tra độ dài
    if len(mat_khau) < 8:
        danh_sach_loi.append("❌ Thiếu độ dài (cần ít nhất 8 ký tự).")
        manh_hay_khong = False
    # 3. Kiểm tra ký tự số
    if not any(c.isdigit() for c in mat_khau):
        danh_sach_loi.append("❌ Thiếu ký tự số (cần ít nhất 1 số).")
        manh_hay_khong = False
    # 3. Kiểm tra ký tự in hoa
    if not any(c.isupper() for c in mat_khau):
        danh_sach_loi.append("❌ Thiếu ký tự in hoa (cần ít nhất 1 chữ in hoa).")
        manh_hay_khong = False
    # 4. Kiểm tra ký tự đặc biệt (là ký tự không phải chữ/số)
    co_ky_tu_dac_biet = False
    for char in mat_khau:
        if not char.isalnum():
            co_ky_tu_dac_biet = True
            break
    if not co_ky_tu_dac_biet:
        danh_sach_loi.append("❌ Thiếu ký tự đặc biệt (cần ít nhất 1 ký tự đặc biệt).")
        manh_hay_khong = False
    # --- PHẦN 3: HIỂN THỊ KẾT QUẢ CUỐI CÙNG ---
    print("\n" + "=" * 60)
    print(f"KẾT QUẢ: Mật khẩu đã nhập là **'{mat_khau}'**")
    print("=" * 60)
    if manh_hay_khong:
        print("✅ MẬT KHẨU ĐỦ MẠNH! Đã đạt tất cả các tiêu chí.")
    else:
        print("🔴 MẬT KHẨU CHƯA ĐỦ MẠNH VÌ VI PHẠM CÁC ĐIỀU SAU:")
        for loi in danh_sach_loi:
            print(f"  {loi}")
    print("=" * 60)
# Chạy chương trình
kiem_tra_do_manh_mat_khau() #ý nghĩ của hàm if __name__ == "__main__":thực hiện cai name chính