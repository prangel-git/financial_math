from finlibrary.src.random_walk import RandomWalk
from finlibrary.src.ticker import Ticker

def test_random_walk_initialization():
    ticker = Ticker()
    walk = RandomWalk(ticker)
    assert walk.position == 0 
    assert walk.probability_up == 0.5

def test_random_walk_evolution():
    ticker = Ticker()
    walk = RandomWalk(ticker)
    walk.update()
    assert walk.position == 1 or walk.position == -1