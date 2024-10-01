from collections import defaultdict

class Node:

    def __init__(self, num=None, parent=None):
        self.id = None
        self.num = None
        self.parent = parent
    
    def getId(self):
        return self.id
    
    def getNum(self):
        return self.num
    
    def getParent(self):
        return self.parent
    
    def setId(self, id):
        self.id = id

    def setNum(self, num):
        self.num = num

    def setParent(self, parent):
        self.parent = parent

class Graph:

    def __init__(self):
        self.size = 0
        self.list = defaultdict(list)

    def addList(self, listNode):
        count = 0
        for node in listNode:
            node.setId(self.size + count)
            self.list[self.size].append(node)
            count += 1
        self.size += count

    def addListWithId(self, id, listNode):
        count = 0
        for node in listNode:
            node.setId(self.size + count)
            self.list[id].append(node)
            count += 1
        self.size += count

    def IDDFS(self, node, target, depth):
        print('ok')

    def CopyAndEdit(self): # -------------------implementacao 1
        print('copy')

    def ModParentState(self): # --------------- implementacao 2
        print('edit')
        
    
g = Graph()
g.addList([Node()])


print('End Point')