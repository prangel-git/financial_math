def one_period_binomial_pricing(
        stock_initial_price,
        up_factor,
        down_factor,
        bond_return,
        derivative_payoff
    ):

    stock_up = stock_initial_price * up_factor
    stock_down = stock_initial_price * down_factor
    derivative_up = derivative_payoff(stock_up)
    derivative_down = derivative_payoff(stock_down)
    
    probability_up = (bond_return - down_factor) / (up_factor - down_factor)

    probability_down = (up_factor - bond_return) / (up_factor - down_factor)

    price = (probability_up * derivative_up + probability_down * derivative_down) / bond_return

    stock_allocation = (derivative_up - derivative_down) / (stock_up - stock_down)

    bond_allocation = price - stock_allocation * stock_initial_price

    return price, stock_allocation, bond_allocation