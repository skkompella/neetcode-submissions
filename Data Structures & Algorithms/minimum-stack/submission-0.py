class MinStack:

    def __init__(self):
        self.jiggesh = []

    def push(self, val: int) -> None:
        self.jiggesh.append(val)

    def pop(self) -> None:
        self.jiggesh.pop()

    def top(self) -> int:
        return self.jiggesh[-1]

    def getMin(self) -> int:
        return min(self.jiggesh)
