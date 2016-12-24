class Ex147(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        i = 1
        dummy = ListNode(0)
        dummy.next = head
        target = head.next
        end = head
        last_end = dummy
        while True:               
            #target = target.next  
            t_next = target.next
            
            #self.insert(dummy, target, i)
            found = False
            prev = dummy
            cur = dummy.next
            
            next = end.next
            for j in range(i):            
                if cur.val > target.val:
                    #t_next = target.next
                    #next0 = prev.next
                    prev.next = target
                    target.next = cur
                    found = True
                    break
                prev = cur
                cur = cur.next
                
            if found:
                end.next = t_next            
            else:
                # target is the largest
                last_end = end
                end = next
                
            if t_next == None:
                break
            i += 1
            target = t_next
            
        return dummy.next
    '''
    public ListNode insertionSortList(ListNode head) {
        if( head == null ){
            return head;
        }
        
        ListNode helper = new ListNode(0); //new starter of the sorted list
        ListNode cur = head; //the node will be inserted
        ListNode pre = helper; //insert node between pre and pre.next
        ListNode next = null; //the next node will be inserted
        //not the end of input list
        while( cur != null ){
            next = cur.next;
            //find the right place to insert
            while( pre.next != null && pre.next.val < cur.val ){
                pre = pre.next;
            }
            //insert between pre and pre.next
            cur.next = pre.next;
            pre.next = cur;
            pre = helper;
            cur = next;
        }
        
        return helper.next;
    }
    '''
    '''
    class Solution { 
    public:
        ListNode* insertionSortList(ListNode* head) {
            ListNode* new_head = new ListNode(0);
            new_head -> next = head;
            ListNode* pre = new_head;
            ListNode* cur = head;
            while (cur) {
                if (cur -> next && cur -> next -> val < cur -> val) {
                    while (pre -> next && pre -> next -> val < cur -> next -> val)
                        pre = pre -> next;
                    /* Insert cur -> next after pre.*/
                    ListNode* temp = pre -> next;
                    pre -> next = cur -> next;
                    cur -> next = cur -> next -> next;
                    pre -> next -> next = temp;
                    /* Move pre back to new_head. */
                    pre = new_head;
                }
                else cur = cur -> next;
            }
            ListNode* res = new_head -> next;
            delete new_head;
            return res;
        }
    };
    '''
        
   
ex147 = Ex147()
head = ListNode(3)
head.next = ListNode(1)
head.next.next = ListNode(2)
print 147, ex147.insertionSortList(head)

