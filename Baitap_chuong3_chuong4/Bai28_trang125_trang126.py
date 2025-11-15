def quan_ly_sinh_vien():
    """
    Chương trình quản lý sinh viên với 4 chức năng chính: Thêm, Xóa, Sửa, Xem.
    Sử dụng dictionary: {Ma_Sinh_Vien: Ten_Sinh_Vien}.
    """
    # Khởi đầu là danh sách sinh viên rỗng (dùng dictionary)
    danh_sach_sinh_vien = {}
    while True:
        # 1. Hiển thị menu chức năng
        print("\n" + "=" * 50)
        print("          HỆ THỐNG QUẢN LÝ SINH VIÊN")
        print("=" * 50)
        print("1. Thêm sinh viên (Mã SV & Tên SV)")
        print("2. Xóa sinh viên (theo Mã SV)")
        print("3. Sửa thông tin sinh viên (theo Mã SV)")
        print("4. Xem danh sách sinh viên")
        print("5. Thoát chương trình")
        print("=" * 50)
        chon = input("▶️ Nhập lựa chọn của bạn (1-5): ").strip()
        # --- 2. Xử lý các chức năng ---
        if chon == '1':
            # 1. Thêm sinh viên
            ma_sv = input("   Nhập Mã sinh viên: ").strip().upper()
            if ma_sv in danh_sach_sinh_vien:
                print(f"❌ Lỗi: Mã sinh viên '{ma_sv}' đã tồn tại. Không thêm được.")
            else:
                ten_sv = input("   Nhập Tên sinh viên: ").strip().title()
                danh_sach_sinh_vien[ma_sv] = ten_sv
                print(f"✅ Đã thêm sinh viên: [{ma_sv} - {ten_sv}]")

        elif chon == '2':
            # 2. Xóa sinh viên
            ma_sv = input("   Nhập Mã sinh viên cần XÓA: ").strip().upper()
            if ma_sv in danh_sach_sinh_vien:
                ten_sv_bi_xoa = danh_sach_sinh_vien.pop(ma_sv)
                print(f"✅ Đã xóa sinh viên: [{ma_sv} - {ten_sv_bi_xoa}]")
            else:
                print(f"❌ Lỗi: Không tìm thấy Mã sinh viên '{ma_sv}' để xóa.")
        elif chon == '3':
            # 3. Sửa sinh viên
            ma_sv = input("   Nhập Mã sinh viên cần SỬA thông tin: ").strip().upper()
            if ma_sv in danh_sach_sinh_vien:
                ten_cu = danh_sach_sinh_vien[ma_sv]
                print(f"   Thông tin hiện tại: [{ma_sv} - {ten_cu}]")
                ten_moi = input("   Nhập Tên sinh viên MỚI: ").strip().title()
                danh_sach_sinh_vien[ma_sv] = ten_moi
                print(f"✅ Đã cập nhật thành công: [{ma_sv} - {ten_moi}]")
            else:
                print(f"❌ Lỗi: Không tìm thấy Mã sinh viên '{ma_sv}' để sửa.")
        elif chon == '4':
            # 4. Xem danh sách sinh viên
            print("\n" + "*" * 30)
            print("DANH SÁCH SINH VIÊN HIỆN TẠI")
            print("*" * 30)
            if not danh_sach_sinh_vien:
                print("Danh sách hiện đang rỗng.")
            else:
                stt = 1
                # Duyệt qua dictionary theo thứ tự Mã SV
                for ma_sv, ten_sv in sorted(danh_sach_sinh_vien.items()):
                    print(f"{stt}. Mã SV: **{ma_sv}** - Tên: {ten_sv}")
                    stt += 1
            print("*" * 30)
        elif chon == '5':
            # 5. Thoát chương trình
            print("\n👋 Đã thoát chương trình. Tạm biệt!")
            break
        else:
            print("⚠️ Lựa chọn không hợp lệ. Vui lòng nhập số từ 1 đến 5.")
# Chạy chương trình
quan_ly_sinh_vien()