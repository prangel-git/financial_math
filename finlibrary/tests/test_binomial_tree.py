
from finlibrary.src.binomial_tree import one_period_binomial_pricing

def test_one_period_binomial_pricing():
    stock_initial_price = 4
    up_factor = 2
    down_factor = 1/2
    bond_return = 5/4
    derivative_expiry = 1
    strike = 5
    derivative_payoff = lambda s_N: max(s_N-strike, 0)

    derivative_price, stock_allocation, bond_allocation = one_period_binomial_pricing(
        stock_initial_price,
        up_factor,
        down_factor,
        bond_return,
        derivative_expiry,
        derivative_payoff
    )

    assert derivative_price == 1.2
    assert stock_allocation == 1/2
    assert bond_allocation == 0.8

