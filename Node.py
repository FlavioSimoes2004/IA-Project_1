import numpy as np

class Node:

    def __init__(self, mtrx, parent=None, children=None):
        self.mtrx = np.array(mtrx)
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
        #return np.array_equal(self.mtrx, matrix)
        if len(self.mtrx) != len(matrix):
            return False

        for i in range(len(self.mtrx)):
            for j in range(len(self.mtrx[i])):
                if self.mtrx[i][j] != matrix[i][j]:
                    return False
        return True
    
    def quantActions(self):
        num_action = 4
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
        return num_action
    
    def getActions(self):
        zeroPos = self.zeroPos()
        actions = []

        if zeroPos[0] < len(self.getMatrix())-1:
            actions.append('down')
        if zeroPos[0] > 0:
            actions.append('up')
        
        if zeroPos[1] < len(self.getMatrixRow(0))-1:
            actions.append('right')
        if zeroPos[1] > 0:
            actions.append('left')

        return actions
    
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

    def CopyNode(self):
        return Node(np.copy(self.getMatrix()))