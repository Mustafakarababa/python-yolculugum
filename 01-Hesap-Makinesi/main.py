print("--- Benim Basit Hesap Makineme Hoş Geldiniz! --- \n")

print("Lütfen hesap yapmak istediğiniz sayıları giriniz:")

sayi1 = float(input("1.Sayı: "))
sayi2 = float(input("2.Sayı: "))

print("lütfen bu sayılara hangi işlemi yaptırmak istediğiniz seçiniz:  \nToplama : 1 \nÇıkarma:  2 \nÇarpma:   3 \nBölme:    4")

islem = float(input("işlem:"))


if(islem == 1):
    sonuc = sayi1 +sayi2
    print("Toplama işleminin sonucu: " + str(sonuc))
elif(islem == 2):
    sonuc = sayi1-sayi2
    print("Çıkarma işleminin sonucu: " + str(sonuc))
elif(islem == 3):
    sonuc = sayi1 * sayi2
    print("Çarpma işleminin sonucu: " + str(sonuc))
elif(islem == 4):
    if(sayi2 == 0):
        print("Bölme işleminde 0 sayısı hata verir. Lütfen başka bir sayı giriniz.")
    else:
        sonuc = sayi1 / sayi2
        print("Bölme işleminin sonucu: " + str(sonuc))
else:
    print("Lütfen konsolda gösterilen işlem numaralarından birini seçiniz!")

