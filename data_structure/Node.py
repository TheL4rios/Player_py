class Node:
    LIST = 0
    TREE = 1

    def __init__(self, player, previous, next, type):
        self.player = player

        if type == self.LIST:
            self.previous = previous
            self.next = next
            return

        self.right = next
        self.left = previous

