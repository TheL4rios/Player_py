import pygame
import os


class Player:
    def __init__(self, path):
        self.path = path
        pygame.mixer.init()
        self.player = pygame.mixer_music

    def play(self):
        self.player.load(self.path)
        self.player.play()

    def open_file(self):
        self.player.load(self.path)

    def pause(self):
        self.player.pause()

    def resume(self):
        self.player.unpause()

    def stop(self):
        self.player.stop()

    def get_name(self):
        return os.path.basename(self.path)
