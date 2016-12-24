class Ex82(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return head
        dummy = ListNode(0)
        dummy.next = head
        last = dummy
        while head != None and head.next != None:
            found = False
            cur = head
            while cur.next != None and cur.val == cur.next.val:
                cur = cur.next
                found = True
            if found:
                last.next = cur.next
            else:
                last = head
            head = cur.next            
                
        return dummy.next
    '''
    public ListNode deleteDuplicates(ListNode head) {
        if (head == null) return null;
        
        if (head.next != null && head.val == head.next.val) {
            while (head.next != null && head.val == head.next.val) {
                head = head.next;
            }
            return deleteDuplicates(head.next);
        } else {
            head.next = deleteDuplicates(head.next);
        }
        return head;
    }
    '''
    '''
    class Solution {
    public:
        ListNode *deleteDuplicates(ListNode *head) {
            ListNode **runner = &head;
            
            if(!head || !head->next)return head;
            
            while(*runner)
            {
                if((*runner)->next && (*runner)->next->val == (*runner)->val)
                {
                    ListNode *temp = *runner;
                    while(temp && (*runner)->val == temp->val)
                        temp = temp->next;
                    
                    *runner = temp;
                }
                else
                    runner = &((*runner)->next);
            }
            
            return head;
        }
    };
    '''

