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

    def __init__(self) -> None:
        self.head: Node | None = None
        self.tail: Optional[Node] = None
        self.size = 0

    def __len__(self) -> int:
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
            nodeList: list[str] = []
            while current:
                nodeList.append(str(current.data))
                current = current.next
            return " -> ".join(nodeList)

    def addAtHead(self, value: Any) -> None:
        new_node = Node(value, self.head)
        if self.head is None:
            self.tail = new_node
        self.head = new_node
        self.size += 1

    def addAtTail(self, data: Any) -> None:
        '''Inserts the data at the end of the linked list
        :param data: element to be inserted at the end of the linked list
        :return: None'''
        newNode = Node(data, next=None)
        if self.isEmpty():
            self.head = newNode
        else:
            # Using tail to insert node at end of LinkedList in O(1) or constant time
            self.tail.next = newNode
        self.tail = newNode
        self.size += 1

    def addAtIndex(self, value: Any, index: int = 0) -> None:
        '''Adds data at the given index in the linked list.
         By default, adds data at the beginning of the linked list.
        :param value: element to be inserted at the given position of the linked list
        :param index: position of the element to be inserted in the linked list
        :return: None'''

        if index < 0:
            raise ValueError("Index must be Non-Negative")

        elif index > self.size:
            raise ValueError("Index={} exceeds linked list size={}".format(index, self.size))

        current = self.head

        # In empty list, insertion is possible only at index == 0.
        # If list is empty & index != 0 (say 3) then insertion should NOT be possible.
        if current is None and index == 0:
            self.addAtHead(value=value)

        # Adding Node at head, if list is not empty
        elif index == 0 and current is not None:
            self.addAtHead(value)

        elif index == self.size:
            self.addAtTail(value)

        # To add Node before index, traversing to index-1 position.
        else:
            for _ in range(index - 1):
                current = current.next
            new_node = Node(value, current.next)
            current.next = new_node
            self.size += 1

    def deleteAtTail(self) -> Any:
        '''Deletes the last node the linked list
        :return: deleted node of linked list'''
        if self.isEmpty():
            raise ValueError("The linked list is EMPTY")
        current = self.head
        for _ in range(self.size):
            if current.next.next is None:
                data = current.next.data
                # After deleting last Node, tail pointer is set to Null,
                # we need to set tail pointer to the updated last Node.
                self.tail = current
                current.next = None
                self.size -= 1
                return data
            current = current.next

    def deleteAtIndex(self, index: int = 0) -> Union[Node, Any]:
        '''Deletes node at the given index in the linked list.
        By default, node at the beginning (index=0) of the linked list will be deleted.
        :param index: Index of the element to be deleted from the linked list, index must be >= 0
        :return: deleted element at the given position from the linked list'''
        if index < 0:
            raise ValueError("Index must be Non-Negative")

        elif self.head is None:
            raise ValueError("The linked list is EMPTY")

        else:
            cur: Node = self.head
            prev: Node | None = None
            count: int = 0
            while cur.next is not None and count < index:
                prev = cur
                cur = cur.next
                count += 1
            if index == 0:
                self.head = cur.next
                val = cur.data
                self.size -= 1
                del cur
                return val

            elif count == index:
                val = cur.data
                prev.next = cur.next
                # cur.next is None implies we are at the Last Node.
                # If the last Node is deleted then tail will be set to None,
                # which will break adAtTail method. Therefore, setting last node as Tail
                if cur.next is None:
                    self.tail = prev
                self.size -= 1
                del cur
                return val

            elif cur.next is None:
                return None

    def get(self, index: int) -> int:
        '''
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :param index: Index of the element to be retrieved from the linked list.
        :return: value of the index-th node in the linked list
        '''
        if index < 0 or index >= self.size:
            return -1
        elif index == 0:
            return self.head.data
        elif index == self.size - 1:
            return self.tail.data
        else:
            current = self.head
            count = 0
            while current is not None and count < index:
                current = current.next
                count += 1
            return current.data
