class Node:
    def __init__(self, data):
        self.prev = None
        self.next = None
        self.data = data


class DoublyLinkedList:
    def __init__(self, list=None):
        self.tail = None
        self.values = list
        self.isCircular = False
        self.head = self.createList()

    #* make Linkedlist from given list
    def createList(self):
        if self.values == None:
            self.head = None
        else:
            self.head = Node(self.values[0])
            tail = self.head
            for x in range(1, len(self.values)):
                self.append(self.values[x])
            return self.head


    #* push a element at start
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    #* append a element at end
    def append(self, new_data):
        new_node = Node(new_data)
        if self.head == None:
            self.head = new_node
        else:
            tail = self.head
            while tail.next:
                tail = tail.next
            tail.next = new_node
            new_node.prev = tail
            self.tail = new_node

    # TODO insert a element at a specific position
    # TODO delete a specific node
    # TODO delete a node at a specific position

    
    #* make the list circular
    def circular(self):
        self.isCircular = True
        self.tail.next = self.head
        self.head.prev = self.tail

    #* print the list
    def printList(self):
        temp = self.head
        if temp == None:
            return "None"
        elif self.isCircular:
            pass
        else:
            print("None", end=" <--> ")
        while temp:
            print(temp.data, end=" <--> ")
            temp = temp.next
            if temp == self.head:
                print(f"{temp.data}(HEAD)")
                break
        if temp == None:
            print("None")


if __name__ == "__main__":
    l1 = DoublyLinkedList()
    l1.append(2)
    l1.append(3)
    l1.push(1)
    
    l2_list = [8,6,9,5,4,7,5,2]
    l2 = DoublyLinkedList(l2_list)
    l2.circular()
    l2.printList()
