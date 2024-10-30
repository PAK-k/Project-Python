# def S(n):
#     if n == 0:
#         return 0
#     else:
#         return n + S(n - 1)

# if __name__ == '__main__':
#     n = int(input('n = '))
#     print(S(n))

# def gt(n):
#     if n == 0:
#         return 1
#     else:
#         return n * gt(n-1)

# if __name__ == '__main__':
#     n = int(input('n = '))
#     print(gt(n))

# def dectobin(n):
#     if n < 2:
#         print(n, end = ' ')
#         return
#     dectobin(n // 2)
#     print(n % 2, end = ' ')

# if __name__ == '__main__':
#     n = int(input('n = '))
#     print(dectobin(n))

# in đảo ngược số n nguyên dương
# def dn(n, kq = 0):
#     if n == 0:
#         return kq
#     else:
#         kq = kq  * 10 + n % 10
#         return dn(n // 10, kq)

# if __name__ == '__main__':
#     n = int(input('n = '))
#     print(dn(n))

# đếm số lượng chữ số nguyên dương n
# def dem(n):
#     if n < 10:
#         return 1
#     else:
#         return 1 + dem(n // 10)

# if __name__ == '__main__':
#     n = int(input('n = '))
#     print(dem(n))

# tìm chữ số có số lượng lớn nhất của chữ số n
def maxx(n, max = 0):
    if n == 0:
        return max
    else:
        m = n % 10
        if m > max:
            max = m
        return maxx(n // 10, max)

if __name__ == '__main__':
    n = int(input('n = '))
    print(maxx(n))

