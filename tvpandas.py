import pandas as pd
df = pd.read_csv('sinhvien1.csv', sep=',', header=None, names=['ma','ten','lop','que']) # Đọc file txt
# df = pd.read_csv('sinhvien1.csv', sep=',', header=None, names=['ma','ten','lop','que']) // Đọc file csv
# df = pd.read_excel('sinhvien2.xlsx', header=None, names=['ma','ten','lop','que']) # Đọc file Excel
# df1 = df.sort_values(['que']) # sắp xếp theo điều kiện
# cách 1 tìm theo đk
# df1 = df.query('que=="Quảng Nam" or lop=="21cntt2"')
# cách 2
qq = ['Quảng Nam','Đà Nẵng']
df1 = df.query('que in @qq')
print(df1)
