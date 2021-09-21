"""
70. Climbing Stairs
src: https://leetcode.com/problems/climbing-stairs/

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""


def climbing_stairs(n_stairs: int) -> int:
    if n_stairs < 0:
        return 0

    if n_stairs <= 1:
        return 1

    ways_to_climb = [None] * (n_stairs + 1)

    ways_to_climb[0] = 1
    ways_to_climb[1] = 1

    for i in range(2, n_stairs + 1):
        ways_to_climb[i] = ways_to_climb[i - 1] + ways_to_climb[i - 2]

    return ways_to_climb[n_stairs]


def climbing_stairs_recursive(n_stairs: int) -> int:
    if n_stairs < 0:
        return 0

    if n_stairs <= 1:
        return 1

    return climbing_stairs_recursive(n_stairs - 1) + climbing_stairs_recursive(
        n_stairs - 2
    )


def test_climbing_stairs():
    assert climbing_stairs(0) == 1
    assert climbing_stairs(1) == 1
    assert climbing_stairs(2) == 2
    assert climbing_stairs(3) == 3
    assert climbing_stairs(4) == 5


def test_climbing_stairs_recursive():
    assert climbing_stairs_recursive(0) == 1
    assert climbing_stairs_recursive(1) == 1
    assert climbing_stairs_recursive(2) == 2
    assert climbing_stairs_recursive(3) == 3
    assert climbing_stairs_recursive(4) == 5
