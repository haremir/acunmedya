number = int(input("Bir sayı girin: "))

if number % 2 == 0:
    print("Girdiğiniz sayı çifttir.")
else:
    print("Girdiğiniz sayı tektir.")

grade = int(input("Notunuzu girin: "))

if 90 <= grade <= 100:
    print("Harf notunuz: A")
elif 80 <= grade <= 89:
    print("Harf notunuz: B")
elif 70 <= grade <= 79:
    print("Harf notunuz: C")
elif 60 <= grade <= 69:
    print("Harf notunuz: D")
else:
    print("Harf notunuz: F")

age = int(input("Yaşınızı girin: "))

if 0 <= age <= 12:
    print("Yaş grubunuz: Çocuk")
elif 13 <= age <= 19:
    print("Yaş grubunuz: Genç")
elif 20 <= age <= 59:
    print("Yaş grubunuz: Yetişkin")
else:
    print("Yaş grubunuz: Yaşlı")
