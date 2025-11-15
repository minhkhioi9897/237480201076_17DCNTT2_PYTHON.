def kiem_tra_list_sap_xep():
    """
    Kiểm tra xem list L đã được sắp xếp tăng dần hay chưa.
    """
    try:
        # Nhập list từ người dùng
        input_str = input("Nhập list số nguyên L (cách nhau bởi dấu cách): ")
        L = [int(x) for x in input_str.split()]
    except ValueError:
        print("Lỗi: Vui lòng chỉ nhập các số nguyên hợp lệ.")
        return False
    if len(L) <= 1:
        # List rỗng hoặc chỉ có 1 phần tử luôn được coi là đã sắp xếp
        print(f"\nList đã nhập: {L}")
        print("List có 0 hoặc 1 phần tử, kết quả là: **True**")
        return True
    # Duyệt qua list, so sánh từng cặp phần tử liền kề
    for i in range(len(L) - 1):
        # Nếu phần tử hiện tại (L[i]) lớn hơn phần tử tiếp theo (L[i+1]),
        # list không tăng dần
        if L[i] > L[i + 1]:
            print(f"\nList đã nhập: {L}")
            print("Phần tử tại index", i, "lớn hơn phần tử tiếp theo. List KHÔNG được sắp xếp tăng dần.")
            print("Kết quả là: **False**")
            return False
    # Nếu vòng lặp hoàn tất mà không có cặp nào vi phạm
    print(f"\nList đã nhập: {L}")
    print("List được sắp xếp tăng dần.")
    print("Kết quả là: **True**")
    return True
# Chạy hàm để thử nghiệm Bài 18
kiem_tra_list_sap_xep()