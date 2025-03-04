def dem_so_phan_tu(input_list):
    count_lst = {}
    for item in input_list:
        if item in count_lst:
            count_lst[item] += 1
        else:
            count_lst[item] = 1
    return count_lst

input_list = input("Nhập danh sách các số, cách nhau bởi dấu phẩy:");
word_list = input_list.split()

so_lan_xuat_hien = dem_so_phan_tu(word_list)
print("Số lần xuất hiện của mỗi phần tử trong list là: ", so_lan_xuat_hien)