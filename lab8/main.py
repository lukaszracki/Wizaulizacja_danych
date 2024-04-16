import numpy as np

# a = np.arange(12).reshape((3,4))
# print(a)
# print(a.sum())
# print(a.sum(axis=0))
# print(a.min(axis=1))
# print(a.cumsum(axis=1))

# b = np.arange(3)
# print(b)
# print(np.exp(b))
# print(np.sqrt(b))
# c = np.array([2., -1., 4.])
# print(np.add(b,c))

# a = np.arange(6).reshape((3,2))
# print(a)
# for b in a:
#     print(b)
#     print("")
#
# a = np.arange(6).reshape((3,2))
# print(a)
# for b in a.flat:
#     print(b)
#     print("")

# c = np.arange(1,10)
# print(c)
# print(a.flat)

# a = np.arange(6)
# print(a)
# print(a.shape)
# print("")
# c = a.reshape((3,2))
# print(c)
# print(c.shape)
# print("")
# d = c.ravel()
# print(d)
# print(d.shape)
# print("")

def zad1():
    macierz1 = np.array([1, 2, 3])
    macierz2 = np.array([4, 5, 6])

    wynik = np.dot(macierz1, macierz2)

    print("Pierwsza macierz:", macierz1)
    print("Druga macierz:", macierz2)
    print("Wynik mnożenia:", wynik)

def zad2():
    macierz1 = np.arange(9).reshape((3,3))
    macierz2 = np.arange(16).reshape((4,4))

    print(f'Najmniejsze wartosci dla kolumn w macierzy 3x3 {np.min(macierz1, axis=0)}')
    print(f'Najmniejsze wartosci dla wierszy w macierzy 3x3 {np.min(macierz1, axis=1)}')
    print(f'Najmniejsze wartosci dla kolumn w macierzy 4x4 {np.min(macierz2, axis=0)}')
    print(f'Najmniejsze wartosci dla wierszy w macierzy 4x4 {np.min(macierz2, axis=1)}')

def zad3():
    macierz1 = np.array([1, 2, 3])
    macierz2 = np.array([4, 5, 6])



def main():
    # zad1()
    # zad2()
    zad3()

if __name__ == '__main__':
    main()
