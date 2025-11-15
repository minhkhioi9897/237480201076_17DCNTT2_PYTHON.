def dem_ky_tu_trong_chuoi():
    """
    Nhận input là một chuỗi và đếm số lượng ký tự in hoa, in thường, và ký tự số.
    """
    # 1. Nhập chuỗi từ người dùng
    chuoi_input = input("Nhập một chuỗi bất kỳ: ")
    # 2. Khởi tạo các biến đếm
    dem_in_hoa = 0
    dem_in_thuong = 0
    dem_ky_so = 0
    # 3. Duyệt qua từng ký tự trong chuỗi
    for ky_tu in chuoi_input:
        if ky_tu.isupper():
            # Kiểm tra ký tự in hoa (A-Z)
            dem_in_hoa += 1
        elif ky_tu.islower():
            # Kiểm tra ký tự in thường (a-z)
            dem_in_thuong += 1
        elif ky_tu.isdigit():
            # Kiểm tra ký tự số (0-9)
            dem_ky_so += 1
    # 4. In kết quả
    print("\n" + "=" * 40)
    print(f"KẾT QUẢ ĐẾM KÝ TỰ (Chuỗi: '{chuoi_input}')")
    print("=" * 40)
    print(f"Số lượng ký tự IN HOA: **{dem_in_hoa}**")
    print(f"Số lượng ký tự in thường: **{dem_in_thuong}**")
    print(f"Số lượng ký tự SỐ: **{dem_ky_so}**")
    print(
        f"Số lượng ký tự khác (khoảng trắng, ký hiệu, v.v.): **{len(chuoi_input) - dem_in_hoa - dem_in_thuong - dem_ky_so}**")
# Chạy hàm để thử nghiệm Bài 5
dem_ky_tu_trong_chuoi()#ý nghĩ của hàm if __name__ == "__main__": thực hiện cái name chính