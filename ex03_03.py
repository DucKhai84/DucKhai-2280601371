def tao_list(lst):
    return tuple(lst)

input_list = input("Nhập danh sách các số, cách nhau bởi dấu phẩy:");
numbers = list(map(int, input_list.split(',')))
my_tuple = tao_list(numbers)
print("List: ", numbers)
print("Tuple được tạo từ list là: ", my_tuple)
