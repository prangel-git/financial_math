from .random_walk import RandomWalk

class BinomialTree(RandomWalk):
    def __init__(self, ticker, initial_value=1, probability_up=0.5):
        super().__init__(ticker, probability_up)
        self.initial_value = initial_value
        self.probability_up = probability_up