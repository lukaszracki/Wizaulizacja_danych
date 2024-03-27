import  numpy as np

# a = np.arange(2)
# print(a)
#
# a = np.array([0, 1])
# print(a)
# print(type(a))
# print(a.dtype)
#
# a = np.arange(2, dtype='int64')
# print(a.dtype)
#
# b = a.astype('float')
# print(b)
# print(b.dtype)
# print(b.shape)
#
# print(a.ndim)
#
# m = np.array([np.arange(2), np.arange(2)])
# print(m.shape)
# print(type(m))

# zera = np.zeros((5,5))
# jedynki = np.ones((4,4))
# print(zera)
# print(jedynki)
# print(zera.dtype)
# print(jedynki.dtype)

# pusta = np.empty((2,2))
# print(pusta)
#
# poz1 = pusta[1,1]
# poz2 = pusta[0,1]
# print(poz1)
# print(poz2)

# macierz = np.array([[1,2],[3,4]])
# print(macierz)

# liczby = np.arange(1,2,0.1)
# print(liczby)

# liczby_lin = np.linspace(1,2,5)
# print(liczby_lin)

# z = np.indices((5,3))
# print(z)

# x,y = np.mgrid[0:5, 0:5]
# print(x)
# print(y)

# mat_diag = np.diag([a for a in range(5)])
# print(mat_diag)

# mat_diag_k = np.diag([a for a in range(5)],-1)
# print(mat_diag_k)

# z = np.fromiter(range(5), dtype='int32')
# print(z)

def zad1():
    a = np.arange(3,46,3)
    print(a)

def zad2():
    a = np.array([1.2,3.4,5.6,7.8,9.0])
    print(a)
    print(a.dtype)
    b = a.astype('int64')
    print(b)
    print(b.dtype)

def zad3(n):
    a = np.ones((n,n))
    x = 1
    for i in range(0,n):
        for j in range(0,n):
            a[i][j] = x
            x += 1
    print(a)

def zad4(x,y):
    a = np.logspace(1,y,num=y,base=x)
    print(a)

def zad5(x):
    a = np.linspace(x,1,x)
    d = np.diag(a)
    print(d)

def zad7(n):
    x = np.diag(np.ones((n))*2)
    for i in range(n):
        x += np.diag(np.ones((n - i))*2*i,-i)
        x += np.diag(np.ones((n - i)) * 2 * i, i)
    print(x)

def zad9():
    def fibonacci(n):
        fib = [1, 1]
        for i in range(2, n):
            fib.append(fib[i - 1] + fib[i - 2])
        return fib

    def macierz_fib(n):
        fib_sequence = fibonacci(n ** 2)
        macierz = np.array(fib_sequence[:n ** 2]).reshape((n, n))
        return macierz

    print(macierz_fib(5))

def main():
    # zad1()
    # zad2()
    # zad3(5)
    # zad4(2,4)
    # zad5(5)
    # zad7(10)
    zad9()


if __name__ == '__main__':
    main()