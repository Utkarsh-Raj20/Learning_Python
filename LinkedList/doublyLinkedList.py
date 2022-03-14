from tkinter import N
from pygame import init


class Node:
    def __init__(self, data):
        self.prev = None
        self.next = None
        self.data = data


class DoublyLinkedList:
    def __init__(self, list=None):
        self.head = None
        self.tail = None
        self.values = list

    # TODO make Linkedlist from given list
    # TODO push a element at start
    # TODO append a element at end
    # TODO insert a element at a specific position
    # TODO delete a specific node
    # TODO delete a node at a specific position
    # TODO make the list circular
    # TODO print the list
