import subprocess

#Browseri açmadan önce aktifleştir.



def aktif():
    output = ""
    while (output != "firefox"):
        output = subprocess.getoutput("ps aux")
        if "firefox" in output:
            subprocess.getoutput("killall -9 firefox")
            #Açık olan browser pencerelerini kapatır.
            from browserlogger.kontrolet import girisYap
            
        else:
            pass

aktif()
