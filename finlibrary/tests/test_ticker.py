from finlibrary.src.ticker import Ticker

def test_get_period():
    ticker = Ticker()
    assert ticker.period == 0

def test_tick_advances_time():
    ticker = Ticker()
    ticker.tick()
    assert ticker.period == 1