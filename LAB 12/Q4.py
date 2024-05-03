class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("ERROR: The queue is empty!")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("ERROR: The queue is empty!")
        return self.items[len(self.items)-1]

	
try:
    queue1 = Queue()
    queue1.enqueue('a')
    queue1.dequeue()
    queue1.enqueue('b')
    print(queue1.dequeue())
    print(queue1.dequeue())
except IndexError as err:
    print(err)