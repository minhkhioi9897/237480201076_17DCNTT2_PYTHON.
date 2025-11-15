def nhap_va_tim_vi_tri_k():
    """
    Yêu cầu người dùng nhập list số nguyên và số k, sau đó tìm và in ra
    vị trí đầu tiên của k.
    """
    try:
        # 1. Nhập list số nguyên
        input_list_str = input("Nhập các số nguyên cho list (cách nhau bởi dấu cách): ")
        danh_sach_so_nguyen = [int(x) for x in input_list_str.split()]
        # 2. Nhập số k cần tìm
        k = int(input("Nhập số nguyên k cần tìm: "))
    except ValueError:
        print("Lỗi: Vui lòng đảm bảo bạn chỉ nhập các số nguyên hợp lệ.")
        return
    if not danh_sach_so_nguyen:
        print("List rỗng.")
        return
    # Logic tìm vị trí k
    vi_tri_k = -1
    for i in range(len(danh_sach_so_nguyen)):
        if danh_sach_so_nguyen[i] == k:
            vi_tri_k = i
            break  # Thoát ngay khi tìm thấy phần tử đầu tiên
    print(f"\nList đã nhập: {danh_sach_so_nguyen}")
    if vi_tri_k != -1:
        print(f"Số **{k}** được tìm thấy lần đầu tại vị trí (chỉ số): **{vi_tri_k}**")
    else:
        print(f"Không tìm thấy số **{k}** trong list.")
# Chạy hàm để thử nghiệm
nhap_va_tim_vi_tri_k()#ý nghĩ của hàm if __name__ == "__main__":thực hiện cái name chính