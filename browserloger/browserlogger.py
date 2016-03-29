import csv, sqlite3, os
from datetime import datetime, timedelta
from tkinter import *
bilgiler = ("demo", "demo")
def girisYap():

    kAdi = isim.get()
    parola = sifre.get()
    print ( kAdi, " - ", parola )
    print ("Kontrol ediliyor ...")
    if kAdi == bilgiler[0] and parola == bilgiler[1]:
        print ("Bilgiler dogru!")
        sonuc.config(text = u"Oturum acma islemi basarili.")
        home = os.path.expanduser("~")
        os.system('taskkill /f /im chrome.exe')
        path = home+"\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\History"
        connection = sqlite3.connect(path)
        connection.text_factory = str
        cur = connection.cursor()
        output_file = open("chrome_history.csv", 'w')
        csv_writer = csv.writer(output_file)
        headers = ('BROWSER LOGGER', '')
        csv_writer.writerow(headers)
        epoch = datetime(1601, 1, 1)
        for row in (cur.execute('SELECT url FROM urls ORDER BY last_visit_time DESC')):
            row = list(row)
            csv_writer.writerow(row)
            
    else:
        print ("Bilgiler yanlis!")
    pass

pencere = Tk()


pencere.title(u"Browser Logger")
pencere.geometry("290x200+100+100")

karsilama = Label(pencere)
karsilama.config(text = u"Hosgeldiniz, lutfen giris yapiniz.")
karsilama.pack()

isimSor = Label(pencere)
isimSor.config(text = u"Kullanici Adi:")
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
buton.pack()

sonuc = Label(pencere)
sonuc.config(text = u"Giris yapilmadi.")
sonuc.pack()
mainloop ()
