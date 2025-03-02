def asal_mi(sayi):
    if sayi <= 1:
        return f"{sayi} bir asal sayı değildir."
    if sayi <= 3:
        return f"{sayi} bir asal sayıdır."
    if sayi % 2 == 0 or sayi % 3 == 0:
        return f"{sayi} bir asal sayı değildir."
    i = 5
    while i * i <= sayi:
        if sayi % i == 0 or sayi % (i + 2) == 0:
            return f"{sayi} bir asal sayı değildir."
        i += 6
    return f"{sayi} bir asal sayıdır."

print(asal_mi(7))
print(asal_mi(10))

#------------------------------------------------------#

def hesap_makinesi(sayi1, sayi2, islem):
    if islem == '+':
        return f"{sayi1} + {sayi2} = {sayi1 + sayi2}"
    elif islem == '-':
        return f"{sayi1} - {sayi2} = {sayi1 - sayi2}"
    elif islem == '*':
        return f"{sayi1} * {sayi2} = {sayi1 * sayi2}"
    elif islem == '/':
        if sayi2 == 0:
            return "Bölme işlemi için ikinci sayı 0 olamaz!"
        else:
            return f"{sayi1} / {sayi2} = {sayi1 / sayi2}"
    else:
        return "Geçersiz işlem türü!"

print(hesap_makinesi(5, 3, '+'))
print(hesap_makinesi(10, 2, '/'))
print(hesap_makinesi(4, 0, '/'))
print(hesap_makinesi(6, 2, '%'))