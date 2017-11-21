# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        head = None
        carry = 0
        prev = None
        while l1:
            if l2 == None:
                break
            v1 = l1.val
            v2 = l2.val
            cur = v1 + v2 + carry
            if cur >= 10:
                carry = 1
                cur = cur - 10
            else:
                carry = 0
            
            node = ListNode(cur)
            if prev != None:
                prev.next = node
            else:
                head = node
            prev = node
            l1 = l1.next
            l2 = l2.next
        if l1 == None and l2:
            l2, l1 = l1, l2
        if l2 == None and l1:
            while l1:
                cur = l1.val + carry
                if cur >= 10:
                    carry = 1
                    cur = cur - 10
                else:
                    carry = 0
                node = ListNode(cur)
                prev.next = node
                l1 = l1.next
                prev = node
        #return carry, prev
        if carry == 1:
            node = ListNode(carry)
            prev.next = node
        #return carry, prev
        return head
            
