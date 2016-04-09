from tkinter import *
import subprocess


def girisYap():

    kAdi = isim.get()
    parola = sifre.get()
    user = ("user", "user")
    admin = ("admin", "admin")
    print ( kAdi, " - ", parola )
    print ("Kontrol ediliyor ...")
    if kAdi == user[0] and parola == user[1]:
        print ("Bilgiler dogru!")
        sonuc.config(text = u"Oturum acma islemi basarili.")
        subprocess.Popen("firefox",shell=True,stdout=subprocess.PIPE)
    elif kAdi == admin[0] and parola == admin[1]:
        print ("Bilgiler dogru!")
        sonuc.config(text = u"Oturum acma islemi basarili.")
        import adminpanel

    else:
        print ("Bilgiler yanlis!")
    pass




def durdur():
    exit()

def log():
    from browserlogger.logList  import visited
    visited()


pencere = Tk()


pencere.title(u'Browser Logger/User Login')
pencere.geometry("300x350+100+100")

karsilama = Label(pencere)
karsilama.config(text = u"\nHoş geldiniz sayın misafir\n")
karsilama.pack()

karsilama = Label(pencere)
karsilama.config(text = u"Web browserı açabilmek için\nLütfen aşağıdaki biligleri doldurunuz\n ")
karsilama.pack()


isimSor = Label(pencere)
isimSor.config(text = u"\nKullanici Adi:")
isimSor.pack()

isim = Entry(pencere)
isim.pack()

sifreSor = Label(pencere)
sifreSor.config(text= u"Sifreniz:")
sifreSor.pack()

sifre = Entry(pencere)
sifre.pack()

buton = Button(pencere)
buton.config(text = u"Giris yap!", command = girisYap)
buton.pack(pady=5)

sonuc = Label(pencere)
sonuc.config(text = u"Giris yapilmadi.")
sonuc.pack(pady=5)

butondur = Button(pencere)
butondur.config(text = u"Programı Durdur!", command = durdur)
butondur.pack(pady=2,fill="x")

butonlog = Button(pencere)
butonlog.config(text = u"Log Kayıtlarını Aç!", command = log )
butonlog.pack(pady=2,fill="x")

mainloop ()
