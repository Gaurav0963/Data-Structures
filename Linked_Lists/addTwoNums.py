from LinkedList import LinkedList, Node
from typing import Optional


class AddLinkedList:
    def add_two_lists(self, l1: Node, l2: Node) -> Node:
        '''You are given two non-empty linked lists representing two non-negative integers.
        The digits are stored in reverse order, and each of their nodes contains a single digit.
        Add the two numbers and return the sum as a linked list.
        You may assume the two numbers do not contain any leading zero, except the number 0 itself.
        :param l1: First linked list.
        :param l2: Second linked list.
        :return: head Node of added linked list.'''

        dummyHead = Node(0)
        ptr = dummyHead
        carry = 0

        while l1 or l2 or carry!=0:
            digit1 = l1.data if l1 else 0
            digit2 = l2.data if l2 else 0

            sum = digit1 + digit2 + carry
            digit = sum % 10
            carry = sum // 10

            # Create a Node containing the digit
            newNode = Node(digit)
            ptr.next = newNode
            ptr = ptr.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        result = dummyHead.next
        dummyHead.next = None
        return result


    def print_linked_list(self, head: Optional[Node]) -> None:
        '''prints linked list
        :param head: head node of linked list
        :return: None'''
        while head:
            print(head.data, end=" -> ")
            head = head.next
        print("None")



if __name__ == '__main__':
    obj = AddLinkedList()

    l1 = LinkedList()
    l1.insert(9)

    l2 = LinkedList()
    l2.insert(9)

    obj.print_linked_list(l1.head)
    obj.print_linked_list(l2.head)

    res = obj.add_two_lists(l1.head, l2.head)
    obj.print_linked_list(res)