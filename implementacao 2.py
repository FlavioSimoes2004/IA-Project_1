import numpy as np
from Node import Node

class Graph:

    def __init__(self, node, limit=30000):
        self.root = node
        self.limit = limit
        self.generateNodes()

    def generateNodes(self):
        list_nodes = [self.root]
        size = 1
        index = 0

        node = list_nodes[index]
        actions = node.getActions()

        copy_node = None

        while(True):
            for action in actions:
                self.ModifyParent(node, action)
                if self.checkNodes(node.getMatrix()) == False:
                    copy_node = node.CopyNode()
                    node.addChild(copy_node)
                    copy_node.setParent(node)
                    list_nodes.append(copy_node)
                    size += 1
                    print(size)
                self.UndoModification(node, action)

            index += 1
            if index >= size or size >= self.limit:
                break
            node = list_nodes[index]
            actions = node.getActions()

    def checkNodes(self, matrix_compare): # check every matrix already created and compare to the new matrix to know if it already exists
        list_nodes = [self.root]
        index = 0
        node = list_nodes[index]
        children = node.getChildren()

        count = 0

        if node.Compare(matrix_compare):
            count += 1

        while(True):
            if children != None:
                for child in children:
                    list_nodes.append(child)
                    if child.Compare(matrix_compare):
                        count += 1
                        if count >= 2:
                            return True
                    
            index += 1
            if index >= len(list_nodes):
                break
            node = list_nodes[index]
            children = node.getChildren()

        return False

    def ModifyParent(self, node, action): # do action on parent
        zeroPos = node.zeroPos()

        if action == 'left':
            aux = node.getMatrixSingleElement(zeroPos[0], zeroPos[1]-1)
            node.setMatrixSingleElement(zeroPos[0], zeroPos[1]-1, 0)
            node.setMatrixSingleElement(zeroPos[0], zeroPos[1], aux)
        elif action == 'right':
            aux = node.getMatrixSingleElement(zeroPos[0], zeroPos[1]+1)
            node.setMatrixSingleElement(zeroPos[0], zeroPos[1]+1, 0)
            node.setMatrixSingleElement(zeroPos[0], zeroPos[1], aux)
        elif action == 'down':
            aux = node.getMatrixSingleElement(zeroPos[0]+1, zeroPos[1])
            node.setMatrixSingleElement(zeroPos[0]+1, zeroPos[1], 0)
            node.setMatrixSingleElement(zeroPos[0], zeroPos[1], aux)
        else: # action == up
            aux = node.getMatrixSingleElement(zeroPos[0]-1, zeroPos[1])
            node.setMatrixSingleElement(zeroPos[0]-1, zeroPos[1], 0)
            node.setMatrixSingleElement(zeroPos[0], zeroPos[1], aux)

    def UndoModification(self, node, action): # undo the action made on parent
        zeroPos = node.zeroPos()

        if action == 'left':
            aux = node.getMatrixSingleElement(zeroPos[0], zeroPos[1]+1)
            node.setMatrixSingleElement(zeroPos[0], zeroPos[1]+1, 0)
            node.setMatrixSingleElement(zeroPos[0], zeroPos[1], aux)
        elif action == 'right':
            aux = node.getMatrixSingleElement(zeroPos[0], zeroPos[1]-1)
            node.setMatrixSingleElement(zeroPos[0], zeroPos[1]-1, 0)
            node.setMatrixSingleElement(zeroPos[0], zeroPos[1], aux)
        elif action == 'down':
            aux = node.getMatrixSingleElement(zeroPos[0]-1, zeroPos[1])
            node.setMatrixSingleElement(zeroPos[0]-1, zeroPos[1], 0)
            node.setMatrixSingleElement(zeroPos[0], zeroPos[1], aux)
        else: # action == up
            aux = node.getMatrixSingleElement(zeroPos[0]+1, zeroPos[1])
            node.setMatrixSingleElement(zeroPos[0]+1, zeroPos[1], 0)
            node.setMatrixSingleElement(zeroPos[0], zeroPos[1], aux)

    def IDDFS(self, goal):
        pass

node = Node([[3,1,2], [0, 4, 5], [6, 7, 8]])
desired_matrix = [[0,1,2], [3,4,5],[6,7,8]]
g = Graph(node, 1000)
g.IDDFS(desired_matrix)

print('End Point')