
kata_satuan = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

def terbilang(n):
    if n < 10:
        return kata_satuan[n]
    elif n >= 1_000_000_000:
        return terbilang(n // 1_000_000_000) + ' billion ' + (terbilang(n % 1_000_000_000) if n % 1_000_000 != 0 else '')
    elif n >= 1_000_000:
        return terbilang(n // 1_000_000) + ' million ' + (terbilang(n % 1_000_000) if n % 1_000_000 != 0 else '')
    elif n >= 1_000:
        return terbilang(n // 1_000) + " thousend " + terbilang(n % 1_000 if n % 1_000_000 != 0 else '')
    elif n >= 100:
        return terbilang(n//100) + ' hundred ' + terbilang(n%100 if n % 1_000_000 != 0 else '')
    
    elif n >= 20:
            if n//10 == 2:
                return 'twenty ' + terbilang(n%10)
            elif n//10 == 3:
                return 'thirty ' + terbilang (n%10)
            elif n//10 == 4:
                return 'forty ' + terbilang (n%10)
            elif n//10 == 5:
                return 'fifty ' + terbilang (n%10)
            else :
                return terbilang (n//10) + ('ty ' if (n//10) != 8 else 'y') + terbilang (n%10)
        
    else:
        if n == 10:
            return ' ten'
        elif n == 11:
            return ' eleven'
        elif n == 12:
            return ' twelve'
        elif n == 13:
            return ' thirteen'
        elif n == 15:
            return ' fifteen'
        elif n == 18:
            return ' eighteen'
        else:
            return terbilang(n % 10) + 'teen'        

import os
while True:
    os.system('cls')
    try:
        n = int(input('angka ? '))
        print(f'{n:,} = {terbilang(n)}')
    except:
        print('yang bener inputnya, harus angka semua !!')
    os.system('pause')