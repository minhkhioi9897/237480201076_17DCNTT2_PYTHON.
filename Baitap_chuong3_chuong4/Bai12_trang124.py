def tim_so_nho_nhat_trong_doan():
    """
    Tìm và in ra số nhỏ nhất trong list L nằm trong đoạn chỉ số từ a đến b (L[a] đến L[b]).
    """
    # 1. Nhập list L
    try:
        input_l_str = input("Nhập list số nguyên L (cách nhau bởi dấu cách): ")
        L = [int(x) for x in input_l_str.split()]
    except ValueError:
        print("Lỗi: Vui lòng nhập các số nguyên hợp lệ cho list L.")
        return
    # 2. Nhập hai chỉ số a và b
    try:
        a = int(input("Nhập chỉ số bắt đầu a (số nguyên dương): "))
        b = int(input("Nhập chỉ số kết thúc b (số nguyên dương, b > a): "))
    except ValueError:
        print("Lỗi: Vui lòng nhập số nguyên dương hợp lệ cho a và b.")
        return
    # --- XỬ LÝ KIỂM TRA ĐIỀU KIỆN ---
    # Kiểm tra điều kiện 1: a và b phải là số dương (theo đề bài)
    if a < 0 or b < 0:
        print("Lỗi: Chỉ số a và b phải là số nguyên dương.")
        return
    # Kiểm tra điều kiện 2: a phải nhỏ hơn b
    if a >= b:
        print("Lỗi: Chỉ số bắt đầu 'a' phải nhỏ hơn chỉ số kết thúc 'b' (a < b).")
        return
    # Kiểm tra điều kiện 3: Chỉ số a và b phải nằm trong phạm vi của list
    len_L = len(L)
    if a >= len_L or b >= len_L:
        print(
            f"Lỗi: Chỉ số a và/hoặc b nằm ngoài phạm vi của list (List có {len_L} phần tử, chỉ số từ 0 đến {len_L - 1}).")
        return
    # --- 3. THỰC HIỆN TÌM GIÁ TRỊ NHỎ NHẤT ---
    # Slicing (cắt) list để lấy đoạn con từ a đến b (bao gồm b)
    # Python slice: L[start:end] - end là index KHÔNG BAO GỒM, nên dùng b+1
    doan_con = L[a: b + 1]
    # Tìm giá trị nhỏ nhất trong đoạn con này
    so_nho_nhat = min(doan_con)
    # 4. In kết quả
    print(f"\nList L đã nhập: {L}")
    print(f"Phạm vi tìm kiếm (chỉ số): từ {a} đến {b}")
    print(f"Đoạn con được xét: {doan_con}")
    print(f"Số nhỏ nhất trong đoạn con là: **{so_nho_nhat}**")
# Chạy hàm để thử nghiệm Bài 12
tim_so_nho_nhat_trong_doan()