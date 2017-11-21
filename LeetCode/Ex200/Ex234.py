class Ex234(object):        
    def isPalindrome0(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        A = []
        head0 = head
        while head0 != None:
            A.append(head0)
            head0 = head0.next
        A.reverse()
        head0 = head
        i = 0
        while head0 != None:
            if head0.val != A[i].val:
                return False
            head0 = head0.next
            i += 1
        return True
    '''
    def isPalindrome(self, head):
        rev = None
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        if fast:
            slow = slow.next
        while rev and rev.val == slow.val:
            slow = slow.next
            rev = rev.next
        return not rev
    '''

