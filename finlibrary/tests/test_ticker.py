from finlibrary.src.ticker import Ticker, MockTickerDependent

def test_get_period():
    ticker = Ticker()
    assert ticker.period == 0

def test_tick_advances_time():
    ticker = Ticker()
    ticker.tick()
    assert ticker.period == 1

def test_ticker_dependent_object_registers_as_a_dependency_of_ticker():
    ticker = Ticker()
    ticker_dependent = MockTickerDependent(ticker)
    assert ticker_dependent == ticker.dependencies[0]

def test_tick_ticks_ticker_dependent_objects():
    ticker = Ticker()
    ticker_dependent = MockTickerDependent(ticker)
    ticker.tick()
    assert ticker_dependent.times_updated == 1