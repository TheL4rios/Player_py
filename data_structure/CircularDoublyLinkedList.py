from data_structure.Node import Node


class CircularDoublyLinkedList:

    def __init__(self):
        self.start = None
        self.size = 0

    def add(self, player):
        if self.start is None:
            self.start = Node(player, self.start, self.start, Node.LIST)
            self.size += 1
            return

        if self.size < 2:
            new_node = Node(player, self.start, self.start, Node.LIST)
            self.start.next = new_node
            self.start.previous = new_node
            self.size += 1
            return

        self.__add(player, self.start)

    def __add(self, player, node):
        if node.next != self.start:
            self.__add(player, node.next)
        else:
            new_node = Node(player, node, node.next, Node.LIST)
            node.next = new_node
            self.start.previous = new_node
            self.size += 1

    def remove(self):
        if self.size == 1:
            self.start = None
        elif self.size == 2:
            self.start.next = self.start
            self.start.previous = self.start
        else:
            self.__remove(self.start)
        self.size -= 1

    def __remove(self, node):
        if node.next != self.start:
            self.__remove(node.next)
        else:
            node = node.previous
            node.next = self.start
            self.start = node

    def get_start(self):
        return self.start

    def get_size(self):
        return self.size