class Ex224(object):
    def calculate1(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 1:
            return int(s)
        stack_op = []
        stack_num = []
        ops = ['+', '-', '*', '/', '(', ')']
        need_num2 = False
        
        last_digit = None
        for cur in s:
            if cur == ' ' or cur in ops:
                if not need_num2:
                    if last_digit != None:
                        stack_num.append(int(last_digit))
                        last_digit = None
                else:
                    if last_digit != None:
                        num2 = int(last_digit)
                        last_digit = None
                    if cur == ' ':
                        continue
                    if cur != ')':
                        stack_op.append(cur)
                        if cur != '(':
                            need_num2 = True
                        else:
                            need_num2 = False
                        num2 = stack_num.pop()
                        num1 = stack_num.pop()
                        
                        if op == '+':
                            res = num1 + num2
                        elif op == '-':
                            res = num1 - num2
                        elif op == '*':
                            res = num1 * num2
                        elif op == '/':
                            res = num / num2
                        else:
                            print 'Impossible!', op, cur
                        stack_num.append(res) 
                        op = stack_op.pop()
                    else:
                        op = stack_op.pop()
                        while op != '(':
                            num2 = stack_num.pop()
                            num1 = stack_num.pop()
                            
                            if op == '+':
                                res = num1 + num2
                            elif op == '-':
                                res = num1 - num2
                            elif op == '*':
                                res = num1 * num2
                            elif op == '/':
                                res = num / num2
                            else:
                                print 'Impossible!', op, cur
                            stack_num.append(res) 
                            op = stack_op.pop()
                '''                        
                else:
                    op = stack_op.pop()
                '''
            else:      
                if last_digit != None:
                    last_digit = last_digit*10 + int(cur)
                else:
                    last_digit = int(cur)
                    
        if last_digit != None:
            stack_num.append(last_digit)
        if len(stack_op) > 0:
            op = stack_op.pop()
            num2 = stack_num.pop()
            num1 = stack_num.pop()
            if op == '+':
                res = num1 + num2
            elif op == '-':
                res = num1 - num2
            elif op == '*':
                res = num1 * num2
            elif op == '/':
                if num1 * num2 < 0:
                    res = abs(num1)/abs(num2) * (-1)
                    #print 79, res
                else:
                    res = num1 / num2
            else:
                print 'Impossible!'
            stack_num.append(res)
                    
        print stack_num[0], stack_num, stack_op
        return stack_num[0]
        
    def cal(self, num1, num2, op):
        if op == '+':
            res = num1 + num2
        elif op == '-':
            res = num1 - num2
        elif op == '*':
            res = num1 * num2
        elif op == '/':
            if num1 * num2 < 0:
                res = abs(num1) / abs(num2) * (-1)
                # print 79, res
            else:
                res = num1 / num2
        else:
            print 'Impossible!'
        return res
        
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 1:
            return int(s)
        stack_op = []
        stack_num = []
        ops = ['+', '-', '*', '/', '(', ')']
        need_num2 = False

        last_digit = None
        for cur in s:
            if cur == ' ':
                if not need_num2:
                    if last_digit != None:
                        stack_num.append(int(last_digit))
                        last_digit = None
                else:
                    if last_digit != None:
                        num2 = int(last_digit)
                        last_digit = None
                    else:
                        continue
                    num1 = stack_num.pop()
                    op = stack_op.pop()                    
                    res = self.cal(num1, num2, op)
                    stack_num.append(res)
                    need_num2 = False
                continue
            elif cur in ops:
                if last_digit != None:
                    stack_num.append(int(last_digit))
                    last_digit = None
                if cur != ')':
                    stack_op.append(cur)
                    if cur != '(':
                        need_num2 = True
                    else:
                        need_num2 = False
                else:
                    op = stack_op.pop()
                    while op != '(':
                        num2 = stack_num.pop()
                        num1 = stack_num.pop()
                        
                        res = self.cal(num1, num2, op)
                        stack_num.append(res)
                        op = stack_op.pop()
            else:
                if last_digit != None:
                    last_digit = last_digit * 10 + int(cur)
                else:
                    last_digit = int(cur)

        if last_digit != None:
            stack_num.append(last_digit)
        if len(stack_op) > 0:
            op = stack_op.pop()
            num2 = stack_num.pop()
            num1 = stack_num.pop()
            
            res = self.cal(num1, num2, op)
            stack_num.append(res)

        print stack_num[0], stack_num, stack_op
        return stack_num[0]
        
ex224 = Ex224()

#s = " 2-1 + 2 "
#s = "(1+(4+5+2)-3)+(6+8)"
s = "2147483647"
s = "1 + 1"
s = '01'
s = "0-2147483647"

s = "(11+(14+15+12)-3)+(16+8)"
s = "1 + 1"
s = "4-5+2"
#print 224, ex224.calculate(s)

