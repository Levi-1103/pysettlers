from typing import Optional
from BuildingType import BuildingType
from Player import *

class Building():
    def _init_(self, hasBuilding: None, buildingType : Optional[BuildingType] = BuildingType.Empty, owner: Optional[Player] = None ):
        self.hasBuilding  = hasBuilding
        self.buildingType = buildingType
        self.owner = owner

