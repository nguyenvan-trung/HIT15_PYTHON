class Strack:
    def initialization(self,capacity):
        self.strack = []
        self.maxn = capacity
    def isEmpty(self):
        return len(self.strack) == 0
    def isFull(self):
        return len(self.strack) == self.maxn
    def  pop(self):
        if self.strack.isEmpty():
            return " strack is empty "
        return self.strack.pop()
    def push(self, v):
        self.strack.append(v) 
    def top(self):
        if self.is_empty():
            return " strack is empty "
        return self.data[-1]
    
stack1 = Strack()
stack1.initialization(5)
stack1.push(1)
stack1.push(2)
print(stack1.isFull())