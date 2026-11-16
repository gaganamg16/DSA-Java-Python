class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x):
        self.stack1.append(x)

    def pop(self):
        self.peek()
        return self.stack2.pop()

    def peek(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        return self.stack2[-1]

    def empty(self):
        return not self.stack1 and not self.stack2


queue = MyQueue()

queue.push(10)
queue.push(20)
queue.push(30)

print("Front element:", queue.peek())
print("Removed element:", queue.pop())
print("Removed element:", queue.pop())
print("Is queue empty?", queue.empty())
