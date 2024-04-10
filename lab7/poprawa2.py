import math
import random
import sys


def zad1():
    for i in range(25,40,1):
        wynik = (math.sin(i) + math.log(36,4))**(1/3)
        print(round(wynik,2))

def zad2(mini, maxi, ile, n):
    try:
        if ile <= 0:
            raise ValueError
        lista = []
        for i in range(ile):
            element = random.randint(mini, maxi)
            lista.append(element)
        print(lista)
        result_list = []
        if ile % n == 0:
            for i in range(0, len(lista), n):
                temp_list = []
                for j in range(i, i+n):
                    temp_list.append(lista[j])
                result_list.append(temp_list)
        return result_list
    except ValueError:
        return 'error'

def zad3(nazwa_pliku):
    with open(nazwa_pliku, 'r') as f:
        liczby = f.readlines()
    print(liczby)
    for i in range(len(liczby)):
        liczby[i] = liczby[i].replace('\n','').split(' ')
        print(liczby[i])
    lista = []
    for i in range(len(liczby[0])):
        temp = []
        for j in range(len(liczby)):
            temp.append(int(liczby[j][i]))
        lista.append(temp.index(min(temp)))
    return lista

def zad4():
    try:
        a = int(sys.stdin.readline())
        h = int(sys.stdin.readline())
        if a<=0 or h<=0:
            raise ValueError
        ob = a*a*h
        return ob
    except ValueError:
        return 'error'

def main():
    # zad1()
    # print(zad2(1,10,6, 3))
    # zad3('liczby.txt')
    print(zad4())

if __name__ == '__main__':
    main()