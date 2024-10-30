#Nhập vào một list số nguyên L, tìm và in ra giá trị lớn nhất trong L
# a = []
# n = int(input('n = '))
# for i in range(0, n):
#     a.append(input(f'a[{i}] = '))
# print(max(a))

# Nhập vào một list số nguyên L, nhập vào 2 số nguyên dương a và b (a < b < len(L))
# Tìm và in ra số nhỏ nhất trong list từ vị trí a đến vị trí b
# L = list(map(int, input('nhập list: ').split()))
# a = int(input('nhập a = '))
# b = int(input('nhập b = '))
# if 0 <= a < b <= len(L):
#     minvl = L[a]
#     for i in range(a, b+1):
#         if L[i] < minvl:
#             minvl = L[i]
#             print(f'số nhỏ nhất trong list từ vị trí {a} đến vị trí {b} là: {L[i]}')
# else:
#     print('bạn đã nhập sai lêu lêu!')

#Nhập vào một list số nguyên L,
# hãy kiểm tra xem tất cả các phần tử trong mảng có bằng nhau hay không, nếu có thì in True, không có thì in False
# l = list(map(int, input('nhập list: ').split()))
# kq = True
# first = l[0]
# for item in l:
#     if first != item:
#         kq = False
# print(kq)

#Nhập vào một list số nguyên L, tìm và in ra giá trị dương đầu tiên của list, 
#nếu không có giá trị dương, ta in ra -1
# l = list(map(int, input('input list: ').split()))
# found = False
# for item in l:
#     if item > 0:
#         print(item)
#         found = True
#         break
# if not found:
#     print(-1)

# Nhập vào một list L, hãy tìm và in ra giá trị âm lớn nhất trong L, nếu L không có giá trị âm thì ta in 0
# l = list(map(int, input('nhập list: ').split()))
# for item in l:
#     if item >= 0:
#         l.remove(item)
# maxam = l[0]
# for item in l:
#     if item > maxam:
#         maxam = item
# print(maxam)

# Nhập vào một list số nguyên L, nhập vào số nguyên x, tìm giá trị trong list xa x nhất
# from math import *
# l = list(map(int, input('nhập list: ').split()))
# x = int(input('nhập x = '))
# maxvl = -1
# vl = 0
# for item in l:
#     dis = abs(item - x)
#     if dis > maxvl:
#         maxvl = dis
#         vl = item
# print(f'giá trị xa nhất với {x} trong list là: {vl}')

# Nhập vào một list số nguyên L, tính giá trị trung bình của list L
# l = list(map(int, input('nhập list: ').split()))
# sum = 0
# for item in l:
#     sum += item
# avg = sum / len(l)
# print(f'giá trị trung bình của list: {avg}')

# Nhập vào một list số nguyên L, hãy kiểm tra xem L có được sắp xếp từ bé đến lớn hay không, 
# nếu có thì in True, không có thì in False
# l = list(map(int, input('nhập list: ').split()))
# if l == sorted(l):
#     print(True)
# else:
#     print(False)

# Xây dựng chương trình quản lý điện năng tiêu thụ ///////////////////////////////////////////////////////////////////////////
# bài này có sử dụng thư viện pandas để in ra bảng 
import pandas as pd
def tinhTienDien(kw):
    tiendien = 0
    VAT = 0
    tongdien = 0
    if kw <= 100:
        tiendien = kw * 1500
    elif 100 < kw <= 200:
        tiendien = 100 * 1500 + (kw - 100) * 2000
    elif 200 < kw <= 300:
        tiendien = 100 * 1500 + 100 * 2000 + (kw - 200) * 2500
    else:
        tiendien = 100 * 1500 + 100 * 2000 + 100 * 2500 + (kw - 300) * 3000
    VAT = tiendien * 0.1
    tongdien = tiendien + VAT
    return int(tongdien)

if __name__ == '__main__':
    n = int(input('nhập số hộ mong muốn: '))
    for i in range(n):
        maho = ''
        tenho = ''
        diachi = ''
        kw = 0
        while True:
            maho = input('nhập mã hộ: ') + (',')
            if maho != '':
                break
        while True:
            tenho = input('nhập tên hộ: ') + (',')
            if tenho != '':
                break
        while True:
            diachi = input('nhập địa chỉ: ') + (',')
            if diachi != '':
                break
        while True:
            kw = int(input('nhập số kw đã tiêu thụ: '))
            if kw >= 0:
                break
        tiendien = tinhTienDien(kw) 
        kw = str(kw) + (',')
        tiendien = str(tiendien) + ('\n')

        with open('data.txt','a') as file:
            file.writelines([maho,tenho,diachi,kw,tiendien])
    
    df = pd.read_csv('data.txt',sep=',',header=None,names=[' mã hộ ',' tên chủ hộ ',' địa chỉ ',' số điện ',' tiền điện phải trả '])
    print(df)