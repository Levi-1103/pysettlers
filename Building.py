from typing import Optional
from BuildingType import BuildingType
from Player import *


class Building:
    def __init__(self, buildingType, owner):
        self.buildingType = buildingType
        self.owner = owner
        