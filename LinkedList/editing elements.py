from tkinter import N
from tkinter.messagebox import NO


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

    # *Printing the Linked List
    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end=" --> ")
            temp = temp.next
        if temp == None:
            print("None")


if __name__ == "__main__":

    l1 = LinkedList()
    l1.push(1)
    l1.append(2)
    l1.append(3)
    l1.append(5)

    l1.insertAfter(3, 4)
    l1.deleteNode(1)

    l1.printList()
