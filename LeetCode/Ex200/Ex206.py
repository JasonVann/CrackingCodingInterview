class Ex206(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return head
        (s, e) = self.helper(head)
        return s
        
    def helper(self, head):
        if head.next == None:
            return (head, head)
        (start, end) = self.helper(head.next)
        end.next = head
        head.next = None
        return (start, head)
    '''
    public ListNode reverseList(ListNode head) {
        /* iterative solution */
        ListNode newHead = null;
        while (head != null) {
            ListNode next = head.next;
            head.next = newHead;
            newHead = head;
            head = next;
        }
        return newHead;
    }
    '''
    '''
    class Solution {
    public:   
        ListNode* reverseList(ListNode* head) {
            if (!head || !(head -> next)) return head;
            ListNode* node = reverseList(head -> next);
            head -> next -> next = head;
            head -> next = NULL;
            return node; 
        }
    }; 
    '''

