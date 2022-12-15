import sqlite3
# select * from personel where id=10, like, between


def select(baglanti, sorgu):
    imlec = baglanti.cursor()
    imlec.execute(sorgu)
    gelen = imlec.fetchall()
    return gelen

# insert into tablo_ismi (degerler) values (yazılacaklar)


def insert(baglanti, tablo_ismi, degerler, yazilacaklar):
    imlec = baglanti.cursor()
    sorgu = "insert into "+tablo_ismi + " " + \
        str(degerler)+" values "+str(yazilacaklar)
    print(sorgu)
    imlec.execute(sorgu)
    baglanti.commit()

# update tablo set ad="ahmet" where id=10


def update(baglanti, tablo_ismi, guncellenecek, kosul):
    imlec = baglanti.cursor()
    sorgu = "update "+tablo_ismi + " set "+guncellenecek+" where "+kosul
    print(sorgu)
    imlec.execute(sorgu)
    baglanti.commit()

# delete fonksiyonunu yazınız id si 2 olan kişiyi siliniz.


def delete(baglanti, tablo_ismi, kosul):
    imlec = baglanti.cursor()
    sorgu = "delete from {} where {}".format(tablo_ismi, kosul)
    print(sorgu)
    imlec.execute(sorgu)
    baglanti.commit()
