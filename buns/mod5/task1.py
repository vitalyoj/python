class Node:
    """
    Вспомогательный класс для узлов списка
    """
    def __init__(self, data):
        self.data = data  # храним информацию
        self.pref = None  # ссылка на предыдущий узел

class Stack:
    """
    Основной класс для стека
    """
    def __init__(self):
        self.end = None  # ссылка на конец стека

    def pop(self):
        """
        возвращение последнего элемента из списка с удалением его из списка
        """
        if self.end is None:
            print("Стек пуст!")
            return None
        else:
            val = self.end.data
            self.end = self.end.pref
            return val

    def push(self, val):
        """
        добавление элемента val в конец списка
        """
        new_node = Node(val)
        if self.end is None:
            self.end = new_node
        else:
            new_node.pref = self.end
            self.end = new_node

    def print(self):
        """
        вывод на печать содержимого стека
        """
        temp = self.end
        while temp:
            print(temp.data)
            temp = temp.pref

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

stack.print()  
