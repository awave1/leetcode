"""
287. Find the Duplicate Number
src: https://leetcode.com/problems/find-the-duplicate-number/

Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.
"""


from typing import Optional


def binary_search(nums: list[int], to_find: int) -> Optional[int]:
    def _binary_search(
        nums: list[int], to_find: int, left: int, right: int
    ) -> Optional[int]:
        if right >= left:
            middle = left + (right - left) // 2

            if nums[middle] == to_find:
                return middle

            elif nums[middle] > to_find:
                return _binary_search(nums, to_find, left=middle - 1, right=right)
            else:
                return _binary_search(nums, to_find, left=middle + 1, right=right)
        else:
            return None

    return _binary_search(nums, to_find, left=0, right=len(nums) - 1)


def find_duplicate_number_brute_force(nums: list[int]) -> int:
    nums_len = len(nums)
    last_idx = nums_len - 1

    i, j = 0, last_idx
    while i != last_idx:
        if j == i:
            i += 1
            j = last_idx

        if nums[i] == nums[j]:
            return nums[i]

        j -= 1


def find_duplicate_number(nums: list[int]) -> int:
    """
    explanation: https://www.youtube.com/watch?v=wjYnzkAhcNk
    """
    slow_idx = nums[0]
    fast_idx = nums[0]

    while True:
        slow_idx = nums[slow_idx]
        fast_idx = nums[nums[fast_idx]]

        if slow_idx == fast_idx:
            break

    slow_idx = nums[0]
    while slow_idx != fast_idx:
        slow_idx = nums[slow_idx]
        fast_idx = nums[fast_idx]

    return slow_idx


def test_find_duplicate_number_brute_force():
    assert find_duplicate_number_brute_force([1, 3, 4, 2, 2]) == 2
    assert find_duplicate_number_brute_force([3, 1, 3, 4, 2]) == 3
    assert find_duplicate_number_brute_force([1, 1]) == 1
    assert find_duplicate_number_brute_force([2, 2, 2, 2]) == 2


def test_find_duplicate_number():
    assert find_duplicate_number([1, 3, 4, 2, 2]) == 2
    assert find_duplicate_number([3, 1, 3, 4, 2]) == 3
    assert find_duplicate_number([1, 1]) == 1
    assert find_duplicate_number([2, 2, 2, 2]) == 2


find_duplicate_number([1, 3, 4, 2, 2])
find_duplicate_number([2, 2, 2, 2])
