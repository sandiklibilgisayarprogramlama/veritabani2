import sqlite3


# veri tabanına bağlanmak
# imlec(cursor)
# sorgu (query)
# execute -> tablo oluşturma, select
# commit -> veri yazma, güncelleme
# close

"""
baglanti = sqlite3.connect("db.db")
imlec = baglanti.cursor()

sorgu = 
create table pastane ( 
    id integer primary key autoincrement,
    urunad text not null,
    urunadet integer not null);


imlec.execute(sorgu)
baglanti.close()

sorgu = "select * from pastane"
imlec.execute(sorgu)  # sorgunun çalıştırıldığı yer
gelen = imlec.fetchall()  # verilerin alındıgı yer
print(gelen)


sorgu = "insert into pastane (urunad,urunadet) values('Yaş Pasta',20)"
imlec.execute(sorgu)
baglanti.commit()
baglanti.close()


sorgu = "update pastane set urunad='Poğaça' where id=2"
imlec.execute(sorgu)
baglanti.commit()
baglanti.close()


sorgu = "delete from pastane where id=2"
imlec.execute(sorgu)
baglanti.commit()
baglanti.close()

from dbyardimci import select, insert
baglanti = sqlite3.connect("db.db")
veriler = select(baglanti, "select * from pastane")
print(veriler)
insert(baglanti, "pastane", ('urunad', 'urunadet'), ('Yaş Pasta', 30))
veriler = select(baglanti, "select * from pastane")
print(veriler)
baglanti.close()

from dbyardimci import select, insert, update, delete
baglanti = sqlite3.connect("db.db")
veriler = select(baglanti, "select * from pastane")
print(veriler)
delete(baglanti, "pastane", "id=1")
veriler = select(baglanti, "select * from pastane")
print(veriler)
baglanti.close()

pastane tablosuna yeni bir kayıt ekleyin.


"""
from dbyardimci import insert, select, update
baglanti = sqlite3.connect("db.db")
update(baglanti, "pastane", "urunad='tost'", "urunad='simit'")
gelen = select(baglanti, "select * from pastane")
print(gelen)
baglanti.close()
