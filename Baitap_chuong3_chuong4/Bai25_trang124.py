def sap_xep_list_chan_le_khong():
    """
    Nhập một list số nguyên L và sắp xếp lại theo thứ tự:
    [Số chẵn khác 0] + [Số 0] + [Số lẻ].
    """
    try:
        # 1. Nhập list từ người dùng
        input_str = input("Nhập list số nguyên (cách nhau bởi dấu cách): ")
        L = [int(x) for x in input_str.split()]
    except ValueError:
        print("Lỗi: Vui lòng chỉ nhập các số nguyên hợp lệ.")
        return
    # 2. Khởi tạo 3 list phân loại
    list_chan = []
    list_so_khong = []
    list_le = []
    # 3. Phân loại các phần tử
    for so in L:
        if so == 0:
            list_so_khong.append(so)
        elif so % 2 == 0:
            list_chan.append(so)
        else:
            list_le.append(so)
    # 4. Nối 3 list lại theo thứ tự yêu cầu
    # Kết quả = [Các số chẵn] + [Các số 0] + [Các số lẻ]
    L_moi = list_chan + list_so_khong + list_le
    # 5. In kết quả
    print("\n" + "=" * 50)
    print("KẾT QUẢ SẮP XẾP LIST")
    print("=" * 50)
    print(f"List ban đầu: {L}")
    print(f"List sau khi sắp xếp: **{L_moi}**")
    print("=" * 50)
# Chạy hàm để thử nghiệm Bài 25
sap_xep_list_chan_le_khong()