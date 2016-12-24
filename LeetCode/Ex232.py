class Ex232(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        from collections import deque
        self.stack = deque()

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.stack.append(x)

    def pop(self):
        """
        :rtype: nothing
        """
        self.stack.popleft(0)

    def peek(self):
        """
        :rtype: int
        """
        return self.stack[0]

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.stack) == 0

class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.stack.append(x)

    def pop(self):
        """
        :rtype: nothing
        """
        self.stack.pop(0)

    def peek(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.stack) == 0
    '''
    # Two stacks
    class MyQueue {
        Stack<Integer> input = new Stack();
        Stack<Integer> output = new Stack();
        
        public void push(int x) {
            input.push(x);
        }

        public void pop() {
            peek();
            output.pop();
        }

        public int peek() {
            if (output.empty())
                while (!input.empty())
                    output.push(input.pop());
            return output.peek();
        }

        public boolean empty() {
            return input.empty() && output.empty();
        }
    }
    '''

