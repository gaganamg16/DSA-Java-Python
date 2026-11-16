class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        self.stack.append(val)

        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self):
        if self.stack:
            removed = self.stack.pop()

            if removed == self.min_stack[-1]:
                self.min_stack.pop()

    def top(self):
        return self.stack[-1]

    def get_min(self):
        return self.min_stack[-1]


# Testing the MinStack
min_stack = MinStack()

min_stack.push(-2)
min_stack.push(0)
min_stack.push(-3)

print("Minimum element:", min_stack.get_min())

min_stack.pop()

print("Top element:", min_stack.top())
print("Minimum element:", min_stack.get_min())
