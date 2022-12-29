from randevu import Randevu, getRandevuList
from kisi import Kisi, getKisiList


while True:
    print("""
Merhaba, işlem kodları aşağıda görünmektedir.
1- Kisi Ekle
2- Randevu Ekle
3- Randevu Sil
4- Randevu Listesi
5- Kisi Sil
6- Kisi Listesi
7- Çıkış

    """)
    kod = input("Kod Giriniz")
    if (kod == "1"):
        kisi = Kisi(0, input("Ad giriniz"), input("soyad giriniz"),
                    input("tel giriniz"), input("adres giriniz"))
        kisi.kisi_db_ekle()
    elif (kod == "2"):
        kisi_list = getKisiList()
        for kisi in kisi_list:
            print("{} id numara kişi : {}".format(
                kisi.id, kisi.ad+" "+kisi.soyad))

        randevu = Randevu(0, input("Kişi id giriniz"),
                          input("saat"), input("tarih"))
        randevu.randevu_db_ekle()
    elif (kod == "3"):
        print("Randevu Listesi")
        randevu_list = getRandevuList()
        for randevu in randevu_list:
            print("{} id'li randevu {} {}".format(
                randevu.id, randevu.tarih, randevu.saat))
        id = input("Silinecek randevu idsini giriniz")
        silinecek_randevu = None
        for randevu in randevu_list:
            if randevu.id == int(id):
                silinecek_randevu = randevu
                break
        silinecek_randevu.randevu_db_sil()
    elif (kod == "4"):
        pass
    elif (kod == "5"):
        pass
    elif (kod == "6"):
        pass
    elif (kod == "7"):
        print("Program Sonlandı")
        break
    else:
        print("Hatalı Kod girdiniz")
