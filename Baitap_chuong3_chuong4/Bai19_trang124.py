def sap_xep_list():
    """
    Nhập một list số nguyên và sắp xếp nó theo thứ tự tăng dần.
    """
    try:
        input_str = input("Nhập list số nguyên (cách nhau bởi dấu cách): ")
        L = [int(x) for x in input_str.split()]
    except ValueError:
        print("Lỗi: Vui lòng chỉ nhập các số nguyên hợp lệ.")
        return
    # Sử dụng phương thức .sort() để sắp xếp tại chỗ
    L.sort()
    print(f"\nList ban đầu: {L}")
    print(f"List sau khi sắp xếp (tăng dần): **{L}**")
# Chạy hàm để thử nghiệm Bài 19
sap_xep_list()