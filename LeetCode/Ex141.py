# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Ex141(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        i, j = head, head
        while j != None and j.next != None:
            
            if j.next == i:
                return True
            
            i = i.next
            j = j.next.next
        return False
