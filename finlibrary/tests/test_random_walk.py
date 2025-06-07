from finlibrary.src.random_walk import RandomWalk
from finlibrary.src.ticker import Ticker

def test_random_walk_initialization():
    ticker = Ticker()
    walk = RandomWalk(ticker)
    assert walk.position == 0 
    assert walk.probability == 0.5