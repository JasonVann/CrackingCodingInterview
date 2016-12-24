# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Ex19(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        head0 = head
        fast = head
        slow = head
        for i in range(n):
            fast = fast.next
        if fast == None:
            return slow.next
        while fast.next != None:
            fast = fast.next
            slow = slow.next
        
        slow.next = slow.next.next
        return head0
        
    def removeNthFromEnd0(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        head0 = head
        temp = []
        while head != None:
            temp.append(head)
            head = head.next
        
        if n >= len(temp):
            if len(temp) >= 2:
                return temp[1]
            return None
        m = len(temp)
        head1 = temp[m-n-1]
        temp.append(None)
        head1.next = temp[m-n+1]
        return head0
        
    def removeNthFromStart(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        head0 = head
        while n >= 1:
            head = head.next
            n -= 1
        if head != None:
            next = head.next.next
            head.next = next
        return head0
    '''
    public ListNode removeNthFromEnd(ListNode head, int n) {
        
        ListNode start = new ListNode(0);
        ListNode slow = start, fast = start;
        slow.next = head;
        
        //Move fast in front so that the gap between slow and fast becomes n
        for(int i=1; i<=n+1; i++)   {
            fast = fast.next;
        }
        //Move fast to the end, maintaining the gap
        while(fast != null) {
            slow = slow.next;
            fast = fast.next;
        }
        //Skip the desired node
        slow.next = slow.next.next;
        return start.next;
    }
    '''
    '''
    public class Solution {
        public ListNode removeNthFromEnd(ListNode head, int n) {
            return removeRec(null, head, n) == n ? head.next : head;
        }
        
        public int removeRec(ListNode prev, ListNode head, int n) {
            if(head == null)
            {
                return 0;
            }
            
            int depth = removeRec(head, head.next, n) + 1;
            
            if(n == depth && prev!= null)
            {
                prev.next = head.next;    
            }
            
            return depth;
        }
    }
    '''

