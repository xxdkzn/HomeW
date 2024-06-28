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
        

# Пример использования

# Создаем экземпляр класса Stack
stack = Stack()

# Проверяем, пуст ли стек
print(stack.is_empty())  # True

# Добавляем элементы в стек
stack.push(1)
stack.push(2)
stack.push(3)

# Проверяем размер стека
print(stack.size())  # 3

# Получаем верхний элемент стека без удаления
print(stack.peek())  # 3

# Удаляем верхний элемент стека
print(stack.pop())  # 3

# Проверяем размер стека после удаления
print(stack.size())  # 2