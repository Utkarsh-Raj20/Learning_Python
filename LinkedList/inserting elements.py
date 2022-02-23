from tkinter import N


class Node:
    def __init__(self, data=None) -> None:
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    # *Inserting element at start of Linked List
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # *Inserting element at end of Linked List
    def append(self, new_data):
        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node

        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def insertAfter(self, prev_node, new_data):
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    # *Printing the Linked List
    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end="--> ")
            temp = temp.next
        if temp == None:
            print("None")


if __name__ == "__main__":

    l1 = LinkedList()
    l1.push(1)
    l1.append(2)
    l1.append(3)
    l1.append(5)

    l1.insertAfter(l1.head.next.next, 4)

    l1.printList()
