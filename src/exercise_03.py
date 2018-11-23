
# Palindrome Kontrol

kelime = input("Lütfen kelimeyi giriniz: ")

ters_kelime = kelime[::-1]

if kelime == ters_kelime:
    print("Girdiğiniz kelime Palindrome!")

else:
    print("Girdiğiniz kelime Palindrome değil.")
