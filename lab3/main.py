import math
import random

def zad1():
    a = [x for x in range(1,11)]
    print(a)
    b = [4**x for x in range(1,8)]
    print(b)
    c = [x for x in range(1,20) if x%2==0]
    print(c)

def zad2():
    lista1 = []
    for i in range(10):
        lista1.append(random.randint(1,100))
    lista2 = [x for x in lista1 if x%2==0]
    print(lista2)

def zad3():
    slownik = {
        "chleb": "bochenki",
        "jajka": "sztuki",
        "ziemniaki": "kilogramy",
        "gowno": "sztuki"
    }
    lista = {key: value for (key, value) in slownik if value == "sztuki" in slownik}
    print(lista)

def zad4():
    a = int(input("Podaj a:"))
    b = int(input("Podaj b:"))
    c = int(input("Podaj c:"))
    if a > b and a > c:
        if b**2 + c**2 == a**2:
            print('trojkat jest prostokatny')
        else:
            print('trojkat nie jest prostokatny')
    if b > a and b > c:
        if a**2 + c**2 == b**2:
            print('trojkat jest prostokatny')
        else:
            print('trojkat nie jest prostokatny')
    if c > a and c > b:
        if b**2 + a**2 == c**2:
            print('trojkat jest prostokatny')
        else:
            print('trojkat nie jest prostokatny')


def zad5(a=5,b=5,h=7):
    pole = ((a+b)*h)/2
    print(f'Pole trapezu o podanych wymiarach wynosi {pole}')

def zad6(a=1, b=4, ile=10):
    #nie jestem pewien czy na pewno dobrze
    wynik = 1
    for i in range(ile):
        wynik *= a
        a *= b
    print(wynik)

def zad7():
    liczba = int(input("Podaj liczbe calkowita: "))
    if liczba > 0:
        print(math.sqrt(liczba))
    else:
        print('Podales ujemna liczbe')

def main():
     zad1()
    # zad2()
    # zad3()
    # zad4()
    # zad5()
    # zad6()
    # zad7()


main()
