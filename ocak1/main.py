name = input("Adınızı girin: ")
age = int(input("Yaşınızı girin: "))
birth_year = int(input("Doğum yılınızı girin: "))

print(f"Merhaba {name}! {age} yaşındasınız ve {birth_year} yılında doğmuşsunuz.")

num1 = float(input("Birinci sayıyı girin: "))
num2 = float(input("İkinci sayıyı girin: "))

sum_result = num1 + num2
difference = num1 - num2
product = num1 * num2
if num2 != 0:
    division = num1 / num2
else:
    division = "Bölme hatası (0'a bölme)"

print(f"Toplam: {sum_result}")
print(f"Fark: {difference}")
print(f"Çarpım: {product}")
print(f"Bölüm: {division}")
