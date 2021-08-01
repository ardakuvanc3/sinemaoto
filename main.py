#Tiyatro veya sinema tercihi
#Sinema 15 tl tiyatro 10 tl
#öğrenci %50 indirim
#öğrenci değilse indirimsiz tutar
sinema_fiyat = 15
tiyatro_fiyat = 10
musteri_para = 100

while True:
    isim = input("Adınız Nedir: ")
    soy_isim = input("Soy Adınız Nedir: ")
    print("Hoşgeldiniz,",isim, soy_isim)
    break

while True:
    secim = input("Tiyatro mu Sinema mı?: ")
    ogrenci_sorgu = input("Öğrenci Misiniz: ")
   
    if ogrenci_sorgu <= "20":
        fiyat = (sinema_fiyat* 50/100)
        print("Öğrenci Olduğunuz İçin %50 indirim uygulanmıştır.Ödeyeceğiniz miktar:",fiyat)
        musteri_para -= fiyat
        print("Kalan Para:",musteri_para)
        print("Yaşınız:",ogrenci_sorgu)
        break

    elif ogrenci_sorgu > "20":
        print("20 Yaşından büyük olduğunuz için tam bilet ücreti uygulanmıştır.Ödeyeceğiniz miktar",sinema_fiyat)
        musteri_para -= sinema_fiyat
        print("Kalan Para:",musteri_para)
        print("Yaşınız:",ogrenci_sorgu)
        break
    else:
        pass

while secim == "Tiyatro":

    if ogrenci_sorgu <= "20":
        fiyat = (tiyatro_fiyat * 50/100)
        print("Öğrenci Olduğunuz İçin %50 indirim uygulanmıştır.Ödeyeceğiniz miktar:",fiyat)
        musteri_para -= fiyat
        print("Kalan Para",musteri_para)
        print("Yaşınız:",ogrenci_sorgu)
        break

    elif ogrenci_sorgu > "20":
        print("20 Yaşından büyük olduğunuz için tam bilet ücreti uygulanmıştır.Ödeyeceğiniz miktar:",tiyatro_fiyat)
        musteri_para -= sinema_fiyat
        print("Kalan Para:",musteri_para)
        print("Yaşınız:",ogrenci_sorgu)
        break

    else:
        pass

while True:
    para_sorgu = input("Para Durumunu Öğrenmek İster Misiniz?: ")
    if para_sorgu == "E":
        print(musteri_para)
        print("Çıkış Yapılıyor...")
        break         
    elif para_sorgu == "H":
        print("Çıkış Yapılıyor...")
        break

    

        









