class Ex160(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        # O(m)
        # ?? Memory Limit
        if headA == None or headB == None:
            return None
        p1 = headA
        p2 = headB
        if headA == headB:
            return headA
        l1 = 0
        l2 = 0
        while p1 != None:
            l1 += 1
            p1 = p1.next        
        while p2 != None:
            l2 += 1
            p2 = p2.next
        if p1 != p2:
            return None
        if l1 >= l2:
            p1, p2 = headA, headB
        else:
            p2, p1 = headA, headB
        # Insert nodes to l2
        i = abs(l1 - l2)
        while i > 0:
            p1 = p1.next
            i -= 1        
        while p1 != None:
            if p1 == p2:
                return p1
            p1 = p1.next
            p2 = p2.next
        return None
    '''
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        int lenA = length(headA), lenB = length(headB);
        // move headA and headB to the same start point
        while (lenA > lenB) {
            headA = headA.next;
            lenA--;
        }
        while (lenA < lenB) {
            headB = headB.next;
            lenB--;
        }
        // find the intersection until end
        while (headA != headB) {
            headA = headA.next;
            headB = headB.next;
        }
        return headA;
    }

    private int length(ListNode node) {
        int length = 0;
        while (node != null) {
            node = node.next;
            length++;
        }
        return length;
    }
    '''
    '''
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        //boundary check
        if(headA == null || headB == null) return null;
        
        ListNode a = headA;
        ListNode b = headB;
        
        //if a & b have different len, then we will stop the loop after second iteration
        while( a != b){
            //for the end of first iteration, we just reset the pointer to the head of another linkedlist
            a = a == null? headB : a.next;
            b = b == null? headA : b.next;    
        }
        
        return a;
    } 
    '''

