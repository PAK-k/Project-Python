from random import randint

KEO = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

BUA = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

BAO = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

while True:
    nguoi = int(input('Nhập phương án của bạn(1-kéo, 2-búa, 3-bao, 4-Thoát) : '))
    may = randint(1, 3)
    if nguoi == 1:
        print(f'Bạn chọn: KÉO')
        print(KEO)
        if may == 1:
            print(f'Máy chọn: KÉO')
            print(KEO)
            print('---------')
            print('Kết quả: HÒA')
        elif may == 2:
            print(f'Máy chọn: BÚA')
            print(BUA)
            print('---------')
            print('Kết quả: THUA')
        elif may == 3:
            print(f'Máy chọn: BAO')
            print(BAO)
            print('---------')
            print('Kết quả: THẮNG')

    if nguoi == 2:
        print(f'Bạn chọn: BÚA')
        print(BUA)
        if may == 1:
            print(f'Máy chọn: KÉO')
            print(KEO)
            print('---------')
            print('Kết quả: THẮNG')
        elif may == 2:
            print(f'Máy chọn: BÚA')
            print(BUA)
            print('---------')
            print('Kết quả: HÒA')
        elif may == 3:
            print(f'Máy chọn: BAO')
            print(BAO)
            print('---------')
            print('Kết quả: THUA')

    if nguoi == 3:
        print(f'Bạn chọn: BAO')
        print(BAO)
        if may == 1:
            print(f'Máy chọn: KÉO')
            print(KEO)
            print('---------')
            print('Kết quả: THUA')
        elif may == 2:
            print(f'Máy chọn: BÚA')
            print(BUA)
            print('---------')
            print('Kết quả: THẮNG')
        elif may == 3:
            print(f'Máy chọn: BAO')
            print(BAO)
            print('---------')
            print('Kết quả: HÒA')
 
    if nguoi == 4:
        print('Trò chơi kết thúc!!')
        break