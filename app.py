from flask import Flask, render_template, request

from data_structures import Stack, Queue, Dequeue, LinkedList

import re

app = Flask(__name__)

linkedlist = LinkedList()
queue = Queue()
dequeue = Dequeue()

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


@app.route('/works/infix_to_postfix', methods=['GET', 'POST'])
def an_infix_to_postfix():
    result = None
    expression = ''
    error = None

    events = [

    ]

    PUSH = 'push'
    POP = 'pop'
    OUTPUT = 'output'
    OPERATORS = 'operators'

    def record_event(action, stack, value):
        events.append({
            'action': action,
            'stack': stack,
            'value': value
        })

    precedence = {
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2,
        '^': 3
    }

    if request.method == 'POST':
        expression = request.form.get('expression', '').strip()
        button_click = request.form.get('button-click', '')

        # Recognize operands, operators, and parentheses.
        tokens = re.findall(
            r'[A-Za-z]+|\d+(?:\.\d+)?|[()+\-*/^]',
            expression
        )

        # Reject characters that the tokenizer did not recognize.
        compact_expression = re.sub(r'\s+', '', expression)

        if not expression:
            error = 'Please enter an expression.'

        elif ''.join(tokens) != compact_expression:
            error = 'Expression contains unsupported characters.'

        else:
            # Create a fresh stack for this request.
            ops_stack = Stack()
            output = []

            for token in tokens:
                # 1. If token is an operand, send it to output.
                if re.fullmatch(r'[A-Za-z]+|\d+(?:\.\d+)?', token):
                    output.append(token)
                    record_event(PUSH, OUTPUT, token)

                # 2. If token is an opening parenthesis, push it.
                elif token == '(':
                    ops_stack.push(token)
                    record_event(PUSH, OPERATORS, token)

                # 3. If token is a closing parenthesis,
                # pop operators until the opening parenthesis.
                elif token == ')':
                    while (
                        ops_stack.peek() is not None
                        and ops_stack.peek() != '('
                    ):
                        top = ops_stack.pop()
                        
                        record_event(POP, OPERATORS, top)
                        
                        output.append(top)

                        record_event(PUSH, OUTPUT, top)

                    if ops_stack.peek() == '(':
                        top = ops_stack.pop()

                        record_event(POP, OPERATORS, top)
                    else:
                        error = 'Mismatched parentheses.'
                        break

                # 4. If token is an operator, handle precedence.
                elif token in precedence:
                    while (
                        ops_stack.peek() is not None
                        and ops_stack.peek() != '('
                        and (
                            precedence[ops_stack.peek()] > precedence[token]
                            or (
                                precedence[ops_stack.peek()] == precedence[token]
                                and token != '^'
                            )
                        )
                    ):
                        top = ops_stack.pop()

                        record_event(POP, OPERATORS, top)

                        output.append(top)

                        record_event(PUSH, OUTPUT, top)

                    ops_stack.push(token)

                    record_event(PUSH, OPERATORS, token)

                # Record the stack WITHOUT removing its nodes.
                operators = []
                current = ops_stack.top

                while current:
                    operators.append(current.data)
                    current = current.next

            # 5. Pop remaining operators.
            if error is None:
                while ops_stack.peek() is not None:
                    operator = ops_stack.pop()
                    record_event(POP, OPERATORS, operator)

                    if operator == '(':
                        error = 'Mismatched parentheses.'
                        break

                    output.append(operator)
                    record_event(PUSH, OUTPUT, operator)

            if error is None:
                result = ' '.join(output)

    return render_template(
        'infix_to_postfix.html',
        expression=expression,
        result=result,
        events=events,
        error=error
    )


@app.route('/works/queue', methods=['GET', 'POST'])
def aqueue():
    action = request.form.get('action', '')
    value = request.form.get('inputString', '')

    if action == 'Enqueue':
        queue.enqueue(value)
    elif action == 'Dequeue':
        queue.dequeue()

    result = queue.get_values()

    return render_template('queue.html', result=result)

@app.route('/works/dequeue', methods=['GET', 'POST'])
def adequeue():
    action = request.form.get('action', '')
    value = request.form.get('inputString', '')

    if action == 'Insert Front':
        dequeue.insert_front(value)
    elif action == 'Insert Rear':
        dequeue.insert_rear(value)
    elif action == 'Remove Front':
        dequeue.remove_front()
    elif action == 'Remove Rear':
        dequeue.remove_rear()
    
    result = dequeue.get_values()

    return render_template('dequeue.html', result=result)

@app.route('/contact')

def contact():
    return render_template('contact.html')

if __name__ == "__main__":
    app.run(debug=True)
