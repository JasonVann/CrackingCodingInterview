class Ex142(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        i, j = head, head
        
        while True:
            if j == None or j.next == None:            
                return None
            i = i.next
            j = j.next.next
            if j == i:
                break          
            
        k = head
        while k != i:
            k = k.next
            i = i.next
        return k
