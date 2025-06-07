from finlibrary.src.binomial_tree import binomial_tree_values

def test_binomial_tree_values():
    initial_value = 1
    up_factor = 2
    down_factor = 0.5
    possible_values = binomial_tree_values(initial_value, up_factor, down_factor, 2)
    expected_values = [0.25, 1, 4]
    assert possible_values == expected_values
