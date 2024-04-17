'''
Given a singly linked list, determine if it is a loop.
'''

from dataclasses import dataclass
from LinkedList import LinkedList
from typing import Any


@dataclass
class Node:
    data: Any
    next: Any = None
    flag: bool = False


class HasLoop(LinkedList):

    def detect_loop(self, head_node: Node) -> bool:
        '''
        Determine if a linked list has a loop.
        :param head_node: head node of a linked list.
        :return: bool, True if the linked list has a loop, False otherwise.
        '''
        while head_node:
            if head_node.flag:
                return True
            head_node.flag = True
            head_node = head_node.next
        return False

    def detect_loop_floyd(self, head: Node) -> bool:
        '''
        Determine if a linked list has a loop using floyd decomposition. Starts with a slow and a fast pointer,
        both pointing at head node, if there is a loop both pointers will meet at some point.
        :param head: head node of a linked list
        :return: bool, True if a loop is detected, False otherwise
        '''
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False


if __name__ == '__main__':
    obj = HasLoop()
    a = Node(1)
    b = Node(2)
    c = Node(3)
    d = Node(2)
    a.next = b
    b.next = c
    c.next = a
    print(obj.detect_loop(a))
    print(obj.detect_loop_floyd(a))
