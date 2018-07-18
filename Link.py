class Node():
    def __init__(self, data, nextNode, previousNode):
        self.data = data
        self.nextNode = nextNode
        self.previousNode = previousNode

    def getData(self):
        return self.data

    def setData(self, obj):
        self.data = obj

    def getNextNode(self):
        return self.nextNode

    def setNextNode(self, node):
        self.nextNode = node

    def getPreviousNode(self):
        return self.previousNode

    def setPreviousNode(self, node):
        self.previousNode = node

class Link():
    def __init__(self, classType):
        self.classType = classType
        self.firstNode = None
        self.currentNode = None
        self.size = 0

    def getSize(self):
        return self.size

    def add(self, obj):
        if type(obj) is self.classType:
            if self.firstNode == None:
                helpNode = Node(obj,None,None)
                helpNode.setNextNode(helpNode)
                helpNode.setPreviousNode(helpNode)
                self.firstNode = self.currentNode = Node(obj,helpNode,helpNode)
                helpNode = None #μπορεί να μην χρειάζεται
            elif self.size == 1:
                self.currentNode = Node(obj,self.firstNode,self.firstNode)
                self.firstNode.setNextNode(self.currentNode)
                self.firstNode.setPreviousNode(self.currentNode)
            else:
                helpNode = self.firstNode.getPreviousNode()
                self.currentNode = Node(obj,self.firstNode,helpNode)
                helpNode.setNextNode(self.currentNode)
                self.firstNode.setPreviousNode(self.currentNode)
                helpNode = None #μπορει να μην χρειάζεται
            self.size += 1

    def clear(self):
        currentNode = self.firstNode
        for i in range(self.size):
            currentNode.setPreviousNode(None)
            currentNode = currentNode.getNextNode()
        currentNode.setNextNode(None)
        self.firstNode = self.currentNode = None

    def get(self, place):
        if place >= 0 and place < self.size:
            counter = 0
            currentNode = self.firstNode
            while counter != place:
                currentNode = currentNode.getNextNode()
                counter += 1
            return currentNode.getData()

    def getData(self):
        if self.currentNode != None:
            return self.currentNode.getData()
        else:
            return None

    def goFront(self, steps):
        if steps > 0:
            for i in range(steps):
                self.currentNode = self.currentNode.getNextNode()
            return self.currentNode

    def goBack(self, steps):
        if steps > 0:
            for i in range(steps):
                self.currentNode = self.currentNode.getPreviousNode()
            return self.currentNode

    def setDefault(self, obj):
        currentNode = self.firstNode
        while currentNode.getData() != obj:
            currentNode = currentNode.getNextNode()
            if currentNode == self.firstNode:
                break
        if currentNode.getData() == obj:
            self.currentNode = currentNode

    def setNext(self):
        if self.currentNode != None:
            self.currentNode = self.currentNode.getNextNode()

    def setPrevious(self):
        self.currentNode = self.currentNode.getPreviousNode()

    def remove(self, obj):
        if type(obj) is self.classType:
            if self.size == 1 and self.firstNode.getData() == obj:
                self.firstNode = self.currentNode = None
            else:
                currentNode = self.firstNode
                while currentNode.getData() != obj:
                    currentNode = currentNode.getNextNode()
                    if currentNode == self.firstNode:
                        break
                if currentNode.getData() == obj:
                    if currentNode != self.firstNode:
                        currentNode.getPreviousNode().setNextNode(currentNode.getNextNode())
                        currentNode.getNextNode().setPreviousNode(currentNode.getPreviousNode())
                    else:
                        helpNode = self.firstNode.getNextNode()
                        helpNode.setPreviousNode(self.firstNode.getPreviousNode())
                        self.firstNode = self.firstNode.getPreviousNode()
                        self.firstNode.setNextNode(helpNode)
                        helpNode = None #μπορεί να μην χρειάζεται
            self.size -= 1

    def swap(self, obj1, obj2):
        n1 = self.firstNode
        n2 = self.firstNode
        while n1.getData() != obj1:
            n1 = n1.getNextNode()
            if n1 == self.firstNode:
                break
        while n2.getData() != obj2:
            n2 = n2.getNextNode()
            if n2 == self.firstNode:
                break
        if n1.getData() == obj1 and n2.getData() == obj2:
            n1.setData(obj2)
            n2.setData(obj1)
