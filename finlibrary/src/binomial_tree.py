def binomial_tree_values(initial_value, up_factor, down_factor, period):
    return [(up_factor ** k) * (down_factor ** (period - k)) for k in range(period+1)]