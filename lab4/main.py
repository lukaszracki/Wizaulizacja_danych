import math
import random

def zad1():
    wynik1 = ((math.e)**4 - math.log(34,2))**(1/3)
    print(round(wynik1,2))
    wynik2 = (math.log(20) + math.cos(45) + math.e)**(1/3)
    print(round(wynik2,2))
    wynik3 = (math.log(20,3) + math.sin(45) * (5/8))**(1/4)
    print(round(wynik3,2))
    wynik4 = math.log(23,3) + (math.sin(34) + 5)**(1/3)
    print(round(wynik4,2))
    wynik5 = (math.log(32,2) + math.pi + math.sin(56))**(1/4)
    print(round(wynik5,2))

def zad2():
    wysokosc = int(input('Podaj wysokosc wiezy: '))
    if wysokosc > 10:
        print('Wieza nie moze byc wieksza niz 10')
    else:
        for i in range(wysokosc+1):
            print("A"*i)

def zad3():
    n = int(input("Wybierz wysokosc piramidy: "))
    for i in range(1, n + 1):
        print(" " * (n - i) + "A" * i + 'A' * (i - 1))
        if n > 10:
            print("Piramida nie moze byc wyzsza niz 10")
            break

def wektor():
    n = int(input("Podaj liczbe n: "))
    macierz = []
    for i in range(n):
        wiersz = [random.randint(1,10) for i in range(n)]
        macierz.append(wiersz)
    suma_wierszy = [sum(wiersz) for wiersz in macierz]

    print('Macierz: ')
    print(macierz)
    print('Wynik dodawania wierszy macierzy: ')
    print(suma_wierszy)


def zad4():
    a = int(input('Podaj liczbe a: '))
    b = int(input('Podaj liczbe b: '))
    napis = str(a**b)
    print(f'Liczba {a} podniesiona do potegi {b} wynosi: {a**b}')
    print(f'Dlugosc wyniku {a**b} to {len(str(a**b))}')
    print(f'Ostatnia liczba wyniku {a**b} to {napis[-1]}')


def main():
    # zad1()
    # zad2()
    # zad3()
    # wektor()
    zad4()


main()
