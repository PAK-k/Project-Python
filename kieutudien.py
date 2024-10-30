info = {'Ma': 1, 
        'name': 'Phạm Anh Kiệt', 
        'Age': 21, 
        'contry': 'Quảng Nôm', 
        'court': 'CNTT'}
print(info['Age'])  #in value theo key
print(info.get('name')) #in value theo key
print(info.values())    #in all value
print(info.keys())  #in all key
print("///////////////////////////////")
for i in info:  #in vừa key vừa value ko còn ngoặc nhọn
    print(i ,':', info[i] )
print("///////////////////////////////")
# t = {}
# n = int(input('nhập n = '))
# for i in range(n):
#     keys = input('nhập key: ')      #nhập key và value từ bàn phím
#     values = input('nhập value: ')
#     t[keys] = values
# for i in t:
#     print(f'{i} : {t[i]}')

print("///////////////////////////////")
info.__delitem__('contry')
for i in info:  #in vừa key vừa value ko còn ngoặc nhọn
    print(i ,':', info[i] )

print("///////////////////////////////")
info.clear()
print(info)
