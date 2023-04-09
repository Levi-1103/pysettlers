class Player:
    def __init__(self,name,color):
        self.name = name
        self.color = color
        self.resources = {"wood": 0, "brick": 0, "sheep": 0, "wheat": 0, "ore": 0}
        self.development_cards = []
        self.roads = []
        self.settlements = []
        self.cities = []
        self.victory_points = 0

    def add_resource(self, resource, amount):
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
        
