from data_structure.BinaryTree import BinaryTree
from data_structure.CircularDoublyLinkedList import CircularDoublyLinkedList
from player.Player import Player
import tkinter as tk
from tkinter import simpledialog, filedialog, ttk
from os import listdir
from os.path import isfile, isdir


def list_directory(path):
    return [obj for obj in listdir(path) if isfile(path + obj)]


class UserInteraction:
    def __init__(self):
        self.open_directory = ""
        self.song = None
        self.load_files = False
        self.bt = BinaryTree()
        self.cl = CircularDoublyLinkedList()
        self.menu = "--- Escoja una opción ---\n" \
                    "0.- Salir\n" \
                    "1.- Escojer la carpeta\n" \
                    "2.- Seleccionar canciones\n" \
                    "3.- Reproducir\n" \
                    "4.- Siguiente canción\n" \
                    "5.- Anterior canción\n" \
                    "6.- Pausar\n" \
                    "7.- Resumir\n" \
                    "8.- Detener"

        self.root = tk.Tk()
        self.root.withdraw()

    def start(self):
        option = 1

        while option != 0:
            try:
                option = int(simpledialog.askstring(title="Escoja una opción",
                                                    prompt=self.menu))
                self.choose_option(option)
            except ValueError:
                simpledialog.messagebox.showinfo(title="Atención",
                                                 message="Inserte una opción correcta")
            except TypeError:
                pass
        # self.song.stop()

    def choose_option(self, option):
        if not self.load_files and option != 1:
            simpledialog.messagebox.showinfo(title="Atención", message="Primero debe seleccionar una carpeta")
            return

        if option == 1:
            self.find_files()
        elif option == 2:
            self.choose_music()
        elif option == 3:
            self.play()
        elif option == 4:
            self.next()
        elif option == 5:
            self.previous()
        elif option == 6:
            self.pause()
        elif option == 7:
            self.resume()
        elif option == 8:
            self.stop()

    def pause(self):
        self.song.player.pause()

    def resume(self):
        self.song.player.resume()

    def stop(self):
        self.song.player.stop()

    def next(self):
        if self.song.next is not None:
            self.song.player.stop()
            # print(self.song.player.get_name())
            self.song = self.song.next
            # print(self.song.player.get_name())
            self.song.player.play()

    def previous(self):
        if self.song.previous is not None:
            self.song.player.stop()
            self.song = self.song.previous
            self.song.player.play()

    def play(self):
        if self.cl.get_size() != 0:
            self.song = self.cl.get_start()
            self.song.player.play()

    def find_files(self):
        self.open_directory = filedialog.askdirectory()
        files = list_directory(self.open_directory + "/")

        if len(files) != 0:
            self.load_file(files)
        # print(open_directory + "/")
        # print(self.files)

    def load_file(self, files):
        for file in files:
            self.bt.add(Player(self.open_directory + "/" + file))

        self.bt.show_tree()
        self.load_files = True

    def choose_music(self):
        names_array = self.bt.get_names()
        names = ""
        for name, i in enumerate(names_array):
            names += "\n" + str(name) + ".-" + str(i)

        song = -1
        try:
            song = int(simpledialog.askstring(title="Escoja una canción",
                                              prompt=names))
        except AttributeError:
            pass

        if song >= 0 or song <= len(names_array) - 1:
            # print(self.cl.get_size())
            self.cl.add(self.bt.find(names_array[song]))
            print(self.cl.get_size())
            print(names_array[song])
        else:
            simpledialog.messagebox.showinfo(title="Atención", message="No existe esa canción, verifique el indice")
