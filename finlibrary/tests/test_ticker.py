from finlibrary.src.ticker import Ticker

def test_get_period():
    ticker = Ticker()
    assert ticker.period == 0