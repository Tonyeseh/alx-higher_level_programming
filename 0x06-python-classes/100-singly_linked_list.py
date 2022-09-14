#!/usr/bin/python3
""" Class Node """


class Node:
    """ Defines a node of singly linked list """

    def __init__(self, data, next_node=None):
        """ Initialises a Node object

        Args:
            data (int): data part of the new node
            next_node (Node object): next node in the list
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """ Getter for data attribute """
        return self.__data

    @data.setter
    def data(self, value):
        """ Setter for data attribute """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """ Getter for next_node attribute """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """ Setter for next_node attribute """
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """ Defines a SinglyLinkedList object"""

    def __init__(self):
        """ Initialises a new SinglyLinkedList Node """
        self.__head = None

    def sorted_insert(self, value):
        """ Inserts new node into a listed list in sorted manner.

        Args:
            value (int): value of new Node object
        """
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            tmp = self.__head
            while(tmp.next_node is not None and tmp.next_node.data < value):
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new

    def __str__(self):
        """ Defines the print() representation of a SinglyLinkedList """
        tmp = self.__head
        node_info = []
        while tmp is not None:
            node_info.append(str(tmp.data))
            tmp = tmp.next_node
        return "\n".join(node_info)
