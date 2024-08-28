# File for handling ray casting

import pygame as pg
import math
from Map import Map
from Player import Player

class RayCaster:
    def __init__(self, map: Map, player: Player) -> None:
        self.map = map
        self.player = player

    def __cast_ray(self):
        pass

    def update(self, dt_sec: float):
        pass