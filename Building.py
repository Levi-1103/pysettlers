from BuildingType import BuildingType

class Building:
    def _init_(self):
        self.hasBuilding = False
        self.buildingType = BuildingType.Empty
        self.owner = None

