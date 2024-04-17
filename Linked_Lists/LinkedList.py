'''
This is Singly Linked List Data Structure which consists of Nodes:
Nodes contain data and link to next node:
    - Head Node: First node, the address of the head node gives us access of the complete list.
    - Tail Node: Last Node, faster insertion at end of linked list, points to Null.
Note: All nodes in the linked list are 0-indexed.
'''

from typing import Any, Optional, Union


class Node:
    '''Node class, creates a Node with data and link to the next node.
    :param data: contains data of a node
    :param next: contains address of  next node'''

    __slots__ = "data", "next"

    def __init__(self, data: Any, next=None):
        self.data = data
        self.next = next


class LinkedList:
    '''This is singly linked list, where each node is linked to the next node.
    :param head: contains of head node of the linked list
    :param tail: contains tail node of the linked list
    :param size: size of the linked list'''

    def __init__(self):
        self.head: Node | None = None
        self.tail: Optional[Node] = None
        self.size = 0

    def __len__(self):
        ''':return: returns the size of the linked list'''
        return self.size

    def isEmpty(self) -> None:
        '''Checks if the linked list is empty
        :return: bool'''
        return self.head is None

    def __str__(self) -> str:
        '''Overriding __str__ method so that it prints the linked list with default print() method
        in the format 1 -> 2 -> 3'''
        if self.isEmpty():
            return ""
        else:
            current = self.head
            node_str = ""
            nodeList: list[str] = []
            while current:
                nodeList.append(str(current.data))
                current = current.next
            node_str = " -> ".join(nodeList)

            return node_str

    def insert_at_end(self, data):
        '''Inserts the data at the end of the linked list
        :param data: element to be inserted at the end of the linked list
        :return: None'''
        newNode = Node(data, next=None)
        if self.isEmpty():
            self.head = newNode
        else:
            self.tail.next = newNode
        self.tail = newNode
        self.size += 1

    def insert(self, data: Any, index: int = 0) -> None:
        '''Inserts the data at the given position of the linked list, by default at the beginning of the linked list
        :param data: element to be inserted at the given position of the linked list
        :param index: position of the element to be inserted in the linked list
        :return: None'''

        if index < 0:
            raise ValueError("Index must be Non-Negative")

        elif index > self.size:
            raise ValueError("Index={} exceeds linked list size={}".format(index, self.size))

        current = self.head

        if current is None and index == 0:
            new_node = Node(data, self.head)
            self.head = new_node
            self.tail = new_node

        elif index == 0 and current is not None:
            new_node = Node(data, self.head)
            self.head = new_node

        # Using tail to insert node at end of LinkedList in O(1) or constant time
        elif index == self.size:
            new_node = Node(data, None)
            self.tail.next = new_node
            self.tail = new_node

        # Traversing to (position-1)th node
        else:
            for _ in range(index - 1):
                current = current.next

            # Create a node with given data & current._next connects this node to the next node in LinkedList.
            new_node = Node(data, current.next)

            # Connect the current node to the node we created
            current.next = new_node
        self.size += 1


    def delete_last_node(self) -> Any:
        '''Deletes the last node the linked list
        :return: deleted node of linked list'''
        if self.isEmpty():
            raise ValueError("The linked list is EMPTY")

        current = self.head
        for _ in range(self.size):
            if current.next.next is None:
                data = current.next.data
                current.next = None
                self.size -= 1
                return data
            current = current.next

    def delete(self, index: int = 0) -> Union[Node, Any]:
        '''Deletes the element at the given position from the linked list.
        By default, node at the beginning of the linked list is deleted.
        :param index: Index of the element to be deleted from the linked list, index must be >= 0
        :return: deleted element at the given position from the linked list'''
        if index < 0:
            raise ValueError("Index must be Non-Negative")

        # For a linkedlist of size = n, Maximum possible index = n-1
        elif index >= self.size:
            raise ValueError('''Index Out of Bound.
            Max allowed Index={}, Index given={}'''.format(self.size-1, index))

        current = self.head

        if self.head is None:
            raise ValueError("The linked list is EMPTY")

        elif index == 0:
            self.head = current.next
            del current
            self.size -= 1
            return

        else:
            for idx in range(index - 1):
                if current is None or current.next is None:
                    return
                current = current.next
            next_node = current.next.next
            del current.next
            current.next = next_node
            self.size -= 1


    def search_index(self, element) -> int:
        '''Checks if element is present in the linked list
        :param element: element to be searched
        :return: index of the element present in the linked list'''
        current = self.head
        for idx in range(self.size):
            if element == current.data:
                return idx
            current = current.next
        return -1