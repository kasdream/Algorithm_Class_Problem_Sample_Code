class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        #定义具体操作
        def calculate(op,a,b):
            if op == '+':
                return b+a
            if op == '-':
                return b-a
        #定义二元运算符的出栈操作
        def op_stack_pop(op_stack,num_stack):
            op = op_stack[-1]; op_stack.pop()
            num_a = num_stack[-1]; num_stack.pop()
            num_b = num_stack[-1]; num_stack.pop()
            res = calculate(op,num_a,num_b)
            num_stack.append(res)
        
        #符号优先级
        rk = {'+':1,'-':1,'(':100,')':-100}
        num_stack = []
        op_stack = []
        for i,c in enumerate(s):
            if c == ' ': continue
            if c >= '0' and c <= '9':
                #处理数字
                if i != 0 and s[i-1] >= '0' and s[i-1] <= '9': 
                    num_stack[-1] = num_stack[-1] * 10 + ord(c) - ord('0')
                else:
                    num_stack.append(int(c))
            elif c == '+' or c == '-':
                #处理运算符号
                while (len(op_stack) != 0 and rk[c] >= rk[op_stack[-1]] ):
                    op_stack_pop(op_stack,num_stack)
                op_stack.append(c)
            elif c == '(':
                #括号单独处理
                op_stack.append(c)
            elif c == ')':
                #括号单独处理
                while (op_stack[-1] != '('):
                    op_stack_pop(op_stack,num_stack)
                op_stack.pop()
        while len(op_stack) != 0:
            op_stack_pop(op_stack,num_stack)
        return num_stack[0]
            
                
