"""
217. Contains Duplicate
LeetCode: https://leetcode.com/problems/contains-duplicate/
"""


def contains_duplicate(nums: list[int]) -> bool:
    seen = set([])

		for num in nums:
			if num in seen:
				return True
			seen.add(num)
		
		return False
