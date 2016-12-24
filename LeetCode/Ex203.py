class Ex203(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head == None:
            return head
        dummy = ListNode(0)
        dummy.next = head
        last = dummy
        while head != None:
            if head.val == val:
                last.next = head.next
            else:
                last = head
            head = head.next
        return dummy.next
    '''
    public ListNode removeElements(ListNode head, int val) {
        if (head == null) return null;
        head.next = removeElements(head.next, val);
        return head.val == val ? head.next : head;
    }
    '''

