"""
876. Middle of the Linked List
src: https://leetcode.com/problems/middle-of-the-linked-list/

Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

Example 1:
Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.

Example 2:
Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
"""

from typing import Optional
from pprint import pprint

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def get_len(head: ListNode) -> int:
    lookup_head = head
    list_len = 0
    while lookup_head:
        lookup_head = lookup_head.next
        list_len += 1

    return list_len


def middle_of_linked_list(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head:
        return None

    list_len = get_len(head)

    middle_index = list_len // 2
    idx = 0

    lookup_head = head
    while lookup_head:
        if idx == middle_index:
            return lookup_head

        lookup_head = lookup_head.next
        idx += 1


def middle_of_linked_list_better(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head:
        return None

    fast = head
    slow = head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    return slow


def test_middle_of_linked_list():
    list1 = ListNode(1)
    list1.next = ListNode(2)
    list1.next.next = ListNode(3)
    list1.next.next.next = ListNode(4)
    list1.next.next.next.next = ListNode(5)

    assert middle_of_linked_list(list1) == list1.next.next
    assert middle_of_linked_list_better(list1) == list1.next.next
