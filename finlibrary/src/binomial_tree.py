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


def multiperiod_binomial_pricing(
        stock_initial_price,
        up_factor,
        down_factor,
        bond_return,
        derivative_payoff,
        derivative_expiry
    ):

    if derivative_expiry == 0:
        price = derivative_payoff(stock_initial_price)
        stock_allocation = 0
        bond_allocation = 0
        hedge_tree_up = None
        hedge_tree_down = None
    
        return BinaryTree(
            price,
            stock_allocation,
            bond_allocation,
            hedge_tree_up,
            hedge_tree_down
        )
    
    hedge_tree_up = multiperiod_binomial_pricing(
        stock_initial_price * up_factor,
        up_factor,
        down_factor,
        bond_return,
        derivative_payoff,
        derivative_expiry - 1
    )

    hedge_tree_down = multiperiod_binomial_pricing(
        stock_initial_price * down_factor,
        up_factor,
        down_factor,
        bond_return,
        derivative_payoff,
        derivative_expiry - 1
    )

    payoff_next_step_dict = {
        stock_initial_price * up_factor : hedge_tree_up.price,
        stock_initial_price * down_factor : hedge_tree_down.price
    }

    payoff_next_step = lambda s_1 : payoff_next_step_dict[s_1]

    price, stock_allocation, bond_allocation = one_period_binomial_pricing(
        stock_initial_price,
        up_factor,
        down_factor,
        bond_return,
        payoff_next_step
    )

    return BinaryTree(
        price,
        stock_allocation,
        bond_allocation,
        hedge_tree_up,
        hedge_tree_down
    ) 




class BinaryTree():
    def __init__(self, 
                 price, 
                 stock_allocation, 
                 bond_allocation,
                 up_tree,
                 down_tree):
        self.price = price
        self.stock_allocation = stock_allocation
        self.bond_allocation = bond_allocation
        self.up_tree = up_tree
        self.down_tree = down_tree