class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, list=None):
        self.values = list
        self.head = self.createList()

    # *creating list from given list
    def createList(self):
        if self.values == None:
            self.head = None
        else:
            self.head = Node(self.values[0])
            tail = self.head
            for x in range(1, len(self.values)):
                self.append(self.values[x])
            return self.head

    # *Inserting element at start of Linked List
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # *Inserting element at end of Linked List
    def append(self, new_data):
        new_node = Node(new_data)

        if self.head == None:
            self.head = new_node

        else:
            tail = self.head
            while tail.next:
                tail = tail.next
            tail.next = new_node

    # *Inserting after specific node
    def insertAfter(self, prev_data, new_data):
        new_node = Node(new_data)
        prev_node = self.head
        while prev_node:
            if prev_node.data == prev_data:
                break
            else:
                prev_node = prev_node.next
        if prev_node is None:
            print(f"{prev_data} does not present in the linked list")
            return
        new_node.next = prev_node.next
        prev_node.next = new_node

    # *Deleting a specific node
    def deleteNode(self, key):
        temp = self.head

        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return

        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        if temp == None:
            return

        prev.next = temp.next
        temp = None

    # *Deleting at specific position
    def deleteNodeAt(self, position):
        if self.head is None:
            return

        if position == 0:
            temp = self.head
            self.head = temp.next
            return

        current = self.head
        index = 0
        while current:
            prev = current
            current = current.next
            index += 1

            if index == position:
                if current is not None:
                    prev.next = current.next
                    current.next = None
                    return
        print("Index exceeds the size of the linked list")

    # *Printing the Linked List
    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end=" --> ")
            temp = temp.next
            if temp == self.head:
                print(f"{temp.data}(HEAD)")
                break
        if temp == None:
            print("None")

    # *Makes the linked list a circular Linked list
    def circular(self):
        tail = self.head
        while tail.next:
            tail = tail.next
        tail.next = self.head


if __name__ == "__main__":

    l1_list = [1, 2, 3, 4, 5, 6]
    l1 = LinkedList(l1_list)
    l1.circular()

    l2 = LinkedList()
    l2.append(1)

    l1.printList()
    l2.printList()
