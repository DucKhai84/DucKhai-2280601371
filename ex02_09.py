number = int(input("Nhập số cần kiểm tra: "))

def isPrime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

if isPrime(number):
    print("Là số nguyên tố")
else:
    print("không là số nguyên tố")