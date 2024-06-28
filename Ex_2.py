class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]

    def size(self):
        return len(self.items)

def is_balanced(expression):
    stack = Stack()
    opening_brackets = '([{'
    closing_brackets = ')]}'
    bracket_pairs = {')': '(', ']': '[', '}': '{'}

    for char in expression:
        if char in opening_brackets:
            stack.push(char)
        elif char in closing_brackets:
            if stack.is_empty():
                return False
            top = stack.pop()
            if top != bracket_pairs[char]:
                return False

    return stack.is_empty()

# Пример использования
print(is_balanced("(((([{}]))))"))  # True
print(is_balanced("[([])((([[[]]])))]{()}"))  # True
print(is_balanced("{{[()]}}"))  # True
print(is_balanced("}{}"))  # False
print(is_balanced("{{[(])]}}"))  # False
print(is_balanced("[[{())}]"))  # False