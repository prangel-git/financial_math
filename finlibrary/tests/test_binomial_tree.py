
import pytest

from finlibrary.src.binomial_tree import one_period_binomial_pricing, multiperiod_binomial_pricing, binomial_tree_values

def test_one_period_binomial_pricing():
    stock_initial_price = 4
    up_factor = 2
    down_factor = 1/2
    bond_return = 5/4
    strike = 5
    derivative_payoff = lambda s_N: max(s_N-strike, 0)

    derivative_price, stock_allocation, bond_allocation = one_period_binomial_pricing(
        stock_initial_price,
        up_factor,
        down_factor,
        bond_return,
        derivative_payoff
    )

    assert derivative_price == 1.2
    assert stock_allocation == 1/2
    assert bond_allocation == -0.8

def test_multiperiod_binomial_pricing():
    stock_initial_price = 4
    up_factor = 2
    down_factor = 1/2
    bond_return = 5/4
    derivative_expiry = 3
    strike = 6
    derivative_payoff = lambda s_N: max(s_N-strike, 0)

    hedging_tree = multiperiod_binomial_pricing(
        stock_initial_price,
        up_factor,
        down_factor,
        bond_return,
        derivative_payoff,
        derivative_expiry
    )

    assert hedging_tree.price == pytest.approx(2.048)
    assert hedging_tree.stock_allocation == pytest.approx(0.7466666666666666)
    assert hedging_tree.bond_allocation == pytest.approx(-0.9386666666666663) 