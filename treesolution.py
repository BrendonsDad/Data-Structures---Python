class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySortedTree():
    def __init__(self):
        self.root = None
        self.size = 0
        self.sum_of_items = 0

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
            self.size = 1
            self.sum_of_items = data
        else:
            self.sorted_insert(data, self.root) 

    def sorted_insert(self, data, node):
        if data == node.value:
            pass
        
        elif data < node.value:
            if node.left is None:
                node.left = Node(data)
                self.size += 1
                self.sum_of_items += data
            else:
                self.sorted_insert(data, node.left)
        else:
            if node.right is None:
                node.right = Node(data)
                self.size += 1
                self.sum_of_items += data
            else:
                self.sorted_insert(data, node.right)
    def _printBST(self):
        if self.root is None:
            print("The tree is empty")
        else:
            total = 0
            self.printBST(self.root, total)
    def printBST(self, node, total):
        if node is not None:
            self.printBST(node.left, total)
            print(node.value)
            self.printBST(node.right, total)

    def printsize(self):
        if self.size == 1:
            print(f"There is only one item in the tree. The root {self.root}.")
        else:
            print(f"There are {self.size} items in this tree")

    def get_sum(self):
        print(f"The sum of all the items is {self.sum_of_items}")


    def get_sum_2(self, node):
        if node == None:
            return 0
        else: 
            return(node.value + self.get_sum_2(node.left) + self.get_sum_2(node.right))



        
mytree = BinarySortedTree()
mytree.insert(15)
mytree.insert(7)
mytree.insert(22)
mytree.insert(3)
mytree.insert(10)
mytree.insert(17)
mytree.insert(25)
mytree._printBST()
mytree.printsize()
mytree.get_sum()
print(mytree.get_sum_2(mytree.root))

