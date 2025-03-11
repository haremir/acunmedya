def calculator(a, b):
    total = a + b
    difference = a - b
    product = a * b
    if b != 0:
        division = a / b
    else:
        division = "Bölme hatası (0'a bölme)"
    
    return total, difference, product, division

num1 = float(input("Birinci sayıyı girin: "))
num2 = float(input("İkinci sayıyı girin: "))
total, difference, product, division = calculator(num1, num2)

print(f"Toplam: {total}")
print(f"Fark: {difference}")
print(f"Çarpım: {product}")
print(f"Bölüm: {division}")

def is_palindrome(word):
    return word == word[::-1]

word = input("Bir kelime girin: ")
if is_palindrome(word):
    print(f"{word} -> Palindrom")
else:
    print(f"{word} -> Değil")

def years_to_100(age):
    years_left = 100 - age
    return years_left

age = int(input("Yaşınızı girin: "))
years_left = years_to_100(age)
print(f"{years_left} yıl sonra 100 yaşında olacaksınız.")
