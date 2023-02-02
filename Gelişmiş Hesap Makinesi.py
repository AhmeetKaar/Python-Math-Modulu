import time

print("""
************************************************
Proje 1 
Math modülündeki hazır fonksiyonları kullanarak
gelişmiş bir hesap makinesi geliştirmeye çalışın.

*************************************************
""")

print("""

Hesap Makinesi Bilgileri;

1.Toplama İşlemi
 
2.Çıkarma İşlemi
 
3.Çarpma İşlemi

4.Bölme İşlemi 

5.Faktoriyel İşlemi

6.Logaritma İşlemi

7.Sayı Dizisindeki En Yüksek Değer

8.Sayı Dizisindeki En Düşük Değer

9.Sayının Mutlak Değerini Al

10.Sayının İstenilen Üssünü Al

11.Sayının Karekökünü Al

12.Pi Sayısını Al

13.Sayıları Kendine En Yakın Sayılara Yuvarla

14.İki Sayının İşaretini Değiştir

15.İki Sayının Bölümünden Kalanını Bul

16.Sayının Ebobunu Bul

17.Sayının İki Tabanında Logaritaması Al

18.Sayının On Tabanında Logaritması Al

19.Verilen Sayı Radyandan Dereceye Çevir

20.Verilen Sayı Dereceden Radyan Çevir

""")

import math

from math import *

islem = input("Lütfen Bir İşlem Giriniz:")



if islem == "1":
    a = int(input("Lütfen Tam Sayı Giriniz:"))

    b = int(input("Lütfen Tam Sayı Giriniz:"))

    print("Sayılar Toplanıyor...")
    time.sleep(1)
    print("{} ile {} 'nin toplamı {}'dir.".format(a, b, a + b ))

elif islem == "2":
    a = int(input("Lütfen Tam Sayı Giriniz:"))

    b = int(input("Lütfen Tam Sayı Giriniz:"))

    print("Sayılar Çıkartılıyor...")
    time.sleep(1)
    print("{} ile {} 'nin farkı {}'dir.".format(a, b, a - b))

elif islem == "3":
    a = int(input("Lütfen Tam Sayı Giriniz:"))

    b = int(input("Lütfen Tam Sayı Giriniz:"))

    print("Sayılar Çarpılıyor...")
    time.sleep(1)
    print("{} ile {} 'nin çarpımı {}'dir.".format(a, b, a * b))

elif islem == "4":
    a = int(input("Lütfen Tam Sayı Giriniz:"))

    b = int(input("Lütfen Tam Sayı Giriniz:"))

    print("Sayılar Bölünüyor...")
    time.sleep(1)
    print("{} ile {} 'nin bölümü {}'dir.".format(a, b, a // b))

elif islem == "5":
    b = int(input("Lütfen Tam Sayı Giriniz:"))

    print("Sayının Faktoriyeli Bulunuyor...")
    time.sleep(1)
    print(factorial(b))

elif islem == "6":
    a = int(input("Lütfen Tam Sayı Giriniz:"))

    print("Sayının Logaritması Alınıyor..")
    time.sleep(1)
    print(log(a))

elif islem == "7":
    a = int(input("Lütfen Tam Sayı Giriniz:"))

    b = int(input("Lütfen Tam Sayı Giriniz:"))

    print("Sayı Dizesindeki En Yüksek Sayı Bulunuyor...")
    time.sleep(1)
    print(max(a,b))

elif islem == "8":
    a = int(input("Lütfen Tam Sayı Giriniz:"))

    b = int(input("Lütfen Tam Sayı Giriniz:"))

    print("Sayı Dizesindeki En Düşük Sayı Bulunuyor...")
    time.sleep(1)
    print(min(a,b))

elif islem == "9":
    a = int(input("Lütfen Tam Sayı Giriniz:"))

    print("Sayının Mutlak Değeri Alınıyor...")
    time.sleep(1)
    print(abs(a))

elif islem == "10":
    a = int(input("Lütfen Tam Sayı Giriniz:"))

    b = int(input("Lütfen Tam Sayı Giriniz:"))

    print("Sayının İstenilen Üssü Alınıyor...")
    time.sleep(1)
    print(pow(a,b))

elif islem == "11":
    a = int(input("Lütfen Tam Sayı Giriniz:"))

    print("Sayının Karekökü Alınıyor...")
    time.sleep(1)
    print(sqrt(a))

elif islem == "12":

    print("Sayının Pi Sayısı Alınıyor...")
    time.sleep(1)
    x = math.pi
    print(x)

elif islem == "13":
    c = float(input("Lütfen Ondalıklı Bir Sayı Giriniz:"))

    print("Sayılar,Kendine En Yakın Tam Sayılara Yuvarlanıyor...")
    time.sleep(1)
    print(ceil(c))
    print(floor(c))

elif islem == "14":
    a = int(input("Lütfen Tam Sayı Giriniz:"))

    b = int(input("Lütfen Tam Sayı Giriniz:"))

    print("Sayıların İşaretleri Değiştiriliyor...")
    time.sleep(1)
    print(copysign(a,b))

elif islem == "15":
    a = int(input("Lütfen Tam Sayı Giriniz:"))

    b = int(input("Lütfen Tam Sayı Giriniz:"))

    print("Bölüm İşleminden Kalan Sayı Bulunuyor")
    time.sleep(1)
    print(fmod(a,b))

elif islem == "16":
    a = int(input("Lütfen Tam Sayı Giriniz:"))

    b = int(input("Lütfen Tam Sayı Giriniz:"))

    print("Sayıların Ebobu Alınıyor...")
    time.sleep(1)
    print(gcd(a,b))

elif islem == "17":
    a = int(input("Lütfen Tam Sayı Giriniz:"))

    print("Sayının İki Tabanında Logaritaması Alınıyor..")
    time.sleep(1)
    print(log2(a))

elif islem == "18":
    a = int(input("Lütfen Tam Sayı Giriniz:"))

    print("Sayının On Tabanında Logaritması Alınıyor...")
    time.sleep(1)
    print(log10(a))

elif islem == "19":
    a = int(input("Lütfen Tam Sayı Giriniz:"))

    print("Verilen Sayı Radyandan Dereceye Çevriliyor...")
    time.sleep(1)
    print(degrees(a))

elif islem == "20":
    a = int(input("Lütfen Tam Sayı Giriniz:"))

    print("Verilen Sayı Dereceden Radyan Çevriliyor..")
    time.sleep(1)
    print(radians(a))

else :
    print("GEÇERSİZ İŞLEM!!")



























































