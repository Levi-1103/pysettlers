from typing import Optional
from Player import *
class Road():
    def __init__(self, owner : Optional[Player] = None):
        self.isEmpty = True
        self.owner = owner
