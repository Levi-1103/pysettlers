from TileResource import TileResource


class Player:
    """
    A class to represent a Player.
    ...

    Attributes
    ----------
    name : str
        string for player name
    color : str
        string for player colour

    Methods
    -------
    __init__():
        Constructs Player Object
    add_resource():
        Adds resource to Player
    remove_resource():
        Remove resource from Player
    add_development_card():
        Adds developement card to Player
    remove_development_card():
        Removes developement card from PLayer
    add_road():
        Stores road for PLayer
    add_settlement():
        Stores Settlement for PLayer
    add_city():
        Stores City for PLayer
    add_victory_point():
        Adds a victory point to player victory points
    remove_victory_point():
        Removes a victory point from player

    """

    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.resources = {
            TileResource.Lumber: 1,
            TileResource.Brick: 1,
            TileResource.Wool: 1,
            TileResource.Grain: 1,
            TileResource.Ore: 1,
        }
        self.development_cards = []
        self.roads = []
        self.settlements = []
        self.cities = []
        self.victory_points = 0

    def add_resource(self, resource, amount):
        if resource != TileResource.Desert:
            self.resources[resource] += amount

    def remove_resource(self, resource, amount):
        if self.resources[resource] >= amount:
            self.resources[resource] -= amount
            return True
        else:
            return False

    def add_development_card(self, card):
        self.development_cards.append(card)

    def remove_development_card(self, card):
        if card in self.development_cards:
            self.development_cards.remove(card)
            return True
        else:
            return False

    def add_road(self, road):
        self.roads.append(road)

    def add_settlement(self, settlement):
        self.settlements.append(settlement)

    def add_city(self, city):
        self.cities.append(city)

    def add_victory_point(self):
        self.victory_points += 1

    def remove_victory_point(self):
        if self.victory_points > 0:
            self.victory_points -= 1
            return True
        else:
            return False
