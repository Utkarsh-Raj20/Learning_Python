class Node:
    def __init__(self, data=None) -> None:
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end="--> ")
            temp = temp.next
        if temp == None:
            print("Null")


if __name__ == "__main__":
    l1 = LinkedList()
    l1.head = Node(1)
    second = Node(2)
    third = Node(3)
    fourth = Node(4)

    l1.head.next = second
    second.next = third
    third.next = fourth

    l1.printList()
