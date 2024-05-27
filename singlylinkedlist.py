class Node:
    def __init__(self, data):#introduced a class
        self.data = data     #2 attributes
        self.next = None 
class LinkedList:
    def __init__(self):
        self.head = None 

    def insertHead(self,newNode):
        temoraryNode = self.head
        self.head = newNode 
        self.head.next = temporaryNode
        del temporaryNode 

    def insertAt(self, newNode, position):
        currentNode = self.head 
        currentPosition = 0
        while True:
            if currentPosition == position:
                previousNode.next = newNode
                newNode.next = currentNode
                break
            previousNode = currentNode  
            currentNode = currentNode.next
            currentPosition +=1

    def insertEnd(self, newNode):
        if self.head is None:
            self.head = newNode
        else:
            lastNode = self.head 
            while True: 
                if lastNode.next is None:
                    break 
                lastNode = lastNode.next
            lastNode.next = newNode
    def printList(self):
        if self.head is None:
            print("List is empty")
            return 
        currentNode = self.head 
        while True:
            if currentNode is None:
                break 
            print(currentNode.data)
            currentNode = currentNode.next
firstNode = Node(10)
linkedList = LinkedList()
linkedList.insertEnd(firstNode)
secondNode = Node(20)
linkedList.insertEnd(secondNode)
thirdNode = Node(15)
linkedList.insertAt(thirdNode, 1)
linkedList.printList()