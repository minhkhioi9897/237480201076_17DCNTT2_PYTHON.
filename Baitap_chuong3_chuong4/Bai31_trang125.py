def tim_key_voi_gia_tri_lon_nhat():
    """
    Tìm và trả về key có giá trị (value) lớn nhất trong dictionary.
    Giả định tất cả values là số nguyên.
    """
    # 1. Tạo dictionary mẫu để thử nghiệm (hoặc bạn có thể tự nhập)
    # Ví dụ mẫu: Tên sản phẩm/người : Điểm số/Giá trị
    du_lieu_dict = {
        "Alice": 85,
        "Bob": 92,
        "Charlie": 78,
        "David": 95,
        "Eve": 92
    }
    print("--- Dictionary đang kiểm tra ---")
    print(du_lieu_dict)

    if not du_lieu_dict:
        print("Lỗi: Dictionary rỗng.")
        return None
    # 2. Khởi tạo
    # Lấy key và value của phần tử đầu tiên làm giá trị ban đầu
    key_lon_nhat = list(du_lieu_dict.keys())[0]
    gia_tri_lon_nhat = du_lieu_dict[key_lon_nhat]
    # 3. Duyệt qua dictionary
    for key, value in du_lieu_dict.items():
        if value > gia_tri_lon_nhat:
            gia_tri_lon_nhat = value
            key_lon_nhat = key
    # 4. In kết quả
    print("\n" + "=" * 50)
    print("KẾT QUẢ TÌM KIẾM")
    print("=" * 50)
    print(f"Giá trị (value) lớn nhất được tìm thấy là: **{gia_tri_lon_nhat}**")
    print(f"Key tương ứng với giá trị lớn nhất đó là: **'{key_lon_nhat}'**")
    print("=" * 50)
    return key_lon_nhat
# Chạy hàm để thử nghiệm Bài 31
tim_key_voi_gia_tri_lon_nhat()