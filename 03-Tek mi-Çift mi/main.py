print(" --- Tek mi Çift mi Hesaplayıcıya Hoş Geldiniz! ---")


while True:
    kullanici_girisi = input("Lütfen bir tam sayı giriniz: ")

    try:
        sayi = int(kullanici_girisi)

        break

    except ValueError:
        print(f"Hata {kullanici_girisi} bir tam sayı değildir. Lütfen bir tam sayı giriniz.")
        print("---------")



if sayi % 2 == 0 :
    print(f"{sayi} bir ÇİFT sayıdır.")

else:
    print(f"{sayi} bir TEK sayıdır.")