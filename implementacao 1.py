import numpy as np
from Node import Node

class Graph:

    def __init__(self, node, goal, limit=30000):
        self.root = node
        self.limit = limit # the limit of how many nodes can be created
        self.generate_nodes_IDDFS(goal, limit)

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
                    print(f'generated nodes: {size}')

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
    
    def IDDFS(self, goal, maxDepth=1000):
        depth = 0
        result = self.IDDFS2(self.getRoot(), goal, depth, maxDepth)
        if result == None:
            print('node NOT found within max depth range')
        else:
            print('node FOUND within max depth range')
        return result

    def IDDFS2(self, node, goal, depth, maxDepth):
        if depth >= maxDepth:
            return None
        print(depth)
        if node.Compare(goal):
            return node
        children = node.getChildren()
        if children != None:
            for child in children:
                result = self.IDDFS2(child, goal, depth+1, maxDepth)
                if result != None:
                    return result
        return None
    
    def generate_nodes_IDDFS(self, goal, maxDepth=1000):
        depth = 0
        result = self.generate_nodes_IDDFS_2([self.getRoot()], goal, depth, maxDepth)
        if result == None:
            print('node NOT found within max depth range')
        else:
            print('node FOUND within max depth range')
        return result
    
    def generate_nodes_IDDFS_2(self, node_list, goal, depth, maxDepth):
        if depth >= maxDepth:
            return None
        
        list_node = []
        actions = []
        
        print(depth)
        for r in node_list:
            if r.Compare(goal):
                return r
            actions = r.getActions()
            for action in actions:
                copy = self.CopyAndEdit(r, action)
                if not self.checkNodes(copy.getMatrix()):
                    r.addChild(copy)
                    copy.setParent(r)
                    list_node.append(copy)
        return self.generate_nodes_IDDFS_2(list_node, goal, depth + 1, maxDepth)



node = Node([[1, 2, 3], [4, 0, 6], [7, 8, 5]])
goal_matrix = [[1,2,3], [4,5,6],[7,8,0]]
g = Graph(node, goal_matrix, 50)
#g.IDDFS(goal_matrix, 50)

print('End Point')