from .ticker import TickerDependent


class RandomWalk(TickerDependent):
    def __init__(self, ticker, probability=0.5):
        super().__init__(ticker)
        self.position = 0
        self.probability = probability