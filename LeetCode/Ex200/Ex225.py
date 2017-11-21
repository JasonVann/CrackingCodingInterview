#Ex225
class Stack(object):
    from collections import deque
    def __init__(self):
        """
        initialize your data structure here.
        """
        
        self.input = self.deque()
        self.output = self.deque()

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.input.append(x)        

    def pop(self):
        """
        :rtype: nothing
        """
        print 77,  self.input, self.output
        while len(self.input) != 0:            
            a = self.input.popleft()  
            if len(self.input) != 0:              
                self.output.append(a)
        self.input = self.output
        self.output = self.deque()
        print 83,  self.input, self.output
        return a
            
    def top(self):
        """
        :rtype: int
        """
        #print 87, self.input, self.output
        while len(self.input) != 0:            
            a = self.input.popleft()             
            self.output.append(a)
        self.input = self.output
        self.output = self.deque()
        return a

    def empty(self):
        """
        :rtype: bool
        """
        print 102, self.input, self.output
        return len(self.input) == 0 and len(self.output) == 0
    '''
    class Stack {
    public:
        queue<int> que;
        // Push element x onto stack.
        void push(int x) {
            que.push(x);
            for(int i=0;i<que.size()-1;++i){
                que.push(que.front());
                que.pop();
            }
        }

        // Removes the element on top of the stack.
        void pop() {
            que.pop();
        }

        // Get the top element.
        int top() {
            return que.front();
        }

        // Return whether the stack is empty.
        bool empty() {
            return que.empty();
        }
    };
    '''
    '''
    class MyStack 
    {
        Queue<Integer> queue;
        
        public MyStack()
        {
            this.queue=new LinkedList<Integer>();
        }
        
        // Push element x onto stack.
        public void push(int x) 
        {
           queue.add(x);
           for(int i=0;i<queue.size()-1;i++)
           {
               queue.add(queue.poll());
           }
        }

        // Removes the element on top of the stack.
        public void pop() 
        {
            queue.poll();
        }

        // Get the top element.
        public int top() 
        {
            return queue.peek();
        }

        // Return whether the stack is empty.
        public boolean empty() 
        {
            return queue.isEmpty();
        }
    }
    '''
    '''
    class MyStack {
        //using two queue. The push is inefficient.
        private Queue<Integer> q1 = new LinkedList<Integer>();
        private Queue<Integer> q2 = new LinkedList<Integer>();
        public void push(int x) {
            if(q1.isEmpty()) {
                q1.add(x);
                for(int i = 0; i < q2.size(); i ++)
                    q1.add(q2.poll());
            }else {
                q2.add(x);
                for(int i = 0; i < q1.size(); i++)
                    q2.add(q1.poll());
            }
        }

        public void pop() {
            if(!q1.isEmpty()) 
                q1.poll();
            else
                q2.poll();
        }
        public int top() {
            return q1.isEmpty() ? q2.peek() : q1.peek();
        }
        public boolean empty() {
            return q1.isEmpty() && q2.isEmpty();
        }
        }
    '''
    
print 225
st = Stack()
st.push(1)
st.pop()
st.empty()
print 57, st.input, st.output

