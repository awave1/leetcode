from solutions.data_structures.linked_list import ListNode

"""
previous = None
current = head
following = head

while current:
    following = current.next
    current.next = previous
    previous = current
    current = following

p - previous
c - current
f - following

initialization:
  1 -> 2 -> 3 -> 4 -> 5   =>   5 -> 4 -> 3 -> 2 -> 1
p c
  f

iterations:
1)
     1 -> 2 -> 3 -> 4 -> 5       following = current.next
     c    f
  
p <- 1    2 -> 3 -> 4 -> 5       current.next = previous
          f

  <- 1    2 -> 3 -> 4 -> 5       previous = current
     c
     p    f
     

  <- 1    2 -> 3 -> 4 -> 5       current = following
     p    f
          c

2)
  <- 1 -> 2 -> 3 -> 4 -> 5       following = current.next
     p    c    f
  
  <- 1 <- 2    3 -> 4 -> 5       current.next = previous
     p    c    f
          
  <- 1 <- 2    3 -> 4 -> 5       previous = current
          c    f
          p

  <- 1 <- 2    3 -> 4 -> 5       current = following
          p    f
               c
3)
  <- 1 <- 2    3 -> 4 -> 5       following = current.next
          p         f
               c
  
  <- 1 <- 2 <- 3    4 -> 5       current.next = previous
          p         f
               c
          
  <- 1 <- 2 <- 3    4 -> 5       previous = current
               p    f
               c

  <- 1 <- 2 <- 3    4 -> 5       current = following
               p    f
                    c
4)
  <- 1 <- 2 <- 3    4 -> 5       following = current.next
               p         f
                    c
  
  <- 1 <- 2 <- 3 <- 4    5       current.next = previous
               p         f
                    c
          
  <- 1 <- 2 <- 3 <- 4    5       previous = current
                    p    f
                    c

  <- 1 <- 2 <- 3 <- 4    5       current = following
                    p    f
                         c
5)
  <- 1 <- 2 <- 3 <- 4    5       following = current.next
                    p       f
                         c
  
  <- 1 <- 2 <- 3 <- 4 <- 5       current.next = previous
                    p       f
                         c
          
  <- 1 <- 2 <- 3 <- 4 <- 5       previous = current
                         p  f
                         c

  <- 1 <- 2 <- 3 <- 4 <- 5       current = following
                         p  f
                            c
"""


def reverse_linked_list(head: ListNode) -> ListNode:
    previous = None
    current = head
    following = head

    while current:
        following = current.next
        current.next = previous
        previous = current
        current = following

    return previous


def test_reverse_linked_list():
    list1 = ListNode(1)
    list1.next = ListNode(2)
    list1.next.next = ListNode(3)
    list1.next.next.next = ListNode(4)

    assert reverse_linked_list(list1).__str__() == "[4, 3, 2, 1]"
