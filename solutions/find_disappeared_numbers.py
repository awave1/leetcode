"""
448. Find All Numbers Disappeared in an Array
src: https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

"""


def find_disappeared_numbers(nums: list[int]) -> list[int]:

    n = len(nums)

    full_range = set(list(range(1, n)))
    # solution using a filter
    # list(filter(lambda x: x not in nums, list(range(1, n))))
    return list(full_range.difference(set(nums)))


def find_disappeared_numbers_improved(nums: list[int]) -> list[int]:
    """
    Cyclic sort solution
    """

    n = len(nums)


def test_find_disappeared_numbers():
    assert find_disappeared_numbers([4, 3, 2, 7, 8, 2, 3, 1]) == [5, 6]
    assert find_disappeared_numbers([1, 1]) == [2]
    assert find_disappeared_numbers_improved([4, 3, 2, 7, 8, 2, 3, 1]) == [5, 6]
    assert find_disappeared_numbers_improved([1, 1]) == [2]
