import math
import random


def zad1():
    for i in range(13,29,1):
        wynik = (math.e**i + math.cos(i))**(1/4)
        print(round(wynik,2))

def zad2(mini, maxi, ile):
    lista = []
    if mini > maxi:
        print('error')
    else:
        for i in range(ile):
            lista.append(random.randint(mini,maxi))
    print(f'Wygenerowana lista: {lista}')
    slownik = {}
    for i in range(ile):
        x = 0
        for j in range(ile):
            if lista[i] == lista[j]:
                x += 1
        slownik[lista[i]] = x
    print(f'Wygenerowany slownik: {slownik}')


def zad3(nazwa_pliku):
    suma_wierszy = 0
    suma_kolumn = 0
    try:
        with open(nazwa_pliku, 'r') as file:
            lines = file.readlines()
            for line in lines:
                suma_wierszy += sum(map(int, line.split()))

            for col in range(len(lines[0].split())):
                suma_kolumn += sum(int(line.split()[col]) for line in lines)

    except FileNotFoundError:
        print("Plik o nazwie", nazwa_pliku, "nie został znaleziony.")
        return None

    return suma_wierszy, suma_kolumn

def zad4(a,h):
    if a <= 0 or h <= 0:
        print('error')
    else:
        objetosc = ((a**2)*h)/3
        print(f'Objetosc wynosi: {objetosc}')


def main():
    # zad1()
    # zad2(1,10,5)
    # print(zad3('liczby.txt'))
    zad4(6,18)

if __name__ == '__main__':
    main()