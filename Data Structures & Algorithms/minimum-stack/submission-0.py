class MinStack:

    def __init__(self):
        self.stk = []
        self.minStk = []

    def push(self, val: int) -> None:
        self.stk.append(val)
        
        if not self.minStk:
            self.minStk.append(val)

        elif self.minStk[-1] < val:
            self.minStk.append(self.minStk[-1])
        else:
            self.minStk.append(val)


    def pop(self) -> None:
        
        del self.stk[-1]
        del self.minStk[-1]
    def top(self) -> int:
        
        return self.stk[-1]

    def getMin(self) -> int:
        
        return self.minStk[-1]