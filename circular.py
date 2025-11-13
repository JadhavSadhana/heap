class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1

    # Check if the queue is empty
    def is_empty(self):
        return self.front == -1

    # Check if the queue is full
    def is_full(self):
        return (self.rear + 1) % self.size == self.front

    # Add an element to the queue
    def enqueue(self, data):
        if self.is_full():
            print("Queue is full! Cannot enqueue", data)
            return
        if self.is_empty():
            self.front = 0
        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = data
        print(f"Enqueued: {data}")

    # Remove an element from the queue
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty! Cannot dequeue.")
            return None
        data = self.queue[self.front]
        if self.front == self.rear:  # Only one element
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        print(f"Dequeued: {data}")
        return data

    # Peek at the front element
    def peek(self):
        if self.is_empty():
            print("Queue is empty! Nothing to peek.")
            return None
        print(f"Front element: {self.queue[self.front]}")
        return self.queue[self.front]

    # Display the queue
    def display(self):
        if self.is_empty():
            print("Queue is empty!")
            return
        i = self.front
        elements = []
        while True:
            elements.append(self.queue[i])
            if i == self.rear:
                break
            i = (i + 1) % self.size
        print("Queue:", elements)


# Example usage
cq = CircularQueue(5)

cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
cq.display()
cq.peek()
cq.dequeue()
cq.display()
cq.enqueue(40)
cq.enqueue(50)
cq.enqueue(60)  # Should show full
cq.display()
