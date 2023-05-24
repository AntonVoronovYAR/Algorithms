from typing import List, Tuple

OPERATIONS: dict = {
    'pop_front': lambda: queue.pop_front(),
    'pop_back': lambda: queue.pop_back(),
    'push_front': lambda n: queue.push_front(n),
    'push_back': lambda n: queue.push_back(n),
}


class MyQueueSized:
    """Класс круговой очереди значений."""

    def __init__(self, max_size: int) -> None:
        """Инициализация класса, заполнение очереди значениями None."""
        self.__max_size = max_size
        self.__queue = [None] * max_size
        self.__head = 0
        self.__tail = 0
        self.__size = 0

    def is_empty(self) -> bool:
        """Проверка списка на наличие значений."""
        return self.__size == 0

    def add_in_empty(self, n: int) -> None:
        """Добавляем значение в пустую очередь."""
        self.__queue[self.__tail] = n
        self.__size += 1

    def set_index(self, item: int, operator: int) -> int:
        return (item + operator) % self.__max_size

    def push_front(self, n: int) -> None:
        """Добавляем значение в начало."""
        if self.__size == self.__max_size:
            print('error')
        elif self.__size == 0:
            self.add_in_empty(n)
        else:
            self.__head = self.set_index(self.__head, -1)
            self.__queue[self.__head] = n
            self.__size += 1

    def push_back(self, n: int) -> None:
        """Добавляем значение в конец."""
        if self.__size == self.__max_size:
            print('error')
        elif self.__size == 0:
            self.add_in_empty(n)
        else:
            self.__tail = self.set_index(self.__tail, 1)
            self.__queue[self.__tail] = n
            self.__size += 1

    def pop_front(self) -> None:
        """Убираем значение в начале."""
        if self.is_empty():
            print('error')
        else:
            z = self.__queue[self.__head]
            self.__queue[self.__head] = None
            self.__size -= 1
            if self.__size != 0:
                self.__head = self.set_index(self.__head, 1)
            print(z)

    def pop_back(self) -> None:
        """Убираем значение в конце."""
        if self.is_empty():
            print('error')
        else:
            z = self.__queue[self.__tail]
            self.__queue[self.__tail] = None
            self.__size -= 1
            if self.__size != 0:
                self.__tail = self.set_index(self.__tail, -1)
            print(z)


def read_input() -> Tuple[List, int]:
    """Считываем входные данные."""
    commands = []
    number_of_commands = int(input())
    max_deck_size = int(input())
    for _ in range(number_of_commands):
        commands.append(input())
    return commands, max_deck_size


def solution(commands: List) -> None:
    """Обработка команд."""
    for i in commands:
        command = i.split()[0]
        if len(i.split()) > 1:
            n = int(i.split()[1])
            OPERATIONS[command](n)
        else:
            OPERATIONS[command]()


if __name__ == "__main__":
    commands, max_size = read_input()
    queue = MyQueueSized(max_size)
    solution(commands)
