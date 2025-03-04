def dao_nguoc_chuoi(str):
    return str[::-1]

input_str = input("Nhập chuỗi cần đảo ngược: ")
numbers = list(map(int, input_str.split(',')))
list_dao_nguoc = dao_nguoc_chuoi(input_str)
print("Chuỗi sau khi đảo ngược là: ", list_dao_nguoc)