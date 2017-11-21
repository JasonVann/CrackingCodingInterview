class Ex61(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # k from tail
        if head == None:
            return head
        if k == 0:
            return head
        p2 = head
        p1 = head
        
        i = 0
        head0 = head
        while i < k:
            p2 = p2.next
            i += 1
            if p2 == None:
                p2 = head0
                break
        if i < k:
            k = k % i
            
            i = 0
            while i < k:
                p2 = p2.next
                i += 1
                if p2 == None:
                    break
            
        head1 = p2
        while p2.next != None:
            p2 = p2.next
            last = p1
            p1 = p1.next
            
        p2.next = head0
        p = p1.next
        p1.next = None
        
        return p
        
    def rotateRight1(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # k from tail
        # Slow is k large
        if head == None:
            return head
        if k == 0:
            return head
        p2 = head
        p1 = head
        
        i = 0
        head0 = head
        while i < k:
            p2 = p2.next
            if p2 == None:
                p2 = head0
            i += 1
        head1 = p2
        while p2.next != None:
            p2 = p2.next
            last = p1
            p1 = p1.next
        p2.next = head0
        
        p = p1.next
        p1.next = None
        
        return p
        
    def rotateRight0(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # k from head
        if head == None:
            return head
        if k == 0:
            return head
        
        i = 0
        head0 = head
        while i < k - 1:
            head = head.next
            i += 1
        temp = head
        head = head.next
        head1 = head
        temp.next = None
        while head.next != None:
            head = head.next
        head.next = head0
        return head1
    '''
    public ListNode rotateRight(ListNode head, int n) {
        if (head==null||head.next==null) return head;
        ListNode dummy=new ListNode(0);
        dummy.next=head;
        ListNode fast=dummy,slow=dummy;

        int i;
        for (i=0;fast.next!=null;i++)//Get the total length 
            fast=fast.next;
        
        for (int j=i-n%i;j>0;j--) //Get the i-n%i th node
            slow=slow.next;
        
        fast.next=dummy.next; //Do the rotation
        dummy.next=slow.next;
        slow.next=null;
        
        return dummy.next;
    }
    '''

