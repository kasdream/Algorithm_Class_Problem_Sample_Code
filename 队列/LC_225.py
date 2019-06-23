class MyStack(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        
        import Queue
        self.q1 = Queue.Queue()
        self.q2 = Queue.Queue()

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        self.q1.put(x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        self.top()
        res = self.q1.get()
        
        #交换q1和q2
        self.q1,self.q2 = self.q2,self.q1
        return res

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        #先把q1只保留一个元素
        while self.q1.qsize() > 1:
            self.q2.put(self.q1.get())
            
        #q1出队得到top
        res = self.q1.get()
        #然后再放回去
        self.q1.put(res)
        return res

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return self.q1.qsize() + self.q2.qsize() == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
