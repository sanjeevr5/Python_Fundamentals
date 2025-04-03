# Definition for a Linked List node
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# from ds_v1.LinkedList.LinkedList import ListNode


def remove_nth_last_node(head, n):
    left = head
    right = head
    while n:
        right = right.next
        n -= 1
    if not right:
        return head.next
    while right and right.next:
        left = left.next
        right = right.next
    left.next = left.next.next
    return head
