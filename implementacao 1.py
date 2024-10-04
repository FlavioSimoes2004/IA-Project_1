from collections import defaultdict
import numpy as np

class Node:

    def __init__(self, mtrx, children=None):
        self.mtrx = mtrx
        self.children = children # its a list of nodes

    def getMatrix(self):
        return self.mtrx
    
    def getMatrixRow(self, index):
        return self.mtrx[index]
    
    def getMatrixSingleElement(self, i, j):
        return self.mtrx[i][j]
    
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

    def Compare(self, matrix):
        return np.array_equal(self.mtrx, matrix)
    
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
        self.generateNodes(node)

    def generateNodes(self, node):
        actions = []
        zeroPos = node.zeroPos()
        
        if zeroPos[0] < len(node.getMatrix())-1:
            actions.append('right')
        if zeroPos[0] > 0:
            actions.append('left')
        
        if zeroPos[1] < len(node.getMatrixRow(0))-1:
            actions.append('down')
        if zeroPos[1] > 0:
            actions.append('up')

        for action in actions:
            new_node = self.CopyAndEdit(node, action)
            if not self.checkNodes(self.root, new_node):
                node.addChild(new_node)

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

node = Node([[1,2,3], [4, 5, 6], [7, 8, 0]])
g = Graph(node)

print('End Point')