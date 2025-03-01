number = int(input("Nhập vào số bạn cần: "))

def isChan(number):
    if number % 2 == 0:
        return "Số chắn"
    return "Số Lẻ"


print("Số bạn nhập là: ",  isChan(number) )