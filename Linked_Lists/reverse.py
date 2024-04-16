'''
Reverse a singly linked list
'''

from LinkedList import LinkedList, Node

class ReverseLinkedList(LinkedList):
    def reverse(self, head: Node) -> None:
        prev = None
        curr = head

        while curr:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
        self.head = prev



if __name__ == '__main__':
    ll = LinkedList()
    ll.insert(3)
    ll.insert(4)
    ll.insert(5)
    ll.insert(6)
    print(ll)
    rll = ReverseLinkedList()
    rll.reverse(ll.head)
    print(rll)
    print(dir(ReverseLinkedList))






