#!/usr/bin/python3

"""Single linked list module"""


class Node(object):
    '''
    Node class of a singly linked list

    Attributes:
        data (int): data of singly linked list
        next_node (int): node of singly linked list
    '''

    def __init__(self, data, next_node=None):
        ''' class constructor '''

        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        '''
        data getter

        Returns:
            data: the stored data

        '''

        return self.__data

    @data.setter
    def data(self, value):
        '''
        data attribute setter

        Args:
            value (int): value to be set in data

        Returns:
            TypeError: if value is not an int


        '''

        if type(value) != int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        '''
        next_node attribute getter

        Returns:
            next_node: pointer to next node
        '''

        return self.__next_node

    @next_node.setter
    def next_node(self, node):
        '''
        next_node attribute setter

        Args:
            node: singly linked list node

        Returns:
            TypeError: next_node can be None or must be a Node,

        '''

        if not isinstance(node, Node) and node is not None:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = node


class SinglyLinkedList(object):
    '''
    Singly linked list class

    Attributes:
        head (Node): pointer to the first node in singly linked list

    '''

    def __init__(self):
        '''Initializer for the SinglyLinkedList class'''

        self.__head = None

    def __str__(self):

        data_holder = ""
        pointer = self.__head

        while pointer:
            data_holder += str(pointer.data)
            if pointer.next_node:
                data_holder += '\n'
            pointer = pointer.next_node

        return data_holder

    def sorted_insert(self, value):
        '''
        Inserts data to a singly linked list in a sorted order

        Args:
            value (int): data value of the new node

        '''

        new_node = Node(value)

        if self.__head is None:
            self.__head = new_node
            return

        pointertonode = self.__head

        if pointertonode.data > value:
            self.__head = new_node
            new_node.next_node = pointertonode
            return

        while pointertonode:
            if pointertonode.next_node and \
                    pointertonode.next_node.data > value:
                new_node.next_node = pointertonode.next_node
                pointertonode.next_node = new_node
                return

            holdePreviousnode = pointertonode
            pointertonode = pointertonode.next_node

        # Insert node at the end
        holdePreviousnode.next_node = new_node
