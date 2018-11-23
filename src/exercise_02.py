def toplama(x, y):
    return x + y


def cikarma(x, y):
    return x - y


def carpma(x, y):
    return x * y


def bolme(x, y):
    return x / y


while True:

    print("Yapmak İstediğiniz İşlemi Seçiniz!")
    print("1) Toplama")
    print("2) Çıkarma")
    print("3) Çarpma")
    print("4) Bölme")
    print("5) Çıkış")

    secenek = input("Seçiminizi Giriniz (1-2-3-4-5):")

    if secenek == '5':
        break

    sayi_1 = float(input("Birinci sayıyı giriniz: "))
    sayi_2 = float(input("İkinci sayıyı giriniz: "))

    if secenek == '1':
        print(sayi_1, " + ", sayi_2, " = ", toplama(sayi_1, sayi_2))

    elif secenek == '2':
        print(sayi_1, " - ", sayi_2, " = ", cikarma(sayi_1, sayi_2))

    elif secenek == '3':
        print(sayi_1, " * ", sayi_2, " = ", carpma(sayi_1, sayi_2))

    elif secenek == '4':
        print(sayi_1, " / ", sayi_2, " = ", bolme(sayi_1, sayi_2))

    else:
        print("Lütfen menüde bulunan bir sayı seçiniz!")
