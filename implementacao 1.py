import numpy as np
from Node import Node

class Graph:

    def __init__(self, node, limit=30000):
        self.root = node
        self.limit = limit # the limit of how many nodes can be created
        self.generateNodes2()

    def getRoot(self):
        return self.root

    def generateNodes(self, node): # recursive (not good because python has recursion limit)
        actions = node.getActions()

        for action in actions:
            new_node = self.CopyAndEdit(node, action)
            if not self.checkNodes(new_node):
                node.addChild(new_node)
                new_node.setParent(node)

        children = node.getChildren()
        if children != None:
            for child in children:
                self.generateNodes(child)

    def generateNodes2(self): # not recursive (good)
        list_nodes = [self.root]
        size = 1
        index = 0

        node = list_nodes[index]
        actions = node.getActions()

        new_node = None

        while(True):
            for action in actions:
                new_node = self.CopyAndEdit(node, action)
                if self.checkNodes(new_node.getMatrix()) == False:
                    node.addChild(new_node)
                    new_node.setParent(node)
                    list_nodes.append(new_node)
                    size += 1
                    print(size)

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

        if node.Compare(matrix_compare):
            return True

        while(True):
            if children != None:
                for child in children:
                    list_nodes.append(child)
                    if child.Compare(matrix_compare):
                        return True
                    
            index += 1
            if index >= len(list_nodes):
                break
            node = list_nodes[index]
            children = node.getChildren()

        return False

        '''children = node.getChildren()
        if children == None:
            return False
        
        else:
            for child in children:
                if child.Compare(matrix_compare):
                    return True
                else:
                    self.checkNodes(child, matrix_compare)
                
        return False'''
    
    def checkNodes2(self, node, matrix_compare): # compare only parent matrix to see if it exists
        while(True):
            if node == None:
                break
            if node.Compare(matrix_compare):
                return True
            node = node.getParent()
            
        return False

    def CopyAndEdit(self, node, action): # copy and edits the structure of a node, make the action and then return the new node
        copy_node = node.CopyNode()
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
    
    def BFS(self, goal, maxDepth):
        stack = []
        stack.append(self.getRoot())
        depth = 0
        node = None
        children = None

        while len(stack) > 0:
            if depth > maxDepth:
                print('COULDNT find node within depth range')
                return False
            
            node = stack.pop()
            if node.Compare(goal):
                print('node FOUND within depth range')
                return True

            children = node.getChildren()
            if not children == None:
                for child in children:
                    stack.append(child)
            

#sys.setrecursionlimit(2500)

node = Node([[3,1,2], [0, 4, 5], [6, 7, 8]])
desired_matrix = [[0,1,2], [3,4,5],[6,7,8]]
g = Graph(node, 1000)
g.BFS(desired_matrix, 6)

print('End Point')