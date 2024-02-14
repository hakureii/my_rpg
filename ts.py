import json
import pygame
pygame.init()

class TileMaps:
    def __init__(self):
        pass

class Deco:
    def __init__(self) -> None:
        self.image = []
        with open("tiny_sword/Deco.json") as file:
            pngs = json.load(file)
        for path in pngs:
            self.image.append(pygame.image.load(path).convert())

    def mashroom(self, size: int = 0):
        rect = pygame.Rect(0, 0, 64, 64)
        sprite = pygame.Surface((64, 64))
        sprite.blit(self.image[size], (0,0), rect)
        sprite.set_colorkey((0,0,0))
        return sprite

    def rock(self, size: int = 3):
        rect = pygame.Rect(0, 0, 64, 64)
        sprite = pygame.Surface((64, 64))
        sprite.blit(self.image[size], (0,0), rect)
        sprite.set_colorkey((0,0,0))
        return sprite

    def grass(self, size: int = 6):
        rect = pygame.Rect(0, 0, 64, 64)
        sprite = pygame.Surface((64, 64))
        sprite.blit(self.image[size], (0,0), rect)
        sprite.set_colorkey((0,0,0))
        return sprite

    def cactus(self, size: int = 0):
        if size == 0:
            size = 9
        else:
            size = 10
        rect = pygame.Rect(0, 0, 64, 64)
        sprite = pygame.Surface((64, 64))
        sprite.blit(self.image[size], (0,0), rect)
        sprite.set_colorkey((0,0,0))
        return sprite
    def fruit(self, size: int = 11):
        if size == 0:
            size = 11
        else:
            size = 12
        rect = pygame.Rect(0, 0, 64, 64)
        sprite = pygame.Surface((64, 64))
        sprite.blit(self.image[size], (0,0), rect)
        sprite.set_colorkey((0,0,0))
        return sprite
    def bone(self, size: int = 13):
        if size == 0:
            size = 13
        else:
            size = 14
        rect = pygame.Rect(0, 0, 64, 64)
        sprite = pygame.Surface((64, 64))
        sprite.blit(self.image[size], (0,0), rect)
        sprite.set_colorkey((0,0,0))
        return sprite
    def sign(self, allow: bool = False):
        if allow:
            size = 16
        else:
            size = 15
        rect = pygame.Rect(0, 0, 64, 128)
        sprite = pygame.Surface((64, 128))
        sprite.blit(self.image[size], (0,0), rect)
        sprite.set_colorkey((0,0,0))
        return sprite

    def scarecrow(self):
        rect = pygame.Rect(0, 0, 192, 192)
        sprite = pygame.Surface((192, 192))
        sprite.blit(self.image[17], (0,0), rect)
        sprite.set_colorkey((0,0,0))
        return sprite

class Effects:
    def __init__(self) -> None:
        self.fire_frame = 0
        self.explosion_frame = 0
        self.image = dict()
        with open("tiny_sword/Effects.json") as file:
            pngs = json.load(file)
        for k, v in pngs.items():
            self.image[k] = pygame.image.load(v).convert()

    def explosion(self):
        x = 192 * self.explosion_frame
        if self.explosion_frame >= 8:
            self.explosion_frame = 0
            return None
        else:
            self.explosion_frame += 1
        rect = pygame.Rect(x, 0, 192, 192)
        sprite = pygame.Surface((192, 192))
        sprite.blit(self.image["Explosion"], (0,0), rect)
        sprite.set_colorkey((0,0,0))
        return sprite

    def fire(self):
        x = 128 * self.fire_frame
        if self.fire_frame >= 6:
            self.fire_frame = 0
        else:
            self.fire_frame += 1
        rect = pygame.Rect(x, 0, 128, 128)
        sprite = pygame.Surface((128, 128))
        sprite.blit(self.image["Fire"], (0,0), rect)
        sprite.set_colorkey((0,0,0))
        return sprite

class Factions:
    def __init__(self):
        self.dynamite_frame = 0
        self.image = pygame.image.load("Dynamite.png").convert()

    def dynamite(self):
        x = 64 * self.dynamite_frame
        if self.dynamite_frame >= 5:
            self.dynamite_frame = 0
        else:
            self.dynamite_frame += 1
        rect = pygame.Rect(x, 0, 64, 64)
        sprite = pygame.Surface((64, 64))
        sprite.blit(self.image, (0,0), rect)
        sprite.set_colorkey((0,0,0))
        return sprite

class Resources:
    pass
class Terrain:
    pass
class UI:
    pass
