class Ex150(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        if len(tokens) == 0:
            return 0
        stack_op = []
        stack_num = []
        ops = ['+', '-', '*', '/']
        for cur in tokens:
            if cur in ops:
                num2 = int(stack_num.pop())
                num1 = int(stack_num.pop())
                
                if cur == '+':
                    res = num1 + num2
                elif cur == '-':
                    res = num1 - num2
                elif cur == '*':
                    res = num1 * num2
                elif cur == '/':
                    if num1 * num2 < 0:
                        res = abs(num1)/abs(num2) * (-1)
                        #print 79, res
                    else:
                        res = num1 / num2
                else:
                    print 'Impossible!'
                stack_num.append(res)
            else:
                stack_num.append(int(cur))
        #print stack_num[0], stack_num
        return int(stack_num[0])
        
ex150 = Ex150()
tokens = ["2", "1", "+", "3", "*"]
tokens = ["4", "13", "5", "/", "+"]
tokens = []
tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]

print 150, ex150.evalRPN(tokens)

