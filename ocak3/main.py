for i in range(1, 101):
    print(i)

for i in range(2, 101, 2):
    print(i)

number = int(input("Bir sayı girin: "))
factorial = 1

for i in range(1, number + 1):
    factorial *= i

print(f"{number}! = {factorial}")

for i in range(2, 101):
    is_prime = True
    for j in range(2, i):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        print(i)