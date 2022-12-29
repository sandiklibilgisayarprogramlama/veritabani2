import sqlite3
from dbyardimci import select, insert, delete


def getKisiList():
    baglanti = sqlite3.connect("veritabani.db")
    gelen = select(baglanti, "Select * from Kisi")
    kisi_list = []
    for db_kisi in gelen:
        kisi_ornek = Kisi(db_kisi[0], db_kisi[1], db_kisi[2],
                          db_kisi[3], db_kisi[4])
        kisi_list.append(kisi_ornek)
    baglanti.close()
    return kisi_list


class Kisi:
    def __init__(self, id, ad, soyad, tel, adres):
        self.id = id
        self.ad = ad
        self.soyad = soyad
        self.tel = tel
        self.adres = adres

    def kisi_db_ekle(self):
        baglanti = sqlite3.connect("veritabani.db")
        insert(baglanti, "Kisi", ('ad', 'soyad',
               'tel', 'adres'), (self.ad, self.soyad, self.tel, self.adres))
        baglanti.close()

    def kisi_db_sil(self):
        baglanti = sqlite3.connect("veritabani.db")
        delete(baglanti, "Kisi", "id="+str(self.id))
        baglanti.close()
