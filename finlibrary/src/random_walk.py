from .ticker import TickerDependent
from random import random

class RandomWalk(TickerDependent):
    def __init__(self, ticker, probability=0.5):
        super().__init__(ticker)
        self.position = 0
        self.probability = probability
    
    def update(self):
        step = 2 * (random() < 0.5) - 1
        self.position += step
        