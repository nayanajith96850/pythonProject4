class Node:  # create a Node class

    def __init__(self):   # constructor
        self.data = None
        self.next = None

    def setData(self, data):  # set data of the Node
        self.data = data

    def getData(self):  # get data of the node
        return self.data

    def setNext(self, address):   # set next of the data
        self.Next = address

    def getNext(self):    # get data of the node
        return self.Next

class Stack:
    def __init__(self, limit=10):
        self.limit = limit #
        self.head = Node()
        self.stack = []

    def push(self, data):
        newNode = Node()
        newNode.setData(data)

        if len(self.stack) < self.limit:# check if stack lenght < limit
            if self.head is None:#check linked list heas is none
                self.head = newNode #assign head to new node
            else:
                newNode.setData(data)
                newNode.setNext(self.head)
                self.head = newNode
            return self.stack.append(data)

        else:
            print(" Stack overflow")
            return



    def pop (self):    # Remove elevement that is in the current head
        if self.head is None:
            print(" Stack is Underflow ")

        else:
            poppednode = self.head   # remove the head node and makes the proccesing one the new Node
            self.head = self.head.getnext()
            poppednode.getNext = None
            poppednode.data
            return self.stack.pop()

    def top(self):   #return the head node data
        if self.head is None:
            print(" Stack underflow")
            return

        else:
            poppednode = self.head
            self.head = self.head.getNext()
            poppednode.getNext = None
            poppednode.data
            return self.stack.pop()

    def top(self):      # return the head node data
        if self.head is None:
            print(" Stack Underflow")
            return
        else:
            return self.head.data
            return self.stack[len(self.stack)-1]

    def isEmptyStack(self):  # check stack is empty
        if len(self.stack) == 0:
            return True
        else:
            return False

    def isFullStack(self):    # check stack is Full
        if len(self.stack) == self.limit:
            return True
        else:
            return False  ## check stack size
    def size(self):
        return len(self.stack)




