class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        arr = []

        head = self
        while head:
            arr.append(str(head.val))
            head = head.next

        return f"[{', '.join(arr)}]"
