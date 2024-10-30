# Viết hàm đưa vào 2 số nguyên, số nào lớn hơn thì in bảng cửu chương của số đó
# def lb(a, b):
#     if a > b:
#         for i in range(1, 11):
#             print(f'{a} * {i} = ',a*i)
#     else:
#         for i in range(1, 11):
#             print(f'{b} * {i} = ',a*i)

# if __name__ == '__main__':
#     x, y = map(int, input('input x, y = ').split())
#     lb(x, y)
    
# Viết hàm đưa vào 1 số nguyên a, kiểm tra xem a có phải là số nguyên tố hay không
# from math import *
# def snt(n):
#     if n < 2:
#         return False
#     for i in range(2, isqrt(n) + 1):
#         if n % i == 0:
#             return False
#         return True
    
# if __name__ == '__main__':
#     n = int(input('n = '))
#     print(snt(n))

# Số Armstrong là số có giá trị bằng tổng lập phương của các chữ số trong số đó. 
# Ví dụ: 153 là số Armstrong bởi vì (1*1*1) + (3*3*3) + (5*5*5) = 153.
# def arm(n):
#     t = 0
#     tn = n
#     while n != 0:
#         t += ((n % 10) * (n % 10) * (n % 10))
#         n //= 10
#     if t == tn:
#         return True
#     return False

# if __name__ == '__main__':
#     n = int(input('n = '))
#     print(arm(n))

