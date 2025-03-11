numbers = []
for i in range(5):
    num = int(input(f"{i+1}. sayıyı girin: "))
    numbers.append(num)

total = sum(numbers)
average = total / len(numbers)
max_number = max(numbers)
min_number = min(numbers)

print(f"Liste: {numbers}")
print(f"Toplam: {total}")
print(f"Ortalama: {average}")
print(f"En büyük sayı: {max_number}")
print(f"En küçük sayı: {min_number}")

words = []
for i in range(5):
    word = input(f"{i+1}. kelimeyi girin: ")
    words.append(word)

words.reverse()
print(f"Ters sıralanmış kelimeler: {words}")

unique_numbers = list(set(numbers))
print(f"Tekrar etmeyen sayılar: {unique_numbers}")
