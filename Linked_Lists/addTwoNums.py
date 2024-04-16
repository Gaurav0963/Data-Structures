from LinkedList import LinkedList, Node


class AddLinkedList(LinkedList):
    def add_two_lists(self, head1: Node, head2: Node) -> None:
        '''You are given two non-empty linked lists representing two non-negative integers.
        The digits are stored in reverse order, and each of their nodes contains a single digit.
        Add the two numbers and return the sum as a linked list.
        You may assume the two numbers do not contain any leading zero, except the number 0 itself.
        :param head1: head node of first linked list.
        :param head2: head node of second linked list.
        :return: head Node of added linked list.'''

        dummyHead = Node(0)
        ptr = dummyHead
        carry = 0

        while head1 or head2 or carry != 0:
            digit1 = head1.data if head1 else 0
            digit2 = head2.data if head2 else 0

            sum_ = digit1 + digit2 + carry
            digit = sum_ % 10
            carry = sum_ // 10

            # Create a Node containing the digit
            newNode = Node(digit)
            ptr.next = newNode
            ptr = ptr.next

            head1 = head1.next if head1 else None
            head2 = head2.next if head2 else None

        self.head = dummyHead.next
        dummyHead.next = None


if __name__ == '__main__':
    obj = AddLinkedList()

    l1 = LinkedList()
    l1.insert(8)
    l1.insert(9)
    print(l1)

    l2 = LinkedList()
    l2.insert(2)
    l2.insert(9)
    print(l2)

    obj.add_two_lists(l1.head, l2.head)
    print(obj)
