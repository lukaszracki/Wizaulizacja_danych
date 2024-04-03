import math
import  random

def zad1():
    for i in range(25,40,1):
        wynik = (math.sin(i) + math.log(36,4))**(1/3)
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

def main():
    # zad1()
    zad2(1,10,5)

if __name__ == '__main__':
    main()