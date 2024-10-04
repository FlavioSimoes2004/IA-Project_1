from collections import defaultdict
import numpy as np

class Node:

    def __init__(self, mtrx, parent=None, children=None):
        self.mtrx = mtrx
        self.parent = parent
        self.children = children # its a list of nodes

    def getMatrix(self):
        return self.mtrx
    
    def getMatrixRow(self, index):
        return self.mtrx[index]
    
    def getMatrixSingleElement(self, i, j):
        return self.mtrx[i][j]
    
    def getParent(self):
        return self.parent
    
    def getChildren(self):
        return self.children
    
    def setMatrix(self, mtrx):
        self.mtrx = mtrx

    def setMatrixRow(self, index, row):
        self.mtrx[index] = row

    def setMatrixSingleElement(self, i, j, value):
        self.mtrx[i][j] = value

    def setChildren(self, children):
        self.children = children

    def addChild(self, child):
        if self.children == None:
            self.children = []
        self.children.append(child)

    def setParent(self, parent):
        self.parent = parent

    def Compare(self, matrix):
        return np.array_equal(self.mtrx, matrix)
        #if len(self.mtrx) != len(matrix):
        #    return False

        #for i in range(len(self.mtrx)):
        #    for j in range(len(self.mtrx[i])):
        #        if self.mtrx[i][j] != matrix[i][j]:
        #            return False
        #return True
    
    def quantActions(self):
        action = 4
        line = 0
        for i in self.mtrx:
            column = 0
            for j in i:
                if j == 0:
                    if line == 0 or line == len(self.mtrx)-1:
                        action -= 1
                    if column == 0 or column == len(self.mtrx[line])-1:
                        action -= 1
                    return action
                column += 1
            line += 1
        return action
    
    def zeroPos(self):
        position = []
        line = 0
        for i in self.mtrx:
            column = 0
            for j in i:
                if j == 0:
                    position.append(line)
                    position.append(column)
                    return position
                column += 1
            line += 1

class Graph:

    def __init__(self, node):
        self.root = node
        self.generateNodes(self.root)

    def generateNodes(self, node):
        actions = []
        zeroPos = node.zeroPos()
        
        if zeroPos[0] < len(node.getMatrix())-1:
            actions.append('down')
        if zeroPos[0] > 0:
            actions.append('up')
        
        if zeroPos[1] < len(node.getMatrixRow(0))-1:
            actions.append('right')
        if zeroPos[1] > 0:
            actions.append('left')

        for action in actions:
            new_node = self.CopyAndEdit(node, action)
            if not self.checkNodes2(node, new_node):
                node.addChild(new_node)
                new_node.setParent(node)

        children = node.getChildren()
        if children != None:
            for child in children:
                self.generateNodes(child)

    def checkNodes(self, node, node_compare):
        children = node.getChildren()
        if children == None:
            return False
        
        else:
            for child in children:
                if child.Compare(node_compare):
                    return True
                else:
                    self.checkNodes(child, node_compare)
                
        return False
    
    def checkNodes2(self, node, node_compare):
        parent = node.getParent()
        if node.Compare(node_compare.getMatrix()):
            return True
        elif parent == None:
            return False
        
        return self.checkNodes2(parent, node_compare)

    def CopyAndEdit(self, node, action):
        copy_mtrx = np.copy(node.getMatrix())
        copy_node = Node(copy_mtrx)
        zeroPos = copy_node.zeroPos()

        if action == 'left':
            aux = copy_node.getMatrixSingleElement(zeroPos[0], zeroPos[1]-1)
            copy_node.setMatrixSingleElement(zeroPos[0], zeroPos[1]-1, 0)
            copy_node.setMatrixSingleElement(zeroPos[0], zeroPos[1], aux)
        elif action == 'right':
            aux = copy_node.getMatrixSingleElement(zeroPos[0], zeroPos[1]+1)
            copy_node.setMatrixSingleElement(zeroPos[0], zeroPos[1]+1, 0)
            copy_node.setMatrixSingleElement(zeroPos[0], zeroPos[1], aux)
        elif action == 'down':
            aux = copy_node.getMatrixSingleElement(zeroPos[0]+1, zeroPos[1])
            copy_node.setMatrixSingleElement(zeroPos[0]+1, zeroPos[1], 0)
            copy_node.setMatrixSingleElement(zeroPos[0], zeroPos[1], aux)
        else: # action == up
            aux = copy_node.getMatrixSingleElement(zeroPos[0]-1, zeroPos[1])
            copy_node.setMatrixSingleElement(zeroPos[0]-1, zeroPos[1], 0)
            copy_node.setMatrixSingleElement(zeroPos[0], zeroPos[1], aux)

        return copy_node
    
    def DSL(self, desired_result):
        pass

node = Node([[1,2,3], [4, 5, 6], [7, 8, 0]])
desired_matrix = [[0,1,2], [3,4,5],[6,7,8]]
g = Graph(node)
g.DSL(desired_matrix)

print('End Point')