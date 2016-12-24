class Ex83(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        head0 = head
        prev = head
        head = head.next
        while head:
            next = head.next
            if prev.val == head.val:
                prev.next = next
            else:
                prev = head
            head = head.next
        return head0
    '''
    public ListNode deleteDuplicates(ListNode head) {
        if(head == null || head.next == null)return head;
        head.next = deleteDuplicates(head.next);
        return head.val == head.next.val ? head.next : head;
    }
    '''

