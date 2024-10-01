class Node:

    def __init__(self, isDirty, children, parent=None):
        self.isDirty = isDirty # if is dirty or not
        self.children = children # list of nodes
        self.parent = parent # parent of the node

    def getIsDirty(self):
        return self.isDirty
    
    def getChildren(self):
        return self.children
    
    def getParent(self):
        return self.parent
    
    def getChildrenByIndex(self, i):
        return self.children[i]
    
    def setIsDirty(self, isDirty):
        self.isDirty = isDirty

    def setParent(self, parent):
        self.parent = parent

class Graph:

    def __init__(self):
        self.size = 0
        self.list = []

    def add(self, node):
        self.list.append(node)
        self.size += 1
        for r in node.getChildren():
            r.setParent(node)
            self.list.append(r)
            self.size += 1

    def IDDFS(self):
        print('ok')

    def CopyAndEdit(self): #implementacao 1
        print('copy')

    def ModParentState(self): # implementacao 2
        print('edit')
        
    
g = Graph()
g.add(Node(True, [Node(False, None), Node(True, None)]))


print('End Point')