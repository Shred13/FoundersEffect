from math import factorial as fac

def input_read(file):
    file1 = open(file, 'r')
    lines = file1.readlines()
    n, m = lines[0].split()
    n = int(n)
    m = int(m)
    a = [int(val) for val in lines[1].split()]
    return a, n, m


def wright_fisher(a, n, m):
    for i in range(m):
        p = "something"
        q = 1 - p
        res = (fac(2*n)/(fac(k)*fac((2*n)-k))) * (p**k) * (q**((2*n)-k))

    # ((2n!)/(k!*(2N-k)!))*(p**k)*(1-p**2N-k)


def main():
    a, n, m = input_read("data.txt")
    wright_fisher(a, n, m)