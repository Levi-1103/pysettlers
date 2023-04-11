import random

class DevelopmentCards:
    def __init__(self):
        self.cards = {
            'knight': 14,
            'year_of_plenty': 2,
            'monopoly': 2,
            'road_building': 2,
            'victory_point': 5
        }
        self.discarded = []  # list to hold discarded cards
    
    def draw_card(self):
        # randomly choose a card type that still has cards remaining
        available_cards = [card_type for card_type, count in self.cards.items() if count > 0]
        if not available_cards:
            return None  # no cards left to draw
        chosen_type = random.choice(available_cards)
        # remove one card of the chosen type and return it
        self.cards[chosen_type] -= 1
        return chosen_type
    
    def discard_card(self, card_type):
        # discard a development card of the specified type
        if card_type in self.cards:
            self.cards[card_type] -= 1
            self.discarded.append(card_type)
