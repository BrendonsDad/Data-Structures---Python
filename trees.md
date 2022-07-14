# Trees
## Trees, Binary Trees, and Binary Sorted Trees

# What is a Tree?
Trees in coding are a form of a data structure that is characterized by having a root and branches type set up. In trees, each item can be a child of only one other item, but each item can have multiple children. This causes the structure to branch out and look like a tree when we illustraite it. What we will learn about are binary trees, or more specificaly, binary sorted trees (BST). 

# Binary Trees
A binary tree is a tree that requires each of it's items to only have a maximum of two children. Note however that items can have one or zero items and still be considered a binary tree. A BST is a binary tree that is organized in such a way that we can easily traverse it. BSTs achieve this by inserting each item into the tree in a certain way. If the value is greater than the current node (item), we check to see if there is an item on to the right. If there is we repeat the prosses until ther is an empty spot (hint, you will use recursion a lot for trees). We do the same thing if the value is less than the current node, only we insert it to the left.

```python
def insert(self, data):
    # This checks if the tree is empty. If so, make the root.
    if self.root is None:
        self.root = Node(data)
    else:
        #otherwise, start sorting using the root first
        self.sorted_insert(data, self.root) 

def sorted_insert(self, data, node):
    # There can only be one of each value in trees, so pass
    if data == node.value:
        pass
    #Checks to see if the value is less than our current value
    elif data < node.value:
        # If there is open space, insert the new node
        if node.left is None:
            node.left = Node(data)
        # If not, repeat the process
        else:
            self.sorted_insert(data, node.left)
    else:
        # Same if value is greater than
        if node.right is None:
            node.right = Node(data)
        else:
            self.sorted_insert(data, node.right)
```

When we organize trees like this, it ends up looking like a tree! 

![FIFO in real life](images/bst.png)

# Balanced BST
The benefit of a balanced BST is that it has O(log n) efficiency, which is very good. A balanced BST is a BST that does not have a large difference in height on either side of the root or subsequent nodes. The table above looks great becuase 56 was entered first, than 30, than 70 and so on. But what if we got really unlucky and inserted each item in order (ie. 3, 11, 16, 22...)? Well, then this tree would essentially have the same preformance of a linked list and this would defeat the purpose of the linked list. There are algorithms to sort trees, but they are outside the scope of this tuturial. If you are interested, study the AVL alogorithm. For now, we will focus on inserting the items correctly so the tree is balanced from the start. This will also help us traverse the list. 



# Traversing the Tree
To sort traverese a linked list we have to use recursion and start at the root. We must keep going until we find the end of our tree on the left side (this will enable us to start at the lowest and work towards the highest.) Since we know lows are on the left an highs are on the right, we should use recursion for the left side, than print the nodes value (This will eventually print every nodes data), than use recursion again accept working towards the right. When the right sided recursion starts, it must check if there are any on the left again. Here is how you code it. 

```python
# This function is here to help us start at the root
def _printBST(self):
    if self.root is None:
        print("The tree is empty")
    else:
        total = 0
        self.printBST(self.root, total)

def printBST(self, node, total):
    # Check to see if there is a node
    if node is not None:
        # keep going down the left rabit hole
        self.printBST(node.left, total)
        # once we are done with that, print our value
        print(node.value)
        # proceed down the right rabit hole
        self.printBST(node.right, total)
```


# Example Problem

Imagine you have been tasked with getting the number of items in a list. Try and think about how you would achieve this. There are many different paths to take, however, the easiest is to simply keep track of this in your binary tree class. Have a variable that keeps track of the numbers and every time you insert a node, add one to that value.

```python
# Here we make our node class, with a value and a right and left value
class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
# Our Binary Tree class, that has a root and a size
class BinarySortedTree():
    def __init__(self):
        self.root = None
        # Initialize the size variable to be 0
        self.size = 0

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
            # When we add our root, add 1 to the size
            self.size = 1
        else:
            self.sorted_insert(data, self.root) 

    def sorted_insert(self, data, node):
        if data == node.value:
            pass
        
        elif data < node.value:
            if node.left is None:
                node.left = Node(data)
                # Everytime we insert a node, += 1 to the size
                self.size += 1
            else:
                self.sorted_insert(data, node.left)
        else:
            if node.right is None:
                node.right = Node(data)
                # Again, we inserted into the BST so we must add one to size
                self.size += 1
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


```

# Challenge Problem
Now is your opertunity try it yourself and solve a challenging problem. Add method that can get the sum of all the items in your linked list. Copy the code above into your IDE and then copy the following test cases at the bottom. The tests should display as expected. 
```python
mytree = BinarySortedTree()
mytree.insert(15)
mytree.insert(7)
mytree.insert(22)
mytree.insert(3)
mytree.insert(10)
mytree.insert(17)
mytree.insert(25)
mytree._printBST() # 3, 7, 10, 15, 17, 22, 25
mytree.printsize() # 7
# Here you will call your function. Name the function whaever you like and 
# give whatever variable you see fit. Just ensure it outputs the sum of all (99)

```

# Solution

please try to work on this for at least an hour. If you still need help feel free to look over the solution code:
[Solution](treesolution.py)

## Return Home
[Home Page](home.md)