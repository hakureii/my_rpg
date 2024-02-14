import pygame

class TileMaps:
    def __init__(self) -> None:
        self.ground_flat = pygame.image.load("./tiny_sword/Terrain/Ground/Tilemap_Flat.png").convert()
        self.ground_elevation = pygame.image.load("./tiny_sword/Terrain/Ground/Tilemap_Elevation.png").convert()
