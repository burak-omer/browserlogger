import subprocess

#Browseri açmadan önce aktifleşir.
#Açık olan browser pencerelerinide kapatır.


def aktif():
    output = ""
    while (output != "firefox"):
        output = subprocess.getoutput("ps aux")
        if "firefox" in output:
            subprocess.getoutput("killall -9 firefox")
            from browserlogger.kontrolet import girisYap

        else:
            pass

aktif()