class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self) -> None:
        self.head = None
    
    def append(self, data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
        else:
            last = self.head
            while last.next:
                last = last.next
            last.next = newNode
        
    def push(self, data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode
    
    #! This creates a circular linkedlist
    def circular(self):
        last = self.head
        while last.next:
            last = last.next
        last.next = self.head
            
    def printList(self):
        last = self.head
        while last:
            print(last.data, end=" --> ")
            last = last.next
            if last == self.head:
                print(f"{last.data}(HEAD)")
                break
        if last == None:
            print("None")
            

if __name__ == "__main__":
    l1 = LinkedList()
    l1.push(1)
    l1.append(2)
    l1.circular()
    l1.printList()