class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# https://leetcode.com/problems/sort-list/discuss/46712/
# https://leetcode.com/problems/sort-list/discuss/46710/

head = ListNode(-3)
head.next = ListNode(4)
head.next.next = head

class Ex148(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        n = 0
        cur = head
        while cur:
            cur = cur.next
            n += 1
        step = 1
        dummy = ListNode(None)
        dummy.next = head
        while step < n:
            cur = dummy.next
            tail = dummy
            while(cur):
                first = cur
                second = self.split(first, step)
                cur = self.split(second, step)
                tail = self.merge(first, second, tail)
            step *= 2
        return dummy.next

    def split(self, head, n):
        # Split ll after n nodes
        # Return the head of the remaining ll
        i = 1
        while i < n and head:
            head = head.next
            i += 1
        if head is None:
            return None
        second = head.next
        head.next = None
        return second

    def merge(self, first, second, head):
        # Merge first and second to head
        # Return the tail
        cur = head
        while first and second:
            if first.val < second.val:
                cur.next = first
                first = first.next
            else:
                cur.next = second
                second = second.next
            cur = cur.next
        if first:
            cur.next = first
        else:
            cur.next = second
        while cur.next:
            cur = cur.next
        return cur

    def sort00(self, prev, head, end):
        # end: next_head
        #return 20, head, end
        if head == end or head.next == end:
            return (head, head)
        if head.next.next == end:
            new_head = head
            if head.val > head.next.val:
                new_head = head.next
                temp = new_head.next
                new_head.next = head
                head.next = temp
                prev.next = new_head
            return (new_head, new_head.next)
        head0 = head
        fast = head
        slow = head
        while fast != end and fast.next != end:
            fast = fast.next.next
            slow = slow.next
        if fast != end:
            slow = slow.next
        #return 74, prev, head, slow
        (h1, end1) = self.sort00(prev, head, slow)
        #return 76, prev, h1, end1, end1.next, head, slow, end
        '''
        head = h1
        fast = head
        slow = head
        while fast != end and fast.next != end:
            fast = fast.next.next
            slow = slow.next
        if fast != end:
            slow = slow.next
        '''
        (h2, end2) = self.sort00(end1, end1.next, end)
        #return 85, h1, h2, head, slow, end, end1, end2
        h = self.merge0(prev, h1, h2, end)
        h0 = h
        while h0 and h0.next and h0.next != end:
            h0 = h0.next

        return (h, h0)

    def merge0(self, prev, h1, h2, end):
        if not h1:
            return h2
        if h2 == end:
            return h1
        h1_end = h2
        dummy = prev
        #return 99, prev, h1, h2, end
        while h1 and h2 and h1 != h1_end and h2 != end:
            #return 101, dummy, prev, h1, h2, end
            if h1.val <= h2.val:
                prev.next = h1
                h1 = h1.next
            else:
                prev.next = h2
                h2 = h2.next
            prev = prev.next
        #return 107, dummy, prev, h1, h2, end
        if h1 and h1 != h1_end:
            prev.next = h1
            last = h1
            while h1 and h1 != h1_end:
                last = h1
                h1 = h1.next
            #if last != None:
            last.next = None
        if h2 and h2 != end:
            prev.next = h2
        return dummy.next

    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        '''
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        if fast:
            slow = slow.next
        h1 = self.sort(head, slow)
        '''
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        (h, end) = self.sort00(prev, head, None)

        return h

    def sortList0(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # ?? bottom-up
        if head == None or head.next == None:
            return head
        i = 0
        fast = head
        slow = head
        while fast:
            for j in range(2**i):
                fast = fast.next
            self.merge(slow, fast)
            i += 1
            #fast = end.next
            fast = head
            slow = head
        return head




ex148 = Ex148()
head = ListNode(-3)
head.next = ListNode(4)
head.next.next = ListNode(1)
head.next.next.next = ListNode(5)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(6)
print(148, ex148.sortList(head))
