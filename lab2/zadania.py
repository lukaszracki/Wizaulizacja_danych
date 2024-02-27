import  sys

def zad1():
    napis = str(input('Napisz jakis zdanie: '))
    spacje = 0
    for i in napis.split():
        if ' ' in napis:
            spacje += 1
    print(f'ilosc slow w zdaniu: {spacje}')


def zad2():
    sys.stdout.write('Wprowadz 1 liczbe: ')
    a = int(sys.stdin.readline())
    sys.stdout.write('Wprowadz 2 liczbe: ')
    b = int(sys.stdin.readline())
    sys.stdout.write('Wprowadz 3 liczbe: ')
    c = int(sys.stdin.readline())

    print(pow(a,b)+c)


def zad3():
    #do dokonczenia
    lista = []
    napis = input('wprowadz slowo: ')
    lista.append(napis)


def zad4():
    liczba = int(input('podaj liczbe: '))
    licznik = 2
    while licznik < liczba:
        if liczba % licznik == 0:
            print(f'{liczba} nie jest pierwsza')
            break
        licznik += 1
    else:
        print(f'{liczba} jest pierwsza')


def zad6():
    lista = [1,2.3,4,5,6.7,8]
    n = 0
    for i in lista:
        lista[n] = i**2
        n += 1
    print(lista)


def zad7():
    lista = []
    licznik = 1
    while licznik <= 10:
        liczba = int(input(f'Podaj {licznik} liczbe: '))
        if liczba % 2 == 0:
            lista.append(liczba)
        licznik += 1
    print(lista)

# zad1()
# zad2()
# zad3()
# zad4()

# zad6()
# zad7()