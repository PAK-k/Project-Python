#bài 1
'''
cú pháp: print(object, end = end, sep = seperator)
'''
print("pak","duck",sep = "#")
print("phạm anh kiệt", end = "!\n")
print("mệt vl")

#bài 2
# đây là chú thích 1 dòng
'''
đây là
cách để
chú thích 
trên nhiều dòng
'''

#bài 3: biến và kiểu dữ liệu
x100 = 30
y = 30.2
z = 20 - 2j
print("kiểu dự liệu của x100", type(x100))
print("kiểu dự liệu của y", type(y))
print("kiểu dự liệu của z", type(z))

#làm tròn chữ số thực
x200 = 1.234567
print('%.2f' % x200)#cách 1
print("{:.2f}". format(x200))#cách 2
#số phức
x3 = 5+2j
print(x3.real)
print(x3.imag)
#bool
x4 = True
print(type(x4))

x5 = 200
print(bool(x5))

x6 = 0
print(bool(x6))
# xâu kí tự
x7 = 'phạm anh kiệt'
print("kiểu dữ liệu của ",x7,type(x7))

x8 = '''phạm anh kiệt
siu nhân đỏ
siu nhân gao
'''
print(x8)
# ép kiểu
x9 = 123.456
x10 = int(x9)
print(x10)
print(type(x9))
print(type(x10))

#bài 4
a, b, c = 100, 200, "pak"
print(a,b,c)
a, b, c = b, c, a
print(a,b,c)

a1 = 35
cv = 2*3.14*a1
dt = a1*a1*3.14
print('chu vi hình tròn là: ', '%.2f'%cv)
print('diện tích hình tròn là: ', '%.2f'%dt)

#nhập input và map
# cú pháp n = input (prompt)
x11 = input('nhập một chuỗi bất kì :')
print('chuỗi vừa nhập :', x11)
print(type(x11))
x12 = int(input('nhập 1 số nguyên bất kỳ: '))
print('x12 = ',x12)
print(type(x12))
# ex: tính chu vi và diện tích hình chữ nhật
print("///////////////////////////////////////////////////////////////////")
z = float(input('nhập chiều dài hcn: '))
t = float(input('nhập chiều rộng hcn: '))
print('chiều dài là: ',z)
print('chiều rộng là: ',t)
print('chu vi hcn là: ',(z+t)*2)
print('diện tích hcn là: ',z*t)

#nhập 3 số liên tiếp
x13, x14, x15 = map(int, input('nhập 3 số ngẫu nhiên: ').split())
print('tổng 3 số = ', x13+x14+x15)
print('hiệu 3 số = ',x13-x14-x15)
print('tích 3 số = ', x13*x14*x15)
print('thương 3 số = ', x13/x14/x15)

'''import math
print(math.sqrt(49))'''
from math import *
print(sqrt(169))
print(isqrt(37))
print(pow(3,2))
print(ceil(2.3))
print(floor(2.3))
print(factorial(3))
print(abs(-3))
'''
cách hàm hay sài
sqrt, isqrt, 
pow = lũy thừa
ceil = làm tròn lên
floor = làm tròn xuống
factorial = giai thừa
gcd = UCLN
abs, round = làm tròn
'''

#bài 8 , if
#cú pháp 
# kiểm tra chẵn lẻ
x16 = 21
if x16%2 == 0:
    print('chẳn')
else:
    print('lẻ')
# kiểm tra 1 số chia hết cho 3 và 5
x17 = 30
if (x17%3 == 0) and (x17%5 == 0):
    print('chia hết cho 3 và 5')
else:
    print('ko chia hết cho 3 và 5')
# cấu trúc elif
x18 = 6
if x18 == 1:
    print('tháng 1')
elif x18 == 3:
    print('tháng 3')
elif x18 == 6:
    print('tháng 6')
else:
    print('sai! nhập lại')   

#ex
x19, x20 = 300, 200
if x19<x20 : print(x19,' bé hơn ',x20);print('hong lẻ ngu rứa')

#toán tử 3 ngôi
x21 = 'bé hơn' if x19<x20 else 'lớn hơn'
print(x21)

# kiểm tra xem 1 số có lớn hơn hoặc bằng 50 và chia hết cho 1 trong 3 số 3 5 7 hay không
x22 = 80
if x22 >= 50:
    if (x22%3 == 0) or (x22%5 == 0 ) or (x22%7 == 0):
        print('yes')
    else:
        print('no')
else:
    print('no')
