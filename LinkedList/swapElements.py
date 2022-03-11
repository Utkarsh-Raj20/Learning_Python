class Node:
    def __init__(self, data):
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

    # * Swap elements in a linkedlist
    def swapElements(self, x, y):
        if self.head is None:
            return "this list contain no elements"
        else:
            tail = self.head
            while tail:
                if tail.data == x:
                    tail.data = y
                elif tail.data == y:
                    tail.data = x
                tail = tail.next

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


if __name__ == "__main__":
    lis = list(map(int, input("Input the array for linked list: ").strip().split()))
    l = LinkedList(lis)
    swap = list(map(int,input("Elements to swap: ").strip().split()))
    x = swap[0]
    y = swap[1]
    l.swapElements(x,y)
    l.printList()