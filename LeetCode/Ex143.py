# Split, reverse, merge
class Ex143(object):
    def reverse(self, head):
        newHead = None;
        while (head != None):
            next = head.next
            head.next = newHead
            newHead = head
            head = next
        
        return newHead
        
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if head == None:
            return
        h0 = head
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        if fast:
            slow = slow.next
            
        (s, e) = self.reverse(slow)
        # Then merge head & s
        l1 = h0
        l2 = s
        self.merge(l1, l2)
        return 
        
    def merge(self, l1, l2):
        while True:    
            if l1 == None:
                return
            if l2 == None:
                l1.next = l2
                return
            next = l1.next
            l1.next = l2
            t = l2.next
            l2.next = next
            l1, l2 = next, t
        
    def merge0(self, l1, l2):
        if l1 == None:
            return
        if l2 == None:
            l1.next = l2
            return
        next = l1.next
        l1.next = l2
        t = l2.next
        l2.next = next
        self.merge(next, t)

