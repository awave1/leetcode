"""
448. Find All Numbers Disappeared in an Array
src: https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

"""


def find_disappeared_numbers(nums: list[int]) -> list[int]:

    n = len(nums)

    full_range = set(list(range(1, n + 1)))
    # solution using a filter
    # list(filter(lambda x: x not in nums, list(range(1, n + 1))))
    return list(full_range.difference(set(nums)))


def find_disappeared_numbers_improved(nums: list[int]) -> list[int]:
    """
    Cyclic sort solution
    """

    n = len(nums)
    idx = 0

    # sort the nums array
    while idx < n:
        # correct position of current number
        # since the list is range [1, n], where n is len(nums)
        # when sorted, for example index of 1 should be 0, index of 2 is 1 and etc
        pos = nums[idx] - 1
        if nums[idx] != nums[pos]:
            # swap the elements
            # expanded version (in case I forget lmao)
            # temp = nums[idx]
            # nums[idx] = nums[pos]
            # nums[pos] = temp
            nums[idx], nums[pos] = nums[pos], nums[idx]
        else:
            idx += 1

    # missed_nums = [i + 1 for i in range(n) if nums[i] != i + 1]
    missed_nums = []
    for i in range(n):
        if nums[i] != i + 1:
            missed_nums.append(i + 1)

    return missed_nums


def test_find_disappeared_numbers():
    assert find_disappeared_numbers([4, 3, 2, 7, 8, 2, 3, 1]) == [5, 6]
    assert find_disappeared_numbers([1, 1]) == [2]


def test_find_disappeared_numbers_improved():
    assert find_disappeared_numbers_improved([4, 3, 2, 7, 8, 2, 3, 1]) == [5, 6]
    assert find_disappeared_numbers_improved([1, 1]) == [2]
