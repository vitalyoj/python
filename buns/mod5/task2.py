class Node:
    """
    Вспомогательный класс для узлов списка
    """
    def __init__(self, data):
        self.data = data  # храним информацию
        self.nref = None  # ссылка на следующий узел
        self.pref = None  # Ссылка на предыдущий узел


class Queue:
    """
    Основной класс
    """

    def __init__(self):
        self.start = None  # ссылка на начало очереди
        self.end = None  # ссылка на конец очереди

    def pop(self):
        """
        возвращаем элемент val из начала списка с удалением из списка
        """
        if not self.start:
            print("Очередь пуста!")
            return None

        val = self.start.data
        self.start = self.start.nref

        if self.start:
            self.start.pref = None
        else:
            self.end = None

        return val

    def push(self, val):
        """
        добавление элемента val в конец списка
        """
        new_node = Node(val)
        if not self.end:
            self.start = self.end = new_node
        else:
            self.end.nref = new_node
            new_node.pref = self.end
            self.end = new_node

    def insert(self, n, val):
        """
        вставить элемент val между элементами с номерами n-1 и n
        """
        if n == 0:
            new_node = Node(val)
            new_node.nref = self.start
            self.start.pref = new_node
            self.start = new_node
            return
        
        current = self.start
        count = 0
        while current:
            if count == n - 1:
                new_node = Node(val)
                new_node.nref = current.nref
                new_node.pref = current
                if current.nref:
                    current.nref.pref = new_node
                else:
                    self.end = new_node
                current.nref = new_node
                return
            current = current.nref
            count += 1

        print("Индекс вне диапазона.")

    def print(self):
        """
        вывод на печать содержимого очереди
        """
        current = self.start
        while current:
            print(current.data, end=" <-> ")
            current = current.nref
        print("None")
q = Queue()
q.push(1)
q.push(2)
q.push(3)
q.print() 
