import datetime

print(" --- Yaş Hesaplama Uygulamama Hoş Geldiniz! ---\n")

print("Lütfen doğum yılınızı giriniz: ")

dogumYili = int(input())

mevcutYil = datetime.datetime.now().year

if dogumYili > mevcutYil :
    print("Gerçek doğum yılınızı giriniz!")

else:
    yas = mevcutYil - dogumYili
    print(f"Siz bu yıl {yas} yaşına gireceksiniz.")
