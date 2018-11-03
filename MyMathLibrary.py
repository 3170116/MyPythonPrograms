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

def nrt(number, power):
    if power == 1:
        return number
    if power == 0:
        return 1
    def f(x):
        return x**(power) - number
    result = BolzanoMethod(f,0,number,10**(-5))
    if (int(result) + 1)**(power) == number:
        return int(result) + 1
    if (int(result))**(power) == number:
        return int(result)
    return result

def integral(f, a, b):
    k = (b-a)/10**5
    result = f(a)
    for i in range(1,10**5 + 1):
        result += k*f(a + i*k)
    return result

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

class Poly:
    def __init__(self, numbers = [0]):
        self.numbers = numbers

    def __add__(self, poly):
        pass

    def __call__(self,number):
        return self.value(number)

    def __str__(self):
        return str(self.numbers)

    def __len__(self):
        return len(self.numbers)

    def __getitem__(self, i):
        return self.numbers[i]

    def roots(self, poly):
        if len(poly) == 3:#ax^2+bx+c
            if (poly[1]**2) - 4*poly[0]*poly[2] == 0:
                return -poly[1]/(2.0*poly[0])
            elif poly[1]**2 - 4*poly[0]*poly[2] > 0:
                d = math.sqrt(poly[1]**2 - 4*poly[0]*poly[2])
                x0 = (-poly[1] + d)/(2.0*poly[0])
                x1 = (-poly[1] - d)/(2.0*poly[0])
                return x0,x1
            else:
                return None
        elif len(poly) == 2:#ax+c
            return -poly[1]/poly[0]
        elif len(poly) == 1:#c
            if poly[0] == 0:
                return 0
            return None
        else:#ax^3,ax^4...
            roots = []
            extremes = list(self.roots(poly.d()))
            if poly.value(extremes[0])*poly[0] < 0:#a*poly(exMax) < 0
                i = 1
                while poly.value(extremes[0])*poly.value(extremes[0] + i) > 0:
                    i += 1
                roots.append(BolzanoMethod(poly,extremes[0],extremes[0]+i,10**(-5)))
            if (-1)*poly.value(extremes[len(extremes)-1])*poly[0] < 0:#-a*poly(exMin) < 0
                i = 1
                while poly.value(extremes[len(extremes)-1])*poly.value(extremes[0] - i) > 0:
                    i += 1
                roots.append(BolzanoMethod(poly,extremes[len(extremes)-1],extremes[0]-i,10**(-5)))
            for i in range(len(extremes)-1):#ex1*ex2 < 0
                if poly(extremes[i])*poly(extremes[i+1]) < 0:
                    roots.append(BolzanoMethod(poly,extremes[i],extremes[i+1],10**(-5)))
            return roots
                        
    def value(self,x0):
        if len(self.numbers) == 1:
            return self.numbers[0]
        elif len(self.numbers) > 1:
            result = self.numbers[0]
            for number in range(1,len(self.numbers)):
                result = result*x0 + self.numbers[number]
            return result

    def d(self):
        if len(self.numbers) > 1:
            numbers = []
            for i in range(len(self.numbers)-1):
                numbers.append(self.numbers[i]*(len(self.numbers)-1-i))
            return Poly(numbers)
        return Poly()

    def integral(self, a, b):
        inte = self.indefiniteIntegral()
        return inte.value(b) - inte.value(a)

    def indefiniteIntegral(self):
        pass
