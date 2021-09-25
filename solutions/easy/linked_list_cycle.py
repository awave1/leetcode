"""
141. Linked List Cycle
src: https://leetcode.com/problems/linked-list-cycle/

Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

Example 2:
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

Example 3:
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
"""

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def has_cycle(head: ListNode, pos: Optional[int] = None) -> bool:
    """
    src: https://en.wikipedia.org/wiki/Cycle_detection
    """
    if not head:
        return False

    slow = head
    fast = head

    while fast.next and fast.next.next:
        fast = fast.next.next
        slow = slow.next

        if fast == slow:
            return True

    return False


list1 = ListNode(3)
list1.next = ListNode(2)
list1.next.next = ListNode(0)
list1.next.next.next = ListNode(-4)
list1.next.next.next = list1.next


def test_has_cycle():
    assert has_cycle(list1, 1) == True


has_cycle(list1, 1)
