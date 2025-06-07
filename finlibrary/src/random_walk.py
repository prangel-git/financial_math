from .ticker import TickerDependent
from random import random

class RandomWalk(TickerDependent):
    def __init__(self, ticker, probability_up=0.5):
        super().__init__(ticker)
        self.position = 0
        self.probability_up = probability_up
    
    def update(self):
        step = 2 * (random() < self.probability_up) - 1
        self.position += step
        