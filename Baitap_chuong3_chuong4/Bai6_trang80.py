def nhap_va_tim_chuoi_ngan_nhat():
    """
    Yêu cầu người dùng nhập list các chuỗi, sau đó tìm và in ra
    chuỗi ngắn nhất.
    """
    # 1. Nhập dữ liệu từ người dùng
    input_data = input("Nhập các chuỗi/từ (cách nhau bởi dấu cách): ")
    danh_sach_chuoi = input_data.split()#tìm kiếm một ký tự hoặc một chuỗi con được chỉ định
    if not danh_sach_chuoi:
        print("List rỗng. Không có chuỗi nào để so sánh.")
        return
    # Logic tìm chuỗi ngắn nhất
    chuoi_ngan_nhat = danh_sach_chuoi[0]
    for chuoi in danh_sach_chuoi[1:]:
        if len(chuoi) < len(chuoi_ngan_nhat):
            chuoi_ngan_nhat = chuoi
    print(f"\nList chuỗi đã nhập: {danh_sach_chuoi}")
    print(f"Chuỗi ngắn nhất là: **'{chuoi_ngan_nhat}'**")
    print(f"Độ dài của chuỗi này là: **{len(chuoi_ngan_nhat)}**")
# Chạy hàm để thử nghiệm
nhap_va_tim_chuoi_ngan_nhat()#ý nghĩ của hàm if __name__ == "__main__":thực hiên cái name chính