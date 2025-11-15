def tinh_tong_ky_tu_so():
    """
    Nhận input là một chuỗi, tách các ký tự số, sau đó tính tổng của chúng.
    """
    # 1. Nhập chuỗi từ người dùng
    chuoi_input = input("\nNhập một chuỗi chứa chữ và số (ví dụ: aNhd5cC4f7Nde3s1): ")
    # 2. Khởi tạo
    tong_ky_so = 0
    cac_ky_so_tim_thay = []
    # 3. Duyệt và tính tổng
    for ky_tu in chuoi_input:
        if ky_tu.isdigit():
            # Nếu là ký tự số:
            # a) Chuyển ký tự số sang số nguyên (int())
            gia_tri_so = int(ky_tu)
            # b) Cộng vào tổng
            tong_ky_so += gia_tri_so
            # c) Lưu lại ký tự số để hiển thị
            cac_ky_so_tim_thay.append(ky_tu)
    # 4. In kết quả
    print("\n" + "=" * 40)
    print("KẾT QUẢ TÍNH TỔNG KÝ TỰ SỐ")
    print("=" * 40)
    if cac_ky_so_tim_thay:
        print(f"Các ký tự số được tìm thấy: **{', '.join(cac_ky_so_tim_thay)}**")
        print(f"Phép tính: **{' + '.join(cac_ky_so_tim_thay)}**")
        print(f"Tổng của các ký tự số là: **{tong_ky_so}**")
    else:
        print("Không tìm thấy ký tự số nào trong chuỗi đã nhập.")
# Chạy hàm để thử nghiệm Bài 6
tinh_tong_ky_tu_so()#ý nghĩ của hàm if __name__ == "__main__":thực hiện cai name chính