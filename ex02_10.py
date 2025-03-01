def dao_nguoc_chuoi (chuoi):
    return chuoi[::-1]

input_str = input("Nhập vào chuỗi: ")

print("Chuỗi đã đảo ngược: " , dao_nguoc_chuoi(input_str))