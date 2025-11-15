def quan_ly_tim_kiem_sinh_vien():
    """
    Chương trình cho phép người dùng nhập danh sách tên sinh viên
    và sau đó tìm kiếm thông tin trên danh sách đó.
    """
    danh_sach_sinh_vien = []
    # --- PHẦN 1: NHẬP DANH SÁCH SINH VIÊN ---
    print("=" * 60)
    print("       CHƯƠNG TRÌNH QUẢN LÝ TÊN SINH VIÊN")
    print("=" * 60)
    print("Vui lòng nhập tên từng sinh viên.")
    print("Nhập 'xong' hoặc nhấn Enter (trống) khi bạn hoàn tất.")
    while True:
        ten_sinh_vien = input(f"Nhập tên sinh viên #{len(danh_sach_sinh_vien) + 1} (hoặc 'xong'): ").strip()
        # Kiểm tra điều kiện dừng
        if ten_sinh_vien.lower() == 'xong' or ten_sinh_vien == "":
            break
        # Thêm tên vào list (chuyển chữ cái đầu thành in hoa cho đẹp)
        danh_sach_sinh_vien.append(ten_sinh_vien.title())
    print("-" * 60)
    print(f"✅ Đã nhập xong {len(danh_sach_sinh_vien)} sinh viên.")
    if not danh_sach_sinh_vien:
        print("Danh sách rỗng. Chương trình kết thúc.")
        return
    # --- PHẦN 2: TÌM KIẾM THÔNG TIN ---
    print("\n--- TÌM KIẾM SINH VIÊN ---")
    print("Danh sách hiện tại: " + ", ".join(danh_sach_sinh_vien))
    while True:
        ten_can_tim = input("\nNhập tên sinh viên cần tìm (hoặc 'thoat' để kết thúc): ").strip()
        if ten_can_tim.lower() == 'thoat' or ten_can_tim == "":
            break
        ten_can_tim_chuan = ten_can_tim.title()
        # Thực hiện tìm kiếm tuần tự (Linear Search)
        tim_thay = False
        vi_tri = -1
        for i in range(len(danh_sach_sinh_vien)):
            if danh_sach_sinh_vien[i] == ten_can_tim_chuan:
                tim_thay = True
                vi_tri = i + 1  # +1 để hiển thị số thứ tự từ 1
                break
        # In kết quả tìm kiếm
        if tim_thay:
            print(f"🌟 KẾT QUẢ: Tìm thấy sinh viên '{ten_can_tim_chuan}' tại vị trí **thứ {vi_tri}** trong danh sách.")
        else:
            print(f"❌ KẾT QUẢ: Không tìm thấy sinh viên '{ten_can_tim_chuan}' trong danh sách.")
    print("\n" + "=" * 60)
    print("Chương trình tìm kiếm đã kết thúc. Tạm biệt!")
    print("=" * 60)
# Chạy chương trình
if __name__ == "__main__":
    quan_ly_tim_kiem_sinh_vien()