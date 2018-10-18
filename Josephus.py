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