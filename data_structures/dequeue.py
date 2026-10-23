from .node import Node

class Dequeue:
    def __init__(self):
        self.front = None
        self.rear = None

    def insert_front(self, data):
        new_node = Node(data)

        if self.front is None:
            self.front = new_node
            self.rear = new_node
        else:
            self.front.next = new_node
            self.front = new_node

    def insert_rear(self, data):
        new_node = Node(data)

        if self.front is None:
            self.front = new_node
            self.rear = new_node

        else:
            new_node.next = self.rear
            self.rear = new_node

    def remove_rear(self):
        if self.rear is None:
            return None

        data = self.rear.data

        if self.front == self.rear:
            self.front = None
            self.rear = None
            return data

        old_rear = self.rear
        self.rear = self.rear.next
        old_rear.next = None

        return data


    def remove_front(self):
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

    def get_values(self):
        values = []
        current_node = self.rear

        while current_node:
            values.append(current_node.data)
            current_node = current_node.next

        return values
class Dequeue:
    def __init__(self):
        self.front = None
        self.rear = None

    def insert_front(self, data):
        new_node = Node(data)

        if self.front is None:
            self.front = new_node
            self.rear = new_node
        else:
            self.front.next = new_node
            self.front = new_node

    def insert_rear(self, data):
        new_node = Node(data)

        if self.front is None:
            self.front = new_node
            self.rear = new_node

        else:
            new_node.next = self.rear
            self.rear = new_node

    def remove_rear(self):
        if self.rear is None:
            return None

        data = self.rear.data

        if self.front == self.rear:
            self.front = None
            self.rear = None
            return data

        old_rear = self.rear
        self.rear = self.rear.next
        old_rear.next = None

        return data


    def remove_front(self):
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

    def get_values(self):
        values = []
        current_node = self.rear

        while current_node:
            values.append(current_node.data)
            current_node = current_node.next

        return values
