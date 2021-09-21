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


def counting_bits(n: int) -> list[int]:
    bits = []
    for i in range(0, n + 1):
        bits.append(bin(i).count("1"))

    return bits


def test_counting_bits():
    assert counting_bits(2) == [0, 1, 1]
    assert counting_bits(5) == [0, 1, 1, 2, 1, 2]


counting_bits(2)
