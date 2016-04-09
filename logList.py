from tkinter import *
import sqlite3
import datetime

def visited():

        path = "/home/laylay/.mozilla/firefox/x84ynd72.default/places.sqlite"
        connection = sqlite3.connect(path)
        cur = connection.cursor()


        cur.execute('SELECT url, last_visit_date FROM moz_places ORDER BY id DESC')

        """veriler = cur.fetchmany(10)"""       #Son 10 kaydı alır
        """veriler = cur.fetchall() """         #Tüm kayıtları alır

        """
        pi=li[0]
        print(li)
        print(pi)
        """

        pencere = Tk()
        pencere.title(u"Browser Logger")
        pencere.geometry("650x300+80+80")

        karsilama = Label(pencere)
        karsilama.config(text = u"\nTutulan Web Geçmişi.\n\n")
        karsilama.pack()

        kayit = Listbox(pencere)
        kayit.pack(fill="both")

        for i in range(10):
                veriler = cur.fetchone()
                li= list(veriler)            #tuple to list
                s = '1346114717972'
                t = datetime.datetime.fromtimestamp(float(li[1])/1000000.)
                fmt = "%Y-%m-%d %H:%M:%S"
                print (t.strftime(fmt))
                li[1]=(t.strftime(fmt))
                print(li)
                kayit.insert(END,li)


        mainloop()




