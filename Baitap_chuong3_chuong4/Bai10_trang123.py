def xoa_chuoi_b_khoi_chuoi_a():
    """
    Hàm xóa tất cả các lần xuất hiện của chuỗi b trong chuỗi a mà không dùng replace().
    """
    # 1. Nhập liệu từ người dùng
    chuoi_a = input("Nhập Chuỗi A (chuỗi chính): ")
    chuoi_b = input("Nhập Chuỗi B (chuỗi con cần xóa): ")
    # 2. Xử lý các trường hợp đặc biệt
    if not chuoi_b:
        print("\nChuỗi B rỗng. Kết quả Chuỗi A: " + chuoi_a)
        return
    if not chuoi_a:
        print("\nChuỗi A rỗng. Không có gì để xóa.")
        return
    # 3. Khởi tạo biến
    chuoi_a_moi = ""
    i = 0  # Biến chỉ số để duyệt qua chuỗi a
    len_a = len(chuoi_a)
    len_b = len(chuoi_b)
    # 4. Vòng lặp duyệt và xóa
    while i < len_a:
        # Kiểm tra xem chuỗi con b có khớp tại vị trí i của chuỗi a không
        # Cắt chuỗi a từ vị trí i với độ dài bằng độ dài chuỗi b: chuoi_a[i : i + len_b]
        if chuoi_a[i: i + len_b] == chuoi_b:
            # Nếu KHỚP, chúng ta bỏ qua các ký tự của chuỗi b
            i += len_b
        else:
            # Nếu KHÔNG KHỚP, giữ lại ký tự tại vị trí i và chuyển sang ký tự tiếp theo
            chuoi_a_moi += chuoi_a[i]
            i += 1
    # 5. In kết quả
    print("\n" + "=" * 50)
    print("KẾT QUẢ XỬ LÝ CHUỖI")
    print("=" * 50)
    print(f"Chuỗi A ban đầu: '{chuoi_a}'")
    print(f"Chuỗi B (cần xóa): '{chuoi_b}'")
    print(f"Chuỗi A sau khi xóa: **'{chuoi_a_moi}'**")
    print("=" * 50)
# Chạy hàm để thử nghiệm Bài 10
xoa_chuoi_b_khoi_chuoi_a()