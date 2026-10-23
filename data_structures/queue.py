from .node import Node

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        new_node = Node(data)

        if self.front is None:
            self.front = new_node
            self.rear = new_node

        else:
            new_node.next = self.rear
            self.rear = new_node

    def dequeue(self):
        if self.front is None:
            return None

        data = self.front.data

        if self.front == self.rear:
            self.front = None
            self.rear = None
            return data

        current_node = self.rear

        while current_node.next != self.front:
            current_node = current_node.next 

        current_node.next = None
        self.front = current_node

        return data

    def peek(self):
        if self.front is None:
            return None
        return self.front.data

    def get_values(self):
        values = []
        current_node = self.rear

        while current_node:
            values.append(current_node.data)
            current_node = current_node.next

        return values