"""
217. Contains Duplicate
LeetCode: https://leetcode.com/problems/contains-duplicate/

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
"""


def contains_duplicate(nums: list[int]) -> bool:
    seen = set([])

    for num in nums:
        if num in seen:
            return True
        seen.add(num)

    return False


def test_contians_duplicate():
    assert contains_duplicate([1, 2, 3, 1])
    assert contains_duplicate([1, 2, 3, 4]) == False
    assert contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2])
