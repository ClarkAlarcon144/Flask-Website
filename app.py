from flask import Flask, render_template, request

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head:
            new_node.next = self.head
            self.head = new_node
        else:
            self.head = new_node
            self.tail = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.tail = new_node
            self.head = new_node

    def get_values(self):
        values = []

        current_node = self.head

        while current_node:
            values.append(current_node.data)
            current_node = current_node.next

        return values
    
    # TODO a: remove the FIRST node and return its data (not the Node).
    # If the list is empty, return None.
    def remove_beginning(self):
        if self.head:
            data = self.head.data
            self.head = self.head.next

            if self.head is None:
                self.tail = None

            return data
        else:
            return None

    # TODO b: remove the LAST node and return its data (not the Node).
    # If the list is empty, return None.
   
    def remove_at_end(self):
        if self.head:
            current_node = self.head

            if self.head == self.tail:
                data = self.tail.data
                self.head = None
                self.tail = None
                return data

            while current_node:
                if current_node.next == self.tail:   
                    data = self.tail.data
                    current_node.next = None
                    self.tail = current_node
                    return data

                else:
                    current_node = current_node.next

        else:
            return None


    # TODO c: remove the first node holding `data` and return its data.
    # If no node holds `data`, return None and leave the list unchanged.
    def remove_at(self, data):
        if self.head:
            current_node = self.head

            if current_node.data == data:
                return self.remove_beginning()

            while current_node.next:
                if current_node.next.data == data:  
                    data = current_node.next.data
                    current_node.next = current_node.next.next
                    
                    if current_node.next is None:
                        self.tail = current_node

                    return data

                else:
                    current_node = current_node.next

            return None
        
        else:
            return None

    # TODO d: insert a new node holding `data` right after the first node
    # holding `nodedata`.
    # If no node holds `nodedata`, return None and leave the list unchanged.
    def insert_after(self, nodedata, data):
        if self.head:
            current_node = self.head
            
            while current_node:
                if current_node.data == nodedata:   
                    new_node = Node(data)
                    new_node.next = current_node.next
                    current_node.next = new_node
                    
                    if new_node.next is None:
                        self.tail = new_node
                    
                    return

                else:
                    current_node = current_node.next

            return None
        else:
            return None
        
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/works')
def works():
    return render_template('works.html')

@app.route('/works/touppercase', methods=['GET', 'POST'])
def touppercase():
    result = None
    if request.method == 'POST':
        input_result = request.form.get('inputString', '')
        result = input_result.upper()
    return render_template('touppercase.html', result=result)

@app.route('/works/area/circle', methods=['GET', 'POST'])
def acircle():
    result = None
    if request.method == 'POST':
        radius = request.form.get('radius', '')

        try:
            radius = float(radius)

            if radius >= 0:
                result = radius*radius*3.14

        except ValueError:
            pass

    return render_template('circle.html', result=result)

@app.route('/works/area/triangle', methods=['GET', 'POST'])
def atriangle():
    result = None
    if request.method == 'POST':
        base = request.form.get('base', '')
        height = request.form.get('height', '')

        try:
            base = float(base)
            height = float(height)

            if base >= 0 and height >=0:
                result = base*height/2

        except ValueError:
            pass

    return render_template('triangle.html', result=result)


linkedlist = LinkedList()

@app.route('/works/linkedlist', methods=['GET', 'POST'])
def alinkedlist():

    result = linkedlist.get_values()

    if request.method == 'POST':

        action = request.form.get('action', '')
        value = request.form.get('inputString', '')
        position = request.form.get('position', '')

        if action == 'Insert Beginning':
            if value:
                linkedlist.insert_at_beginning(value)

        elif action == 'Insert End':
            if value:
                linkedlist.insert_at_end(value)

        elif action == 'Insert After':
            if value and position:
                linkedlist.insert_after(position, value)

        elif action == 'Remove Beginning':
            linkedlist.remove_beginning()

        elif action == 'Remove End':
            linkedlist.remove_at_end()

        elif action == 'Remove':
            linkedlist.remove_at(value)

        result = linkedlist.get_values()

    return render_template('linkedlist.html', result=result)

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == "__main__":
    app.run(debug=True)
