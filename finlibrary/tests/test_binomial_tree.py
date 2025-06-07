from finlibrary.src.ticker import Ticker
from finlibrary.src.binomial_tree import BinomialTree

def test_binomial_tree():
    ticker = Ticker()
    probability_up = 0.5
    initial_value = 1
    tree = BinomialTree(ticker, initial_value, probability_up)
    assert tree.initial_value == 1
    assert tree.probability_up == 0.5
