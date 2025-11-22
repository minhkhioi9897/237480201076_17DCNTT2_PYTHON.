import sys


# --- 1. CLASS SINH VIEN (Đối tượng Sinh viên) ---
class SinhVien:
    """
    Đại diện cho một sinh viên với MaSinhVien và Ten.
    """

    def __init__(self, ma_sv, ten_sv):
        # Thuộc tính
        self.ma_sv = ma_sv
        self.ten_sv = ten_sv

    def __str__(self):
        """Trả về chuỗi đại diện cho đối tượng khi in ra."""
        return f"Mã SV: {self.ma_sv:<10} | Tên: {self.ten_sv}"


# --- 2. CLASS QUAN LY SINH VIEN (Module Quản lý) ---
class QuanLySinhVien:
    """
    Quản lý danh sách các đối tượng SinhVien và thực hiện các thao tác CRUD.
    """

    def __init__(self):
        # Khởi tạo danh sách sinh viên rỗng
        self.danh_sach_sv = []

    def tim_sv_theo_ma(self, ma_sv):
        """Tìm kiếm đối tượng SinhVien theo MaSinhVien."""
        for sv in self.danh_sach_sv:
            if sv.ma_sv == ma_sv:
                return sv
        return None

    def them_sinh_vien(self, ma_sv, ten_sv):
        """Thêm một sinh viên mới vào danh sách."""
        # Kiểm tra trùng lặp Mã SV
        if self.tim_sv_theo_ma(ma_sv):
            print(f"❌ Lỗi: Mã sinh viên **{ma_sv}** đã tồn tại. Thao tác thêm bị hủy.")
            return False

        # Tạo đối tượng SinhVien và thêm vào danh sách
        sv_moi = SinhVien(ma_sv, ten_sv)
        self.danh_sach_sv.append(sv_moi)
        print(f"✅ Thêm sinh viên **{ten_sv}** (Mã: {ma_sv}) thành công.")
        return True

    def xoa_sinh_vien(self, ma_sv):
        """Xóa sinh viên khỏi danh sách dựa trên MaSinhVien."""
        sv_can_xoa = self.tim_sv_theo_ma(ma_sv)

        if sv_can_xoa:
            self.danh_sach_sv.remove(sv_can_xoa)
            print(f"✅ Xóa sinh viên **{sv_can_xoa.ten_sv}** (Mã: {ma_sv}) thành công.")
            return True
        else:
            print(f"❌ Lỗi: Không tìm thấy sinh viên có Mã **{ma_sv}**.")
            return False

    def sua_sinh_vien(self, ma_sv, ten_moi):
        """Cập nhật tên cho sinh viên dựa trên MaSinhVien."""
        sv_can_sua = self.tim_sv_theo_ma(ma_sv)

        if sv_can_sua:
            ten_cu = sv_can_sua.ten_sv
            sv_can_sua.ten_sv = ten_moi
            print(f"✅ Sửa thành công. SV Mã {ma_sv}: Tên cũ **{ten_cu}** -> Tên mới **{ten_moi}**.")
            return True
        else:
            print(f"❌ Lỗi: Không tìm thấy sinh viên có Mã **{ma_sv}**.")
            return False

    def xem_danh_sach_sv(self):
        """Hiển thị toàn bộ danh sách sinh viên."""
        if not self.danh_sach_sv:
            print("\n--- Danh sách sinh viên đang **RỖNG** ---")
            return

        print("\n--- 📚 DANH SÁCH SINH VIÊN HIỆN CÓ 📚 ---")
        # Sắp xếp danh sách theo Mã sinh viên (ID)
        ds_sv_sap_xep = sorted(self.danh_sach_sv, key=lambda sv: sv.ma_sv)

        # In tiêu đề
        print("Mã SV:         | Tên:")
        print("-----------------------------------")

        for i, sv in enumerate(ds_sv_sap_xep):
            print(f"{i + 1}. {sv}")
        print("-----------------------------------")
        print(f"Tổng số sinh viên: {len(self.danh_sach_sv)}.")
        print("-----------------------------------\n")


# --- 3. CHƯƠNG TRÌNH CHÍNH (Giao diện người dùng) ---
def hien_thi_menu():
    """Hiển thị menu chức năng."""
    print("\n======== ⚙️ CHƯƠNG TRÌNH QUẢN LÝ SINH VIÊN ⚙️ ========")
    print("1. Thêm sinh viên")
    print("2. Xóa sinh viên")
    print("3. Sửa sinh viên")
    print("4. Xem danh sách sinh viên")
    print("5. Thoát")
    print("-------------------------------------------------------")


def lay_input_hop_le(prompt):
    """Hàm lấy input không rỗng và loại bỏ khoảng trắng dư thừa."""
    while True:
        data = input(prompt).strip()
        if data:
            return data
        print("⚠ Giá trị không được để trống. Vui lòng nhập lại.")


def main():
    """Hàm chạy chương trình chính."""
    # Khởi tạo đối tượng quản lý
    quan_ly = QuanLySinhVien()

    while True:
        hien_thi_menu()

        lua_chon = input("Mời bạn chọn chức năng (1-5): ")

        if lua_chon == '1':
            # 1. Thêm sinh viên
            print("\n--- THÊM SINH VIÊN ---")
            ma_sv = lay_input_hop_le("Nhập Mã sinh viên: ")
            ten_sv = lay_input_hop_le("Nhập Tên sinh viên: ")
            quan_ly.them_sinh_vien(ma_sv, ten_sv)

        elif lua_chon == '2':
            # 2. Xóa sinh viên
            print("\n--- XÓA SINH VIÊN ---")
            ma_sv = lay_input_hop_le("Nhập Mã sinh viên cần xóa: ")
            quan_ly.xoa_sinh_vien(ma_sv)

        elif lua_chon == '3':
            # 3. Sửa sinh viên
            print("\n--- SỬA SINH VIÊN ---")
            ma_sv = lay_input_hop_le("Nhập Mã sinh viên cần sửa: ")

            sv_ton_tai = quan_ly.tim_sv_theo_ma(ma_sv)
            if sv_ton_tai:
                ten_moi = lay_input_hop_le(f"Nhập Tên mới cho sinh viên **{sv_ton_tai.ten_sv}**: ")
                quan_ly.sua_sinh_vien(ma_sv, ten_moi)
            else:
                print(f"❌ Lỗi: Không tìm thấy sinh viên có Mã **{ma_sv}** để sửa.")

        elif lua_chon == '4':
            # 4. Xem danh sách sinh viên
            quan_ly.xem_danh_sach_sv()

        elif lua_chon == '5':
            # 5. Thoát
            print("\n👋 Cảm ơn bạn đã sử dụng chương trình. Tạm biệt!")
            sys.exit(0)  # Thoát chương trình

        else:
            print("❗ Lựa chọn không hợp lệ. Vui lòng chọn lại từ 1 đến 5.")


# Gọi hàm main để chạy chương trình
if __name__ == "__main__":
    main()