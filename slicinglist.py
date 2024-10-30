a = [1, 6, 9, 3, 7]
b = a[1:-2:1]
print(b)
c = a[::-1] # đảo ngược đoạn
print(c)
a[1:-2] = [2,3,4] # thêm 1 đoạn
print(a)
a[1:-2] = [] # xóa 1 đoạn
print(a)
b[:0] = [4,5] # chèn nhanh vào đầu
print(b)
b[len(b):] = [8,9,10] # chèn nhanh vào cuối doạn
print(b)
d = a[:] # copy lại list
e = a[:]
print(d)
print(e)
print(d is e)
