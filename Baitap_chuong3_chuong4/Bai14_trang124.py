def tim_gia_tri_duong_dau_tien():
    """
    Tìm và trả về giá trị dương đầu tiên trong list.
    Nếu không có, trả về -1.
    """
    try:
        # Nhập list từ người dùng
        input_str = input("Nhập list số nguyên (cách nhau bởi dấu cách): ")
        L = [int(x) for x in input_str.split()]
    except ValueError:
        print("Lỗi: Vui lòng chỉ nhập các số nguyên hợp lệ.")
        return -1
    # Duyệt qua list L
    for so in L:
        if so > 0:
            # Tìm thấy giá trị dương đầu tiên
            print(f"List đã nhập: {L}")
            print(f"Giá trị dương đầu tiên là: **{so}**")
            return so
    # Nếu vòng lặp kết thúc mà không tìm thấy
    print(f"List đã nhập: {L}")
    print("Không tìm thấy giá trị dương nào.")
    return -1
# Chạy hàm để thử nghiệm Bài 14
tim_gia_tri_duong_dau_tien()