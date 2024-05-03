class CircularQueue: 
    def __init__(self, capacity = 8):
        self.items = [None] * capacity
        self.max_queue = capacity
        self.front = 0 
        self.back = self.max_queue - 1
        self.count = 0 
    
    def is_empty(self):
        return self.count == 0 
    
    def show_contents(self):
        return (f"{self.items}, front:{self.front}, back:{self.back}, count:{self.count}")
    


queue1 = CircularQueue(5)
print(queue1.show_contents())