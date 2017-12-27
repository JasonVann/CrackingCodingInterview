# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        n = len(lists)
        if n == 0:
            return []
        step = 1
        n2 = n
        #while step < n:
        while n2 > 1:
            i = 0
            lists2 = []

            while i < n2:
                j = i + step
                l1 = lists[i]
                if j < n2:

                    l2 = lists[j]
                    head = self.merge(l1, l2)
                else:
                    head = l1
                lists2.append(head)
                i += step * 2
            lists = lists2
            #step *= 2
            n2 = len(lists)
        return lists[0]

    def merge(self, l1, l2):
        node1 = l1
        node2 = l2
        dummy = ListNode(None)
        head = None
        while l1 and l2:
            if l1.val < l2.val:
                if head is None:
                    head = l1
                dummy.next = l1
                dummy = dummy.next
                l1 = l1.next
            else:
                if head is None:
                    head = l2
                dummy.next = l2
                dummy = dummy.next
                l2 = l2.next
        if l1:
            dummy.next = l1
        else:
            dummy.next = l2
        return head
