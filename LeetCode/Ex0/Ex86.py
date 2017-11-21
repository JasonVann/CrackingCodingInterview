class Ex86(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        dummy = ListNode(0)
        dummy.next = head
        head2 = None
        end2 = None
        prev = dummy
        while head:
            if head.val < x:
                prev = head
                head = head.next
            #elif head.val == x:
                
            else:
                next = head.next
                if head2 == None:
                    head2 = head
                    #prev2 = head
                    end2 = head                    
                else:
                    end2.next = head
                    end2 = head
                
                prev.next = next
                head = next
                end2.next = None
        prev.next = head2
        return dummy.next
    '''
    ListNode *partition(ListNode *head, int x) {
        ListNode node1(0), node2(0);
        ListNode *p1 = &node1, *p2 = &node2;
        while (head) {
            if (head->val < x)
                p1 = p1->next = head;
            else
                p2 = p2->next = head;
            head = head->next;
        }
        p2->next = NULL;
        p1->next = node2.next;
        return node1.next;
    }
    '''

