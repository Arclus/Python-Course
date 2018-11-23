n = int(input("Lütfen notunuzu giriniz :"))

if 0 <= n < 20:
    print("Notunuz FF")

elif 20 <= n < 30:
    print("Notunuz FD")

elif 30 <= n < 40:
    print("Notunuz DD")

elif 40 <= n < 49:
    print("Notunuz DC")

elif 49 <= n < 55:
    print("Notunuz CC")

elif 55 <= n < 65:
    print("Notunuz CB")

elif 65 <= n < 75:
    print("Notunuz BB")

elif 75 <= n < 85:
    print("Notunuz BA")

elif 85 <= n <= 100:
    print("Notunuz AA")

else:
    print("Lütfen 0-100 arası bir tam sayı giriniz.")
