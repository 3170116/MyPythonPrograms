def det(a):
    if len(a) == 2:
        return a[0][0]*a[1][1] - a[1][0]*a[0][1]
    else:
        d = 0
        for times in range(len(a)):
            newDet = det(sub(a,times))
            d += ((-1)**times)*a[0][times]*newDet
        return d


def sub(a,j):
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
