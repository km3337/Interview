# Min Max Stack
# push, pop, peek
# min, max, mean


class Stack:
    def __init__(self):
        # Constructs the Stack object:
        # vals: holds the current set of numbers on the stack
        # state: holds the current state of the vals. used to refer to previous versions of the stack
        # lastMin,lastMax: the last min and max numbers within the stack.
        self.vals = []
        self.state = dict()
        self.lastMin = float("inf")
        self.lastMax = float("inf") * -1

    def push(self, val):
        # adds a new a value into the stack object.
        # adds the new state into the state dictionary as tuple.
        # updates the lastMin and lastMax values
        self.vals.append(val)
        if val > self.lastMax:
            newMax = val
        else:
            newMax = self.lastMax
        if val < self.lastMin:
            newMin = val
        else:
            newMin = self.lastMin

        self.lastMin = newMin
        self.lastMax = newMax
        self.state[tuple(self.vals)] = (newMin, newMax)
        return 0

    def pop(self):
        # pops the stack, returning the last value on top.
        # updates the lastMin and last Max
        val = self.vals.pop()
        if tuple(self.vals) in self.state:
            self.lastMin, self.lastMax = self.state[tuple(self.vals)]
        return val

    def peek(self):
        # return the item on the stack, without removing it.
        return self.vals[-1:][0]

    def min(self):
        # returns the last min
        return self.lastMin

    def max(self):
        # returns the last max
        return self.lastMax

    def mean(self):
        # calculates the average number on the stack. returns calculation
        size = 0
        total = 0
        for val in self.vals:
            total += val
            size += 1
        return total/size


def main():
    newStack = Stack()
    newStack.push(3)
    newStack.push(2)
    newStack.push(1)
    print(newStack.min())
    print(newStack.max())
    print(newStack.mean())
    print(newStack.peek())
    print(newStack.pop())
    print(newStack.min())
    print(newStack.max())
    print(newStack.pop())
    print(newStack.pop())


if __name__ == "__main__":
    main()


