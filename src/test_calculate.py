from calculate import add_func


def test_add_func():
    assert add_func(1, 2) == 3
    assert add_func(0, 0) == 0
    assert add_func(-1, -2) == -3
    assert add_func(2, 2) == 4
    assert add_func(4, 6) == 10
    add_func(2, 5) == 7
