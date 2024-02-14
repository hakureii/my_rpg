import pygame

class TileMap:
    def __init__(self, filepath) -> None:
        self.image = pygame.image.load(filepath).convert()

    def get_sprite(self, x, y, size:tuple=(32,32), c_key:tuple=()):
        rect = pygame.Rect(x, y, size[0], size[1])
        sprite = pygame.Surface(size)
        sprite.blit(self.image, (0,0), rect)
        if c_key:
            sprite.set_colorkey(c_key)

        return sprite
