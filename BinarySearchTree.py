####Binary Search Tree
#####Taylor Hartman
######Run to print out a random binary tree along with the three given test cases
#####With each tree this program print out its inputs, height, min value, max value,
#####balanced status, pre-order iteration, in-order iteration, and post-order iteration

import random

class node(): ###Node class stores each node and its data
    def __init__(self, value = None):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

class tree(): ####tree class stores entire tree
    def __init__(self):
        self.root = None ####each tree owns its root

    def insert(self, values): ###inserts each value in list into a node with given value into tree
        for value in values:
            if (self.root == None):###if the root node is not set
                self.root = node(value) ##make the root node take this value
            else:
                self.insertNode(value, self.root) ####begins recursion

    def insertNode(self, value, currentNode): ###recursive method to find correct placement
        if (value > currentNode.value):
            if(currentNode.right == None):
                currentNode.right = node(value)
                currentNode.right.parent = currentNode
            else:
                self.insertNode(value, currentNode.right)
        elif (value != currentNode.value):
            if(currentNode.left == None):
                currentNode.left = node(value)
                currentNode.left.parent = currentNode
            else:
                self.insertNode(value, currentNode.left)
        else:
            print("Cannot Insert. The value " + str(value) + " already exists in tree")

    def getHeight(self, inNode): ###returns tree height
        if (self.root == None): ###If there is no root there is no height
            return -1
        else:
            height = self.getHeightRec(inNode, -1) ###otherwise start recursion
            return height

    def getHeightRec(self, currentNode, height): ###Recursive part of height
        if currentNode == None:
            return height
        leftHeight = self.getHeightRec(currentNode.left, height + 1)
        rightHeight = self.getHeightRec(currentNode.right, height + 1)
        return (max(leftHeight,rightHeight))

    def getNumNodes(self): ###returns the number of nodes in the tree
        return 0

    def getMax(self):
        if(self.root != None):
            max = self.getMaxRec(self.root)
            return max ####finds maximum value in tree

    def getMaxRec(self, currentNode):
        if(currentNode.right == None):
            return (currentNode.value)
        max = self.getMaxRec(currentNode.right)
        return max

    def getMin(self):
        if(self.root != None):
            return self.getMinRec(self.root) ###finds minimum value in tree

    def getMinRec(self, currentNode):
        if(currentNode.left == None):
            return(currentNode.value)
        min = self.getMinRec(currentNode.left)
        return min ###recursive getMin

    def delete(self, value): ###non recursive delete
        if (self.root != None):
            return self.deleteRec(value, self.root)
        print("no root found. cannot remove value: " + str(value))
        return -1

    def deleteRec(self, value, currentNode):
        if(value == self.root.value): #### if user wants to delete root
            if (self.root.left == None and self.root.right == None):
                self.root = None
            elif(self.root.left != None and self.root.right != None):
                currentNode.right.parent = None
                self.root = currentNode.right
                traversalNode = currentNode.right
                while(traversalNode.left != None):
                    traversalNode = traversalNode.left
                traversalNode.left = currentNode.left
                traversalNode.left.parent = traversalNode
            elif(self.root.left != None):
                self.root.left.parent = None
                self.root = self.root.left
            elif(self.root.right != None):
                self.root.right = None
                self.root = self.root.right
            return
        if(value == currentNode.value): ###if value is found
            if(currentNode.left == None and currentNode.right == None): ###if deleted node has no children
                if (currentNode.parent.right == currentNode):
                    currentNode.parent.right = None
                else:
                    currentNode.parent.left = None
            elif(currentNode.left == None): ####if deleted node has a right child
                if (currentNode.parent.right == currentNode): ####if the deleted node is a right child
                    currentNode.parent.right = currentNode.right
                    currentNode.right.parent = currentNode.parent
                else:
                    currentNode.parent.left = currentNode.right
                    currentNode.right.parent = currentNode.parent
            elif(currentNode.right == None):####if deleted node has a left child
                if (currentNode.parent.right == currentNode):
                    currentNode.parent.right = currentNode.left
                    currentNode.left.parent = currentNode.parent
                else:
                    currentNode.parent.left = currentNode.left
                    currentNode.left.parent = currentNode.parent
            elif(currentNode.right != None and currentNode.left != None):####if deleted node has two children
                if (currentNode.parent.right == currentNode): ###if this node is a right node
                    currentNode.parent.right = currentNode.right
                    currentNode.right.parent = currentNode.parent
                if (currentNode.parent.left == currentNode): ###if this node is a left node
                    currentNode.parent.left = currentNode.right
                    currentNode.right.parent = currentNode.parent

                currentNode.right.parent == currentNode.parent
                traversalNode = currentNode.right
                while(traversalNode.left != None):
                    traversalNode = traversalNode.left
                traversalNode.left = currentNode.left
                traversalNode.left.parent = traversalNode
            del currentNode


        elif (value > currentNode.value): #####else traverse tree to find value
            if(currentNode.right != None):
                self.deleteRec(value, currentNode.right)
            else:
                print("Cannot delete. Value " + str(value) + " is not in tree")
                return -1
        elif (value < currentNode.value):
            if(currentNode.left != None):
                self.deleteRec(value, currentNode.left)
            else:
                print("Cannot delete. Value " + str(value) + " is not in tree")
                return -1 ####recursive delete function

    def isBalanced(self):##determines if the tree is balanced (defaults to a tolernace of 1)
        if (self.root == None):
            return True

        leftHeight = self.getHeight(self.root.left)
        rightHeight = self.getHeight(self.root.right)

        if (abs(leftHeight - rightHeight) <= 1): ####chnage tolerance here if desired
            return True

        return False

    def preOrderIterator(self):
        if(self.root == None):
            return -1
        return(self.iterator(self.root))####returns an array of the tree values using pre order iteraton

    def inOrderIterator(self):
        if(self.root == None):
            return -1
        leftArray = self.iterator(self.root.left)
        if(leftArray != None):
            del leftArray[leftArray.index(self.root.value):len(leftArray)]
        root = [self.root.value]
        rightArray = self.iterator(self.root.right)
        if(rightArray != None):
            del rightArray[rightArray.index(self.root.value):len(rightArray)]
        if(rightArray == None):
            rightArray = []
        if(leftArray == None):
            leftArray = []
        return(leftArray + root + rightArray)####returns an array of the tree values using in order iteraton

    def postOrderIteration(self):
        if(self.root == None):
            return -1
        leftArray = self.iterator(self.root.left)
        if(leftArray != None):
            del leftArray[leftArray.index(self.root.value):len(leftArray)]
        root = [self.root.value]
        rightArray = self.iterator(self.root.right)
        if(rightArray != None):
            del rightArray[rightArray.index(self.root.value):len(rightArray)]
        if(rightArray == None):
            rightArray = []
        if(leftArray == None):
            leftArray = []
        return(leftArray + rightArray + root)####returns an array of the tree values using post order iteraton

    def iterator(self, inNode):
        if(inNode == None):
            return
        array = []
        return (self.preOrderIteratorRec(inNode, array)) ###iterator funcrtion

    def preOrderIteratorRec(self, currentNode, array):
        x = True
        while(x == True):
            if(currentNode.value not in array): ###adds to array
                array.append(currentNode.value)
            if(currentNode.left != None and currentNode.left.value not in array):###left first
                currentNode = currentNode.left
            elif(currentNode.right != None and currentNode.right.value not in array):###then right
                currentNode = currentNode.right
            elif(currentNode.parent != None): ####then back up
                currentNode = currentNode.parent
            else:
                x = False
                return(array) ####recursive iterator

    def printInfo(self):
        height = self.getHeight(self.root)
        if (height == -1):
            print("No root input given.")
        else:
            print ("Height: " + str(height))
        print ("Minimum: " + str(self.getMin()))
        print ("Maximum: " + str(self.getMax()))
        print("Balanced: " + str(self.isBalanced()))
        print("Pre-Order Iteration: " + str(self.preOrderIterator()))
        print("In-Order Iteration: " + str(self.inOrderIterator()))
        print("Post-Order Iteration: " + str(self.postOrderIteration()))

    def printTree(self): ###I copied most of this and the printRecursive method and eddited them to fit my code
                    ### I thought it would be better to spend time implementing/understanding the data structure
                    ###and printing it would be an useful extra
        if (self.getHeight(self.root) >= 0):
            lines, _, _, _ = self.printRecursive(self.root)
            for line in lines:
                print(line)

    def printRecursive(self, currentNode):
        if (currentNode.right == None and currentNode.left == None): ###If the node has nothign past it
            line = '%s' % currentNode.value
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        if (currentNode.right == None): ##if there is only a node.left
            lines, n, p, x = self.printRecursive(currentNode.left)
            s = '%s' % currentNode.value
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        if (currentNode.left == None): ### if there is only a node.right
            lines, n, p, x = self.printRecursive(currentNode.right)
            s = '%s' % currentNode.value
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        ###if the node has a left and a right child
        left, n, p, x = self.printRecursive(currentNode.left)
        right, m, q, y = self.printRecursive(currentNode.right)
        s = '%s' % currentNode.value
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2


