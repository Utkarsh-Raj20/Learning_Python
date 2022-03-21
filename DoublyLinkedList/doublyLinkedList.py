class Node:
    def __init__(self, data):
        self.prev = None
        self.next = None
        self.data = data


class DoublyLinkedList:
    def __init__(self, list=None):
        self.tail = None
        self.values = list
        self.head = self.createList()

    # * make Linkedlist from given list
    def createList(self):
        if self.values == None:
            self.head = None
        else:
            self.head = Node(self.values[0])
            tail = self.head
            for x in range(1, len(self.values)):
                self.append(self.values[x])
            return self.head

    # * push a element at start
    def push(self, new_data):
        if self.head is None:
            new_node = Node(new_data)
            self.head = new_node
        else:
            new_node = Node(new_data)
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    # * append a element at end
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

    # * insert a element at a specific position
    def insertAt(self, index, data):
        new_node = Node(data)
        if index == 0:
            self.push(data)
            return
        count = 1
        temp = self.head
        while temp:
            if count == index:
                new_node.next = temp.next
                new_node.prev = temp
                temp.next.prev = new_node
                temp.next = new_node
            temp = temp.next
            count += 1

    # * delete a node at a specific position
    def deleteAtIndex(self, index=None):
        if index is None:
            return
        elif index == 0:
            temp = self.head
            self.head = self.head.next
            self.head.prev = None
            return temp
        count = 0
        temp = self.head
        while temp:
            if count == index:
                temp.prev.next = temp.next
                temp.next.prev = temp.prev
                return temp
            temp = temp.next
            count += 1

    # * delete a specific Node
    def deleteNode(self, data):
        temp = self.head
        while temp:
            if temp.data == data:
                temp.prev.next = temp.next
                temp.next.prev = temp.prev
                return temp
            temp = temp.next
        print(f"'{data}' dose not exist in the linked list")

    # * make the list circular
    def circular(self):
        self.tail.next = self.head
        self.head.prev = self.tail

    # * print the list
    def printList(self):
        temp = self.head
        if temp is None:
            print("None")
            return
        else:
            print("None", end=" <-- ")
        while temp and temp.next:
            print(temp.data, end=" <--> ")
            temp = temp.next
            if temp == self.head:
                print(f"{temp.data}(HEAD)")
                break
        if temp.next == None:
            print(f"{temp.data} --> None")


if __name__ == "__main__":
    l1 = DoublyLinkedList()
    l1.append(2)
    l1.append(3)
    l1.push(1)
    # l1.printList()

    l2_list = [8, 6, 9, 5, 4, 7, 5, 2]
    l2 = DoublyLinkedList(l2_list)
    l2.insertAt(2, 0)
    l2.deleteNode(7)
    l2.circular()
    l2.printList()
