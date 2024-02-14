#!/usr/bin/env python

import pygame_sdl2
pygame_sdl2.import_as_pygame()

import os
import sys
import time
import pygame
from ts import Deco, Effects, Factions
pygame.init()

class Config:
    def __init__(self) -> None:
        self.status_running = True
        self.fps = 30
        self.dw = 1024
        self.dh = 576
        self.player = [0,0]

class Font:
    def __init__(self, game, font_path:str, color:tuple=(0,0,0), size:int=12):
        self.font = pygame.font.Font(font_path, size)
        self.color = color
        self.game = game

    def draw(self, text, x, y):
        text = self.font.render(text, True, pygame.Color(self.color))
        self.game.display.blit(text, (x, y))

class Game:
    def __init__(self) -> None:
        self.boom = []
        self.config = Config()
        self.clock = pygame.time.Clock()
        self.display = pygame.display.set_mode((self.config.dw, self.config.dh))
        self.font = Font(self, "/data/data/com.termux/files/usr/share/fonts/TTF/DejaVuSans.ttf")
        self.effects = Effects()
        self.deco = Deco()
        self.factions = Factions()

    def main(self):
        self.events()
        self.display.fill((255,255,255))
        self.draw()
        pygame.display.flip()
        self.clock.tick(self.config.fps)

    def draw(self):
        self.font.draw(f"FPS: {int(self.clock.get_fps())}", 0,0)
        self.display.blit(self.effects.fire(),(0,0))
        self.display.blit(self.deco.mashroom(size=2), (192, 0))
        self.display.blit(self.deco.sign(True), (0, 192))
        self.display.blit(self.deco.scarecrow(), self.config.player)
        trash = []
        for i, bomb in enumerate(self.boom):
            self.display.blit(self.factions.dynamite(), bomb["Coord"])
            if (bomb["time"] + 1) < time.time():
                trash.append(i)
        for i in trash:
            explosion_sprite = self.effects.explosion()
            if explosion_sprite is not None:
                self.display.blit(explosion_sprite, (self.boom[i]["Coord"][0] - 64, self.boom[i]["Coord"][1] - 64))
            else:
                self.boom.pop(i)
        # self.display.blit(self.effects.explosion(), (300, 300))
        # self.display.blit(self.factions.dynamite(), (400, 400))

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.config.status_running = False
            if event.type == pygame.KEYDOWN:
                match event.key:
                    case pygame.K_ESCAPE:
                        self.config.status_running = False
                    case pygame.K_UP:
                        self.config.player[1] -= 32
                    case pygame.K_DOWN:
                        self.config.player[1] += 32
                    case pygame.K_LEFT:
                        self.config.player[0] -= 32
                    case pygame.K_RIGHT:
                        self.config.player[0] += 32
                    case pygame.K_HOME:
                        self.boom.append({"time": time.time(), "Coord": (self.config.player[0] + 64, self.config.player[1] + 128)})

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
