class Ex24(object):
    def recur(self, head):
        if head.next == None or head.next.next == None:
            return 
        temp = head.next.next.next
        head1 = head.next
        head.next.next.next = head.next
        head.next = head.next.next
        head1.next = temp
        self.recur(head.next.next)
        
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return head
            
        new_head = ListNode(0)
        new_head.next = head
        self.recur(new_head)
        
        return new_head.next
    '''
    public class Solution {
      public ListNode swapPairs(ListNode head) {
        if(head==null || head.next==null) return head;
        ListNode newHead = head.next, a=head,b=a.next,pre = null;
        while(a!=null && b!=null){
          a.next = b.next;
          b.next = a;
          if(pre!=null) pre.next = b;
          if(a.next==null) break;
          b = a.next.next;
          pre = a;
          a = a.next;
        }
        return newHead;
      }
    }
    '''
    '''
    def swapPairs(self, head):
        pre, pre.next = self, head
        while pre.next and pre.next.next:
            a = pre.next
            b = a.next
            pre.next, b.next, a.next = b, a, b.next
            pre = a
        return self.next
    '''
    '''
        ListNode* swapPairs(ListNode* head) {
        ListNode **pp = &head, *a, *b;
        while ((a = *pp) && (b = a->next)) {
            a->next = b->next;
            b->next = a;
            *pp = b;
            pp = &(a->next);
        }
        return head;
    }
    '''

