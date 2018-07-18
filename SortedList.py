class Node():
    def __init__(self, data, comparedData, nextNode = None, previousNode = None):
        self.data = data
        self.comparedData = comparedData
        self.nextNode = nextNode
        self.previousNode = previousNode

    def getData(self):
        return self.data

    def getComparedData(self):
        return self.comparedData

    def getNextNode(self):
        return self.nextNode

    def setNextNode(self, node):
        self.nextNode = node

    def getPreviousNode(self):
        return self.previousNode

    def setPreviousNode(self, node):
        self.previousNode = node

    def insert(self, obj):
        if self.comparedData < obj.getComparedData():
            if self.previousNode == None:
                self.previousNode = Node(obj,obj.getComparedData(),self)
            else:
                currentNode = self.previousNode
                while currentNode != None and currentNode.getComparedData() < obj.getComparedData():
                    currentNode = currentNode.getPreviousNode()
                helpNode = Node(obj,obj.getComparedData(),currentNode.getNextNode(),self)
                currentNode.getNextNode().setPreviousNode(helpNode)
                currentNode.setNextNode(helpNode)

        elif self.comparedData > obj.getComparedData():
            if self.nextNode == None:
                self.nextNode = Node(obj,obj.getComparedData(),None,self)
            else:
                currentNode = self.nextNode
                while currentNode != None and currentNode.getComparedData() > obj.getComparedData():
                    currentNode = currentNode.getNextNode()
                helpNode = Node(obj,obj.getComparedData(),currentNode.getNextNode(),self)
                currentNode.getPreviousNode().setNextNode(helpNode)
                currentNode.setPreviousNode(helpNode)


class SortedList():
    def __init__(self,class_Type):
        self.class_Type = class_Type
        self.firstNode = None
        self.lastNode = None
        self.size = 0

    def size(self):
        return self.size

    def add(self, obj):
        if type(obj) is self.class_Type:
            if self.firstNode == None:
                self.firstNode = self.lastNode = Node(obj,obj.getComparedData())
            else:
                self.firstNode.insert(obj)

    def clear(self):
        self.firstNode = self.lastNode = None

    def remove(self,place):
        if place < self.size and place >= 0:
            counter = 0
            currentNode = self.firstNode
            while counter != place:
                currentNode = currentNode.getNextNode()
                counter += 1
            currentNode.getPreviousNode().setNextNode(currentNode.getNextNode())
            if place != self.size - 1:
                currentNode.getNextNode().setPreviousNode(currentNode.getPreviousNode())
            if self.firstNode == currentNode:
                self.firstNode = self.lastNode = None
            if self.lastNode == currentNode:
                self.lastNode = currentNode.getPreviousNode()
            currentNode = None #μπορεί να μην χρειάζεται

    def toList(self):
        objectsList = []
        currentNode = self.firstNode
        for i in range(self.size):
            objectsList.append(currentNode.getData())
            currentNode = currentNode.getNextNode()
        return objectsList
