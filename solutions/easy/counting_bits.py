"""
338. Counting Bits
src: https://leetcode.com/problems/counting-bits/

Given an integer n, return an array of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

Example 1:
Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10

Example 2:
Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101
"""


def counting_bits_brute_force(n: int) -> list[int]:
    bits = []
    for i in range(0, n + 1):
        bits.append(bin(i).count("1"))

    return bits


def counting_bits_dp(n: int) -> list[int]:
    """
    Strategy:
    0  0 0 0 0
    1  0 0 0 1
    2  0 0 1 0
    3  0 0 1 1
    4  0 1 0 0
    5  0 1 0 1
    6  0 1 1 0
    7  0 1 1 1

    memo[x] = memo[x >> 1] + x % 2
    """
    memo_bits = [0] * (n + 1)
    for i in range(0, n + 1):
        # i >> 1 = i / 2 (approx)
        prev_value = i >> 1
        even_bit = i % 2
        memo_bits[i] = memo_bits[prev_value] + even_bit

    return memo_bits[: n + 1]


def test_counting_bits_brute_force():
    assert counting_bits_brute_force(2) == [0, 1, 1]
    assert counting_bits_brute_force(5) == [0, 1, 1, 2, 1, 2]


def test_counting_bits_dp():
    assert counting_bits_dp(2) == [0, 1, 1]
    assert counting_bits_dp(5) == [0, 1, 1, 2, 1, 2]
