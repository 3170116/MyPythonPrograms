class ListTree():
    def __init__(self):
        self.__items = []
        self.__removedItems = 0

    def add(self, item):
        if len(self.__items) != 0:
            cmpItem = self.__items[0] #ριζα
            while cmpItem[1] > 0 or cmpItem[2] > 0: #οσο υπαρχουν παιδιά
                if item < cmpItem[0] and cmpItem[1] > 0:
                    cmpItem = self.__items[cmpItem[1]]
                elif item > cmpItem[0] and cmpItem[2] >0:
                    cmpItem = self.__items[cmpItem[2]]
                else:
                    break
            
            if item < cmpItem[0]:
                cmpItem[1] = len(self.__items)
            else:
                cmpItem[2] = len(self.__items)
            self.__items.append([item,-1,-1])
        else:
            self.__items.append([item,-1,-1]) #item,left,right

    def remove(self,item):
        pass

    def get(self, place):
        pass

    def contains(self, item):
        cmpItem = self.__items[0]
        while item != cmpItem[0] and (cmpItem[1] > 0 or cmpItem[2] > 0):
            if item < cmpItem[0]:
                cmpItem = self.__items[cmpItem[1]]
            else:
                cmpItem = self.__items[cmpItem[2]]
        if item == cmpItem[0]:
            return True
        return False

    def clear():
        self.__items = []
        self.__removedItems = 0

    def size(self):
        return len(self.__items)

    def isEmpty(self):
        return len(self.__items) == 0
