class Ex328(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        odd = head
        even = head.next
        even0 = even
        while odd.next != None:
            odd.next = even.next    
            if odd.next:
                odd = odd.next
                even.next = odd.next
                even = even.next
            else:
                break
        odd.next = even0
        return head
    '''
    public ListNode oddEvenList(ListNode head) {
        if(head==null||head.next==null) return head;
        ListNode odd=head,ehead=head.next,even=ehead;
        while(even!=null&&even.next!=null){
            odd.next=even.next;
            odd=odd.next;
            even.next=odd.next;
            even=even.next;
        }
        odd.next=ehead;
        return head;
    }
    '''

