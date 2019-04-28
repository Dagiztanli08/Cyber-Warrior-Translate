from googletrans import Translator
import pyperclip
import sqlite3
from time import sleep
from subprocess import check_call
from os import name as osnames

def baslangic():
    print("""
OFFLİNE-ONLİNE
    TRANSLATOR.
        CODED FOR CYBER-WARRİOR
            DAĞIZTANLI08.
   
! (Eğer cümle kopyalarsanız cevap vermiyecektir(sadece kelime))
! (if you copy sentence this program doesn't answer.(only word)).
Twitter = 08Ztanl
""")

baslangic()
sleep(0.3)

m = sqlite3.connect("ceviri.db")
m.cursor().execute("CREATE TABLE IF NOT EXISTS EMRE('kelime','ceviri')")


def veri_ekle(value1,value2):
    m_2 = m.cursor()
    m_2.execute("INSERT INTO EMRE(kelime,ceviri) SELECT '{}','{}' WHERE NOT EXISTS(SELECT * FROM EMRE WHERE kelime = '{}' AND ceviri = '{}')".format(a,c,a,c))
    m.commit()
def veri_cekme(value_1):
    m_2 = m.cursor()
    m_2.execute("select * from EMRE where kelime = '{}'".format(value_1))
    l = m_2.fetchall()
    return(l)

a = ""
while True:
    c = pyperclip.paste()
    if " " in c and len(c) > 16:
        continue
    elif c != a:
        a = c
        if len(veri_cekme(a)) != 0:
            if osnames == "posix":
                s_1 = check_call("notify-send '{}' '{}'".format("ÇIKTI",veri_cekme(a)), shell = True)
            print(veri_cekme(a),"Databaseden alındı.")
        else:
            try:
                c = Translator().translate(a,dest='tr').text
                if osnames == "posix":
                    s_1 = check_call("notify-send '{}' '{}'".format(a,c), shell = True) 
                print("{} == {}  /////// İnternet kullanıldı".format(a,c))
                veri_ekle(a,c)
            except __import__('requests').exceptions.ConnectionError:
                print("İnternet bağlantısı olmayabilir.")
