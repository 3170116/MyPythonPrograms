def BolzanoMethod(f, a, b, e):
    c = a + (b-a)/2.0
    if b - c <= e or f(c) == 0:
        return c
    else:
        if sign(f(a))*sign(f(c)) < 0:
            return BolzanoMethod(f,a,c,e)
        else:
            return BolzanoMethod(f,c,b,e)

def sign(number):
    if number < 0:
        return -1
    else:
        return 1


def sqrt(number):
    def f(x):
        return x**2 - number
    return BolzanoMethod(f,0,number,10**(-5))

def det(a):
    if len(a) == 2:
        return a[0][0]*a[1][1] - a[1][0]*a[0][1]
    else:
        d = 0
        for times in range(len(a)):
            d += ((-1)**times)*a[0][times]*det(__sub(a,times))
        return d


def __sub(a,j):
    b = []
    for i in range(len(a)-1):
        arr = []
        for k in range(len(a)):
            arr.append(a[i+1][k])
        b.append(arr)
    size = len(b)
    for times in range(size):
        del b[times][j]
    return b

def josephus(aList,start,step):
    if len(aList) == 1:
        return aList[0]
    else:
        position = (start+step)%len(aList)
        del aList[position]
        if position == 0:
            return josephus(aList,len(aList)-1,step)
        else:
            return josephus(aList,position - 1,step)