class configureRandomTree(): ###Prints out a random tree
    print("Making random tree: ")
    tree = tree()

    nodeNumber = random.randint(0, 30) ####Randomly decides how many nodes to put in tree
    values = []
    for node in range(nodeNumber):
        values.append(random.randint(0,100)) ###chooses random value to give each node

    tree.insert(values)
    print("Tree inputs: " + str(values))
    tree.printTree()
    tree.printInfo()


class runTests(): ####Runs Test Cases after random test case has run
    print("********Running Test Tree 1********")
    #####Test1
    tree1 = tree()
    values = [40, 22, 23, 50, 20, 7, 94, 11, 41, 58, 10]
    tree1.insert(values)
    print ("Tree inputs: " + str(values))
    tree1.printTree()
    tree1.printInfo()
    print("Attempting to delete values 19 and 50 from tree")
    tree1.delete(19)
    tree1.delete(50)
    tree1.delete(10)
    tree1.printTree()
    tree1.printInfo()

    print("********Running Test Tree 2********")
    #####Test1
    tree2 = tree()
    values = [50, 22, 23, 20, 7, 11, 41, 58, 10, 70, 91, 84, 22, 88, 94, 33, 11, 82]
    tree2.insert(values)
    print ("Tree inputs: " + str(values))
    tree2.printTree()
    tree2.printInfo()
    print("Attempting to delete values 11, 33, and 50")
    tree2.delete(11)
    tree2.delete(33)
    tree2.delete(50)
    tree2.printTree()
    tree2.printInfo()

    print("********Running Test Tree 3********")
    #####Test1
    tree3 = tree()
    values = [37, 77, 9, 98, 20, 19, 50, 88, 47, 47, 47, 99, 10, 4, 5]
    tree3.insert(values)
    print ("Tree inputs: " + str(values))
    tree3.printTree()
    tree3.printInfo()
    print("Attempting to delete values 4, 77, and 88")
    tree3.delete(4)
    tree3.delete(77)
    tree3.delete(88)
    tree3.printTree()
    tree3.printInfo()

    print("********Running Test Tree 4********")
    #####Test1
    tree4 = tree()
    values = [1]
    tree4.insert(values)
    print ("Tree inputs: " + str(values))
    tree4.printTree()
    tree4.printInfo()
    print("Attempting to delete value 1")
    tree4.delete(1)
    tree4.printTree()
    tree4.printInfo()

    print("********Running Test Tree 5********")
    #####Test1
    tree5 = tree()
    values = [20, 10, 30]
    tree5.insert(values)
    print ("Tree inputs: " + str(values))
    tree5.printTree()
    tree5.printInfo()
    print("Attempting to delete value 20")
    tree5.delete(20)
    tree5.printTree()
    tree5.printInfo()
