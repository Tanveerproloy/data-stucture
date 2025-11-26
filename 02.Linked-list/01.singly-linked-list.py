#single linked list

class Node:
    def __init__(self , value = None):
        self.value = value
        self.next = None


class sLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node =node.next
            
    #insert in linked list
    def insertSLL(self,value,location):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
            
        else:
            if location == 0:
                newNode.next = self.head
                self.head = newNode
        
            elif location == 1:
                newNode.next = None
                self.tail.next = newNode
                self.tail = newNode
            
            else:
                tempNode = self.head
                index = 0
                while index < location -1:
                    tempNode = tempNode.next
                    index +=1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode
                
    #Traverse single linked list
    def traverseSLL(self):
        if self.head is None:
            print("Single Linked list doesnt exist")
        else:
            node = self.head
            while node is not None:
                print(node.value)
                node = node.next
        
    #Searching a node
    def searchSLL(self,nodeValue):
        if self.head is None:
            return" Does Not Exist"
        else:
            node = self.head
            while node is not None:
                if node.value == nodeValue:
                    return node.value
                node = node.next
            return "The Value Is Not In This List"
        
    #Deleting a node
    def deleteNode(self,location):
        if self.head is None:
            print("Single linked list doesn't exist")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
            elif location ==1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None                
                else:
                    node = self.head
                    while node is not None:
                        if node.next == self.tail:
                            break
                        node.next = None
                        self.tail = None
            else:
                tempNode = self.head
                index = 0
                while index <location - 1:
                    tempNode = tempNode.next
                    index +=1
                nextNode = tempNode.next
                tempNode.next = nextNode.next
    
    #Delete Entire Linked List
    def deleteSLL(self):
        if self.head is None:
            print("Single Linked list doesn't exist")
        else:
            self.head = None
            self.tail = None
                
    
singLinkedList = sLinkedList()
singLinkedList.insertSLL(1,1)
singLinkedList.insertSLL(2,1)
singLinkedList.insertSLL(3,1)
singLinkedList.insertSLL(4,1)
singLinkedList.insertSLL(0,4)
singLinkedList.insertSLL(0,0)
print([node.value for node in singLinkedList])
singLinkedList.traverseSLL()

print(singLinkedList.searchSLL(32))
singLinkedList.deleteNode(3)
print([node.value for node in singLinkedList])