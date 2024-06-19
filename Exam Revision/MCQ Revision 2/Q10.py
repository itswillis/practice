class Queue:

    def __init__(self):
        self.items = []
        self.count = 0
    def size(self):
        return self.count
    def is_empty(self):
        return self.count == 0
    def enqueue(self, item):
        self.items.insert(0,item)
        self.count += 1
    def dequeue(self):
        if not self.is_empty():
            self.count -= 1
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            value = self.items[-1]
            return value
    def __str__(self):
        content_str = ""
        for i in range(self.count - 1,-1,-1):
            content_str += str(self.items[i]) + ", "
        return "[" + content_str[:-2] + "]"
    

queue = Queue()
queue.enqueue(5)
queue.enqueue("A")
queue.enqueue("B")
print(queue.peek(), end=" ")
queue.enqueue(9)
print(queue.dequeue(), end=" ")
print(queue)