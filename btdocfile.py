# File 2to10.inp là file chứa các số nhị phân (mỗi dòng 1 số), /////////////////////////////////////////////////////////
# hãy chuyển các số nhị phân đó sang số thập phân rồi lưu lại vào file 2to10.out (mỗi dòng 1 số)
# def ttt(n):
#     dec = 0
#     n = n.strip()
#     length = len(n)
#     for i in range(length):
#         dig = n[length - i -1]
#         dec += int(dig)*(2**i)
#     return str(dec)

# with open('2to10inp.txt','r') as file:
#     s = file.readlines()
#     print(s)

# with open('2to10out.txt','a') as file:
#     for i in s:  
#         file.writelines(ttt(i) + '\n')

# Hãy phân tích một số tự nhiên thành các thừa số nguyên tố /////////////////////////////////////////////////////////////////
# def thuaso(n):
#     thuaso = []
#     i = 2
#     while i * i <= n:
#         if n % i:
#             i += 1
#         else:
#             n //= i
#             thuaso.append(i)
#     if n > 1:
#         thuaso.append(n)
#     return thuaso

# if __name__ == '__main__':
#     with open('thuasoinp.txt','r') as file:
#         s = file.readlines()
#         print(s)

#     with open('thuasoout.txt','a') as file:
#         for item in s:
#             item = int(item.strip())
#             thuaso_n = thuaso(item)
#             thuaso_n_str = ' '.join(map(str, thuaso_n))
#             file.writelines(f'{thuaso_n_str}\n')

# Cho một chuỗi ký tự S (gồm chữ và số). Hãy viết chương trình tách chữ và số thành hai chuỗi riêng biệt.
# File chuoi.inp chứa duy nhất 1 chuỗi S
# Hãy tách và ghi vào file chuoi.out 2 dòng, 
# dòng thứ nhất ghi chuỗi ký tự chữ, dòng thứ hai ghi chuỗi ký tự số.
# Nếu như chuỗi nào rỗng thì ghi dấu trừ ‘-’.

# def tachchu(l):
#     chu = ''
#     so = ''
#     for i in l:
#         if i.isdigit():
#             so+=i
#         if i.isalpha():
#             chu+=i
#     if chu == '':
#         chu = '-'
#     if so == '':
#         so = '-'
#     return chu, so

# if __name__ == '__main__':
#     with open('chuoiinp.txt') as file:
#         l = file.readline()
#     chu, so = tachchu(l)
#     with open('chuoiout.txt','a') as file:
#         file.write(f'{chu}\n')
#         file.write(f'{so}\n')

# Cho một dãy số 1, 1, 1, 2, 3, 4, 6,... (quy luật a[i] = a[i - 1] + a[i - 3])/////////////////////////////////////////
# Với a[1] = 1, a[2] = 1, a[3] = 1 (3 số đầu tiên)
# File dayso.inp chứa các số nguyên k (k < 1000), mỗi dòng 1 số
# Hãy tìm a[k] trong dãy số và ghi vào file dayso.out

def ds(n):
    if n == 1 or n == 2 or n == 3:
        return 1
    else:
        return ds(n - 1) + ds(n - 3)

if __name__ == '__main__':
    with open('daysoinp.txt','w') as file:
        while True:
            n = int(input('input n = '))
            if n == 0:
                break
            file.write(f'{n}\n')

    with open('daysoinp.txt') as file:
        s = file.readlines()
        print(s)
    
    with open('daysoout.txt','a') as file:
        for i in s:
            k = int(i.strip())
            a = ds(k)
            file.writelines(f'{a}\n')