def tim_gia_tri_x_trong_list():
    """
    Tìm vị trí (index) của giá trị x trong list L.
    """
    try:
        # 1. Nhập list L
        input_l_str = input("Nhập list số nguyên L (cách nhau bởi dấu cách): ")
        L = [int(x) for x in input_l_str.split()]
        # 2. Nhập giá trị x
        x = int(input("Nhập giá trị x cần tìm: "))
    except ValueError:
        print("Lỗi: Vui lòng nhập số nguyên hợp lệ cho cả list và x.")
        return
    # Duyệt qua list L để tìm x
    vi_tri_tim_thay = -1
    for i in range(len(L)):
        if L[i] == x:
            vi_tri_tim_thay = i
            # Nếu chỉ cần tìm vị trí đầu tiên, dùng 'break' ở đây
            break
            # In kết quả
    print(f"\nList L đã nhập: {L}")
    print(f"Giá trị X cần tìm: {x}")
    if vi_tri_tim_thay != -1:
        print(f"Giá trị {x} được tìm thấy tại vị trí (index): **{vi_tri_tim_thay}**")
    else:
        print(f"Không tìm thấy giá trị {x} trong list.")
# Chạy hàm để thử nghiệm Bài 16
tim_gia_tri_x_trong_list()