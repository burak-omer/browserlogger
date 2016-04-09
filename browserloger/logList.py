from tkinter import *
import sqlite3


def visited():

        path = "/home/byk/.mozilla/firefox/mwad0hks.default/places.sqlite"
        connection = sqlite3.connect(path)
        cur = connection.cursor()


        cur.execute('SELECT url, last_visit_date, visit_count FROM moz_places ORDER BY id DESC')

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
                url= li[0]                   #deneme amaçlı url,date,count
                date= li[1]
                count = li[2]
                print(li)
                kayit.insert(END,li)


        mainloop()




