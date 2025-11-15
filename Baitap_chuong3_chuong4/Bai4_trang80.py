def nhap_va_tim_vi_tri_lon_nhat():
    """
    Yêu cầu người dùng nhập list số nguyên, sau đó tìm và in ra
    vị trí (chỉ số) của giá trị lớn nhất.
    """
    try:
        # 1. Nhập dữ liệu từ người dùng
        input_data = input("Nhập các số nguyên (cách nhau bởi dấu cách): ")
        # 2. Chuyển chuỗi nhập thành list các số nguyên
        danh_sach_so_nguyen = [int(x) for x in input_data.split()]
    except ValueError:
        print("Lỗi: Vui lòng chỉ nhập các số nguyên và cách nhau bởi dấu cách.")
        return
    if not danh_sach_so_nguyen:
        print("List rỗng. Không có giá trị lớn nhất.")
        return
    # Logic tìm vị trí lớn nhất
    vi_tri_lon_nhat = 0
    gia_tri_lon_nhat = danh_sach_so_nguyen[0]
    for i in range(1, len(danh_sach_so_nguyen)):
        if danh_sach_so_nguyen[i] > gia_tri_lon_nhat:
            gia_tri_lon_nhat = danh_sach_so_nguyen[i]
            vi_tri_lon_nhat = i
    print(f"\nList đã nhập: {danh_sach_so_nguyen}")
    print(f"Giá trị lớn nhất là: **{gia_tri_lon_nhat}**")
    print(f"Vị trí (chỉ số) của giá trị lớn nhất là: **{vi_tri_lon_nhat}**")
# Chạy hàm để thử nghiệm
nhap_va_tim_vi_tri_lon_nhat()#ý nghĩ của hàm if __name__ == "__main__":thực hiẹn cái name chính