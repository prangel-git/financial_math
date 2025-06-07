
class Ticker:
    def __init__(self):
        self.period = 0
        self.dependencies = []

    def tick(self):
        self.period += 1
        for dependencies in self.dependencies:
            dependencies.update()

    def register(self, ticker_dependent):
        self.dependencies.append(ticker_dependent)


class TickerDependent:
    def __init__(self, ticker):
        ticker.register(self)
    
    def update(self):
        pass


class MockTickerDependent(TickerDependent):
    def __init__(self, ticker):
        super().__init__(ticker)
        self.times_updated = 0
    
    def update(self):
        self.times_updated += 1