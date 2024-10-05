import numpy as np
from Node import Node

class Graph:

    def __init__(self, node):
        self.root = node
        self.generateNodes(self.root)

    def generateNodes(self, node):
        actions = node.getActions()

        for action in actions:
            self.ModifyParent(node, action)
            if not self.checkNodes2(node, node.getParent()):
                pass
            # undo node modification

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