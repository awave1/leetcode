"""
448. Find All Numbers Disappeared in an Array
LeetCode: https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

"""


def find_disappeared_numbers(nums: list[int]) -> list[int]:
    full_range = set(list(range(1, len(nums) + 1)))
    return list(full_range.difference(set(nums)))


def test_find_disappeared_numbers():
    assert find_disappeared_numbers([4, 3, 2, 7, 8, 2, 3, 1]) == [5, 6]
    assert find_disappeared_numbers([1, 1]) == [2]
