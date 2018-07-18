class Node():
    def __init__(self, data, comparedData, previousNode = None, leftNode = None, rightNode = None):
        self.data = data
        self.comparedData = comparedData
        self.previousNode = previousNode
        self.leftNode = leftNode
        self.rightNode = rightNode

    def get_Data(self):
        return self.data

    def get_Compared_Data(self):
        return self.comparedData

    def get_Previous_Node(self):
        return self.previousNode

    def get_Left_Node(self):
        return self.leftNode

    def get_Right_Node(self):
        return self.rightNode

    def set_Left_Node(self, node):
        self.leftNode = node

    def set_Right_Node(self, node):
        self.rightNode = node

    def set_PreviousNode(self, node):
        self.previousNode = node

    def compare_To(self,data):
        if self.comparedData == data:
            return 0
        elif self.comparedData < data:
            return -1
        else:
            return 1

    def insert(newObject):
        if newObject.get_Compared_Data() < self.comparedData:
            if self.leftNode == None:
                self.leftNode = Node(newObject,newObject.get_Compared_Data,self)
                return True
            else:
                self.leftNode.insert(newObject)
        elif newObject.get_ComparedData() > self.comparedData:
            if self.rightNode == None:
                self.rightNode = Node(newObject,newObject.get_Compared_Data,self)
                return True
            else:
                self.rightNode.insert(newObject)
        return False

class Tree_Set():
    def __init__(self, class_Type):
        self.root = None
        self.class_Type = class_Type
        self.size = 0

    def get_Class_Type(self):
        return self.class_Type

    def get_Size(self):
        return self.size

    def clear(self):
        self.root = None

    def add(newObject, comparedData):
        if type(newObject) is self.class_Type:
            if (self.root == None):
                self.root = Node(newObject)
            else:
                insert = self.root.insert(newObject)
                if insert:
                    self.size += 1

    def remove(self,obj):
        if type(obj) is self.class_Type:
            currentNode = self.root
            while currentNode.get_Compared_Data() != obj.get_Compared_Data():
                if currentNode.get_Compared_Data() < obj.get_Compared_Data():
                    currentNode = currentNode.get_Right_Node()
                elif currentNode.get_Compared_Data() > obj.get_Compared_Data():
                    currentNode = currentNode.get_Left_Node()
            if currentNode.get_Compared_Data() == currentNode.get_Compared_Data():
                if currentNode.get_Right_Node() != None:
                    if currentNode.get_Left_Node() != None:
                        if currentNode != self.root:
                            currentNode.get_Right_Node().set_Previous_Node(currentNode.get_Left_Node())
                        else:
                            self.root = currentNode.get_Left_Node()
                    else:
                        if currentNode != self.root:
                            currentNode.get_Right_Node().set_Previous_Node(currentNode.get_Previous_Node())
                        else:
                            self.root = None
                else:
                    if currentNode.get_Right_Node() != None:
                        if currentNode != self.root:
                            currentNode.get_Right_Node().set_Previous_Node(currentNode.get_Previous_Node())
                        else:
                            self.root = currentNode.get_Right_Node()
                    else:
                        if currentNode != self.root:
                            currentNode.get_Previous_Node().set_Right_Node(None)
                        else:
                            self.root = None

    def get_Object_By_Data(self,data):
        currentNode = self.root
        while currentNode.getLeftNode() != None and current.getRightNode() != None:
            if currentNode.compare_To(data) == 0:
                return self.root.get_Data()
            elif currentNode.compare_To(data) == -1:
                currentNode = currentNode.getLeftNode()
            elif currentNode.compare_To(data) == 1:
                currentNode = currentNode.getRightNode()
        if currentNode.get_Compared_Data() == data:
            return currentNode.get_Data()

    def get_Object_By_Place(self,place):#είναι μισοτελειωμένη
        if place >= 0 and place < size:
            counter = 0
            currentNode = self.root
            while counter != place:
                while currentNode.get_Right_Node() != None and currentNode.get_Left_Node() != None:#βρίσκω το πιο δεξιό
                    currentNode = currentNode.get_Right_Node()
                counter += 1
                if currentNode.get_Previous_Node().get_Left_Node() != None:
                    currentNode.get_Previous_Node().get_Left_Node()
                    while currentNode.get_Right_Node() != None and currentNode.get_Left_Node() != None:#ψάχνω στον αριστερό κόμβο
                        currentNode = currentNode.get_Right_Node()
                    counter += 1
                else:
                    currentNode = currentNode.get_Previous_Node()
            return currentNode.get_Data()
                

    def to_List(self):
        '''objects_list = []
        if self.root == None:
            return []
        elif self.root.get_Right_Node() != None:
            currentNode = self.root.get_Right_Node()
        while currentNode != self.root:
            if currentNode == None:'''
        pass
