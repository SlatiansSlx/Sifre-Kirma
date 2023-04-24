mytitle = "> Şifre Deneniyor!"
from os import system
system("title "+mytitle)
import colorama
from colorama import Fore, Style
from random import choice, choice, choices

sayilar = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0, "vefa", "hazal")
sifre = str(input(f" > Kırılacak Şifreyi Giriniz: "))
sifres = ""
adim = 0
while True:
    print(f" > Şifreniz Deneniyor!", sifres)

    if sifre == sifres:
        break

    else:
        sifres = ""
        for i in range(4):
            sifres += str(choice(sayilar))
            adim += 1

print(f" > Şifreniz Kırılmıştır ", sifre, "adimda krilmis", adim)