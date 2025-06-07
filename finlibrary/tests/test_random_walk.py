from finlibrary.src.random_walk import RandomWalk

def test_random_walk_initialization():
    walk = RandomWalk()
    assert walk.position == 0 
    assert walk.probability == 0.5