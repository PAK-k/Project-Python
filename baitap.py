from math import *

#kiểm n có phải là số nguyên tố không, nếu đúng in 1, sai in 0
def snt(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
        else:
            return True
    
#in tổng chữ số của n
def tongchuso(n):
    s = 0
    while n > 0:
        s += n % 10
        n = n // 10
    return s

#in tổng số chẵn của n
def tongchusochan(n):
    s = 0
    while n > 0:
        if n % 10 % 2 == 0:
            s += n % 10 
        n = n // 10
    return s

#in ra tổng chữ số của n là số nguyên tố
def tongsnt(n):
    s = 0
    while n > 0:
        x = n % 10
        if x == 2 or x == 3 or x == 5 or x == 7:
            s += x
        n //= 10
    return s

#in ra số lật ngược của n
def sln(n):
    l = 0
    while n > 0:
        l = l * 10 + n % 10
        n //= 10
    return l

#in số lượng ước của n là số nguyên tố
def slsnt(n):
    dem = 0
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            dem += 1
            while n % i == 0:
                n //= i
    if n > 1:
        dem += 1
    return dem

#hàm 7
def ham7(n):
    res = -1
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            res = i
            while n % i == 0:
                n //= i
    if n > 1:
        res = n
    return res

#hàm 8
def ham8(n):
    while n > 0:
        if n % 10 == 6:
            return True
        n //= 10
    return False

#hàm 9
def ch8(n):
    if tongchuso(n) % 8 == 0:
        return True
    return False

#hàm 10 tính tổng giai thừa của n
def giaithua(n):
    gt = 1
    for i in range(1, n + 1):
        gt *= i
    return gt
def tonggiaithua(n):
    t = 0
    for i in range(1, n + 1):
        t += giaithua(i)
    return t

#hàm 11 kiểm tra n có phải được tạo từ 1 số hay không
def checkn(n):
    while n > 0:
        donvi = n % 10
        while n > 0:
            if donvi != n % 10:
                return False
            n //= 10
        return True

#hàm 12 kiểm tra n có phải có chữ số tận cùng lớn nhất hay không
def checkl(n):
    donvi = n % 10
    while n > 0:
        if donvi < n % 10:
            return False
        n //= 10
    return True

#hàm 13 in tổng lũy thừa của n vd 123 = 1^3+2^3+3^3
def tlt(n):
    mu = n % 10
    t = 0
    while n > 0:
        t += (n % 10) ** mu
        n //= 10
    return t

if __name__ == '__main__':
    a = int(input('nhập a = '))
    if snt(a):
        print('1')
    else:
        print('0')
    print(f'tổng chữ số của {a} = ',tongchuso(a))
    print(f'tổng chữ số chẵn của {a} = ',tongchusochan(a))
    print(f'tổng chữ số của {a} là số nguyên tố = ',tongsnt(a))
    print(f'số lộn ngược của {a} là = ',sln(a))
    print(f'số lượng ước của {a} là số nguyên tố = ',slsnt(a))
    print(f'ước lớn nhất của {a} là = ',ham7(a))
    if ham8(a): 
        print('1')
    else:
        print('0')
    if ch8(a):
        print('1')
    else:
        print('0')
    print(f'tổng giai thừa của {a} = ',tonggiaithua(a))
    if checkn(a):
        print('1')
    else:
        print('0')
    if checkl(a):
        print('1')
    else:
        print('0')
    print(f'tổng lũy thừa của {a} = ',tlt(a))