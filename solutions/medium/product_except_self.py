"""
238. Product of Array Except Self
src: https://leetcode.com/problems/product-of-array-except-self/

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
"""

from functools import reduce


def product_except_self_brute_force(nums: list[int]) -> list[int]:
    """
    O(n^2)
    """
    result = [None] * len(nums)

    for i in range(len(nums)):
        for j, num2 in enumerate(nums):
            if i != j:
                result[i] = num2 if result[i] == None else num2 * result[i]

    return result


def product_except_self_with_reduce(nums: list[int]) -> list[int]:
    """
    O(n^2)
    """
    result = []

    for i in range(len(nums)):
        sub_list = nums[i + 1 :] + nums[:i]
        result.append(reduce(lambda x, y: x * y, sub_list))

    return result


def product_except_self(nums: list[int]) -> list[int]:
    """
    O(n)
    """
    nums_len = len(nums)
    left = [1 for _ in range(nums_len)]

    for i in range(1, nums_len):
        left[i] = left[i - 1] * nums[i - 1]

    right = [1 for _ in range(nums_len)]
    for i in range(nums_len - 2, -1, -1):
        right[i] = right[i + 1] * nums[i + 1]

    result = []
    for i in range(nums_len):
        result.append(left[i] * right[i])

    return result


def test_product_except_self_brute_force():
    assert product_except_self_brute_force([1, 2, 3, 4]) == [24, 12, 8, 6]
    assert product_except_self_brute_force([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]


def test_product_except_self_with_reduce():
    assert product_except_self_with_reduce([1, 2, 3, 4]) == [24, 12, 8, 6]
    assert product_except_self_with_reduce([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]


def test_product_except_self():
    assert product_except_self([1, 2, 3, 4]) == [24, 12, 8, 6]
    assert product_except_self([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]
