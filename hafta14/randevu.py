import sqlite3
from dbyardimci import select, insert, delete


def getRandevuList():
    baglanti = sqlite3.connect("veritabani.db")
    gelen = select(baglanti, "Select * from Randevu")
    randevu_list = []
    for db_randevu in gelen:
        randevu_ornek = Randevu(
            db_randevu[0], db_randevu[1],
            db_randevu[2], db_randevu[3])
        randevu_list.append(randevu_ornek)
    baglanti.close()
    return randevu_list


class Randevu:
    def __init__(self, id, kisiid, saat, tarih):
        self.id = id
        self.kisiid = kisiid
        self.saat = saat
        self.tarih = tarih

    def randevu_db_ekle(self):
        baglanti = sqlite3.connect("veritabani.db")
        insert(baglanti, "Randevu", ('kisiid',
               'saat', 'tarih'), (self.kisiid, self.saat, self.tarih))
        baglanti.close()

    def randevu_db_sil(self):
        baglanti = sqlite3.connect("veritabani.db")
        delete(baglanti, "Randevu", "id="+str(self.id))
        baglanti.close()
