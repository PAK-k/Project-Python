a = [1, 2.5, 'PAK', 'HELLO KEO', 2 + 5j]
print(a)
s = 'phạm anh kiệt đẹp trai vaiz ò'
print(list(s))
print(len(list(s)))
for i in range(0, len(a)):
    print(a[i], end = ' ')
for i in range(len(a)-1, -1, -1):
    print(a[i], end = ' ')
for item in a:
    print(item)
a[4] = 'hehe'
for item in a:
    print(item)
a.append(30.9)
print(a)
b = [1, 2, 4, 5]
b.insert(2, 3)
for item in b:
    print(item)
b.pop(3)
print(b)

del b[1]
print(b)