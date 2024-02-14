#!/usr/bin/env python

# import pygame_sdl2
# pygame_sdl2.import_as_pygame()

import os
import sys
import pygame
from sprite_loader import TileMap
pygame.init()

class Config:
    def __init__(self) -> None:
        self.status_running = True
        self.fps = 60
        self.dw = 1024
        self.dh = 576

class Game:
    def __init__(self) -> None:
        self.config = Config()
        self.clock = pygame.time.Clock()
        pygame.display.set_mode((self.config.dw, self.config.dh))

    def main(self):
        self.events()
        self.keyman()
        pygame.display.update()
        self.clock.tick(self.config.fps)

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.config.status_running = False

    def keyman(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]:
            print("UP")
        if pressed[pygame.K_DOWN]:
            print("DOWN")
        if pressed[pygame.K_LEFT]:
            print("LEFT")
        if pressed[pygame.K_RIGHT]:
            print("RIGHT")
        if pressed[pygame.K_CAPSLOCK]:
            print("SPACE")
        if pressed[pygame.K_q]:
            self.config.status_running = False

    def quit(self):
        pygame.quit()
        os.system("rm -rf __pycache__")
        sys.exit(0)

game = Game()

if __name__ == "__main__":
    while game.config.status_running:
        game.main()
    else:
        game.quit()
