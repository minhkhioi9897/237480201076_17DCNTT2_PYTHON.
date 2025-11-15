def tim_vi_tri_tich_lan_can():
    """
    Tìm vị trí i sao cho L[i] bằng tích của hai giá trị lân cận.
    """
    try:
        input_str = input("Nhập list số nguyên (cách nhau bởi dấu cách): ")
        L = [int(x) for x in input_str.split()]
    except ValueError:
        print("Lỗi: Vui lòng chỉ nhập các số nguyên hợp lệ.")
        return
    if len(L) < 3:
        print(f"\nList: {L}")
        print("List quá ngắn (< 3 phần tử). Không thể kiểm tra lân cận. Kết quả: **-1**")
        return -1
    vi_tri_tim_thay = -1
    # Duyệt từ index 1 đến len(L) - 2 (trừ phần tử đầu và cuối)
    for i in range(1, len(L) - 1):
        if L[i] == L[i - 1] * L[i + 1]:
            vi_tri_tim_thay = i
            break  # Tìm thấy vị trí đầu tiên thì dừng
    print(f"\nList: {L}")
    if vi_tri_tim_thay != -1:
        print(f"Vị trí (index) đầu tiên thỏa mãn điều kiện L[i] = L[i-1] * L[i+1] là: **{vi_tri_tim_thay}**")
    else:
        print("Không tồn tại vị trí nào thỏa mãn điều kiện. Kết quả: **-1**")
    return vi_tri_tim_thay
# Chạy hàm để thử nghiệm Bài 21
tim_vi_tri_tich_lan_can()