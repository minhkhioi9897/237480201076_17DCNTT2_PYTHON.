def kiem_tra_list_chan_le_xen_ke():
    """
    Kiểm tra xem list có tính chất xen kẽ chẵn - lẻ hay không.
    (Theo định nghĩa nghiêm ngặt, chỉ list len <= 1 là thoả mãn).
    Giải pháp này giả định list phải có sự xen kẽ Chẵn/Lẻ
    """
    try:
        input_str = input("Nhập list số nguyên (cách nhau bởi dấu cách): ")
        L = [int(x) for x in input_str.split()]
    except ValueError:
        print("Lỗi: Vui lòng chỉ nhập các số nguyên hợp lệ.")
        return False
    if len(L) <= 1:
        print(f"\nList: {L}. Kết quả: **True** (Không có cặp nào để kiểm tra).")
        return True
    # Xác định tính chẵn lẻ của phần tử đầu tiên
    dau_tien_chan = L[0] % 2 == 0
    # Duyệt từ phần tử thứ hai
    for i in range(1, len(L)):
        hien_tai_chan = L[i] % 2 == 0
        truoc_do_chan = L[i - 1] % 2 == 0
        # Nếu hai phần tử liên tiếp cùng chẵn HOẶC cùng lẻ
        if hien_tai_chan == truoc_do_chan:
            print(f"\nList: {L}")
            print(f"Vi phạm tại vị trí {i} và {i - 1}. List KHÔNG phải là List số chẵn lẻ.")
            return False
    # Nếu duyệt hết và tất cả các cặp đều khác nhau (chẵn-lẻ xen kẽ)
    print(f"\nList: {L}")
    print("List có tính chất xen kẽ chẵn-lẻ. Kết quả: **True**")
    return True
# Chạy hàm để thử nghiệm Bài 22
kiem_tra_list_chan_le_xen_ke()