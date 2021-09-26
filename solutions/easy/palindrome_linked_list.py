"""
234. Palindrome Linked List
src: https://leetcode.com/problems/palindrome-linked-list/

Given the head of a singly linked list, return true if it is a palindrome.

Example 1:
Input: head = [1,2,2,1]
Output: true

Example 2:
Input: head = [1,2]
Output: false
"""

from solutions.data_structures.linked_list import ListNode


def is_palindrome(head: ListNode) -> bool:
    stack = []
    lookup_head = head

    while lookup_head:
        stack.append(lookup_head.val)
        lookup_head = lookup_head.next

    lookup_head = head
    while len(stack) != 0 and lookup_head:
        el = stack.pop()

        if lookup_head.val != el:
            return False

        lookup_head = lookup_head.next

    return True


list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(2)
list1.next.next.next = ListNode(1)

list2 = ListNode(1)
list2.next = ListNode(2)


def test_is_palindrome():
    assert is_palindrome(list1) == True
    assert is_palindrome(list2) == False


is_palindrome(list1)
