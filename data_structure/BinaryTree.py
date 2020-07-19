from data_structure.Node import Node


class BinaryTree:
    def __init__(self):
        self.names = []
        self.root = None

    def __add(self, player, root):
        if root.player.get_name() < player.get_name():
            if root.right is None:
                root.right = Node(player, None, None, Node.TREE)
            else:
                self.__add(player, root.right)
            return

        if root.left is None:
            root.left = Node(player, None, None, Node.TREE)
        else:
            self.__add(player, root.left)

    def add(self, player):
        if self.root is None:
            self.root = Node(player, None, None, Node.TREE)
            return

        self.__add(player, self.root)

    def __find(self, name, root):
        if name > root.player.get_name():
            return self.__find(name, root.right)
        elif name < root.player.get_name():
            return self.__find(name, root.left)
        return root.player

    def find(self, name):
        if self.root is None:
            return None

        return self.__find(name, self.root)

    def show_tree(self):
        self.__show_tree(self.root)

    def __show_tree(self, node):
        if node is None:
            return

        self.__show_tree(node.left)
        print(node.player.get_name(), "\n")
        self.names.append(node.player.get_name())
        self.__show_tree(node.right)

    def get_names(self):
        return self.names
