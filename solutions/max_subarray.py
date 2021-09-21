"""
53. Maximum Subarray
src: https://leetcode.com/problems/maximum-subarray/

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.
"""


def max_subarray(nums: list[int]) -> int:
    """
    https://en.wikipedia.org/wiki/Maximum_subarray_problem#Kadane's_algorithm
    """
    max_sum = nums[0]
    current_sum = nums[0]

    for num in nums[1:]:
        current_sum = max(current_sum + num, num)
        max_sum = max(current_sum, max_sum)

    return max_sum


def test_max_subarray():
    assert max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert max_subarray([1]) == 1
    assert max_subarray([5, 4, -1, 7, 8]) == 23
    assert max_subarray([-2, -1]) == -1


print(max_subarray([-2, -1]))
# print(max_subarray([1]))
# max_subarray([5, 4, -1, 7, 8])
