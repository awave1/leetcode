"""
136. Single Number
src: https://leetcode.com/problems/single-number/

Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.
"""


def single_number(nums: list[int]) -> int:
    if len(nums) == 1:
        return nums[0]

    seen = {}
    for num in nums:
        str_num = str(num)
        if str_num in seen:
            seen[str_num] += 1
        else:
            seen[str_num] = 1

    list_vals = list(seen.values())
    unique_num_index = list_vals.index(1)
    unique_num = int(list(seen.keys())[unique_num_index])

    return unique_num


def test_single_number():
    assert single_number([2, 2, 1]) == 1
    assert single_number([4, 1, 2, 1, 2]) == 4
    assert single_number([1]) == 1
