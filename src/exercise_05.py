def donusturucu():

    while True:

        try:
            celcius = float(input("Celcisus cinsinden sıcaklığı giriniz? "))

        except ValueError as exc:
            print(exc)

        else:

            fahrenheit = (celcius * 9/5) + 32    # (1°C × 9/5) + 32 = 33.8°F

            print("{} °C {} °F'dır.".format(celcius, fahrenheit))


print("Fahrenheit - Celsius Dönüştürücüye Hoş Geldiniz!")

donusturucu()
