"""
303. Range Sum Query - Immutable
src: https://leetcode.com/problems/range-sum-query-immutable/

Given an integer array nums, handle multiple queries of the following type:

1. Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.

Implement the NumArray class:

- NumArray(int[] nums) Initializes the object with the integer array nums.
- int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).


Example 1:
Input
["NumArray", "sumRange", "sumRange", "sumRange"]
[[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
Output
[null, 1, -1, -3]

Explanation
NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
numArray.sumRange(0, 2); // return (-2) + 0 + 3 = 1
numArray.sumRange(2, 5); // return 3 + (-5) + 2 + (-1) = -1
numArray.sumRange(0, 5); // return (-2) + 0 + 3 + (-5) + 2 + (-1) = -3
"""


class NumArray:
    def __init__(self, nums: list[int]):
        self.nums = nums
        self.sums = []

        sum = 0
        for n in nums:
            sum += n
            self.sums.append(sum)

        print(self.sums)

    def sum_range_using_sum(self, left: int, right: int) -> int:
        return sum(self.nums[left : right + 1])

    def sum_range(self, left: int, right: int) -> int:
        if left == 0:
            return self.sums[right]

        return self.sums[right] - self.sums[left - 1]

    def sum_range_loop(self, left: int, right: int) -> int:
        sum_result = 0

        for i in range(left, right + 1):
            sum_result += self.nums[i]

        return sum_result


def test_sum_range():
    num_array = NumArray([-2, 0, 3, -5, 2, -1])
    assert num_array.sum_range(left=0, right=2) == 1
    assert num_array.sum_range(left=2, right=5) == -1
    assert num_array.sum_range(left=0, right=5) == -3
