'''
Stack implementation using linked list.
Last element is pushed onto top of the stack and popped off the top of the stack.
'''
from dataclasses import dataclass
from typing import Any

@dataclass
class Node:
    data: Any
    next: Any = None


class Stack():
    def __init__(self):
        self.head: Node|None = None
        self.size: int = 0

    def __len__(self):
        return self.size

    def isEmpty(self):
        return self.head is None

    def __str__(self):
        current = self.head
        node_list: list[str] = list()
        while current:
            node_list.append(str(current.data))
            current = current.next
        return ' -> '.join(node_list)

    def push(self, data: Any) -> None:
        new_node = Node(data, self.head)
        self.head = new_node
        self.size += 1

    def pop(self) -> Any:
        if self.head is None:
            raise Exception('Stack is Empty')
        current = self.head
        element = self.head.data
        current = current.next
        self.size -= 1
        self.head = current
        return element

    def peek(self) -> Any:
        if self.head is None:
            return None
        return self.head.data


if __name__ == '__main__':
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack)
    print(len(stack))