class Node:
    '''Node class for linked list. This class is used to store the data of a linked list.
    :param data: contains the data of a linked list
    :param next: contains address of the next node of a linked list'''

    __slots__ = "_data", "_next"

    def __init__(self, data, next=None):
        self._data = data
        self._next = next


class LinkedList:
    '''This is singly linked list, where each node is linked to the next node.
    :param head: contains of head node of the linked list
    :param tail: contains tail node of the linked list
    :param size: size of the linked list'''
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):
        ''':return: returns the size of the linked list'''
        return self.size

    def isEmpty(self):
        '''Checks if the linked list is empty
        :return: bool'''
        return self.size == 0

    def insert_at_begining(self, data):
        '''Inserts the data at the begining of the linked list
        :param data: element to be inserted at the begining of the linked list
        :return: None'''
        newNode = Node(data)
        if self.isEmpty():
            self.head = newNode
            self.tail = newNode
        else:
            newNode._next = self.head
            self.head = newNode
        self.size += 1

    def insert_at_end(self, data):
        '''Inserts the data at the end of the linked list
        :param data: element to be inserted at the end of the linked list
        :return: None'''
        newNode = Node(data, next=None)
        if self.isEmpty():
            self.head = newNode
        else:
            self.tail._next = newNode
        self.tail = newNode
        self.size += 1

    def insert_at_position(self, data, position:int):
        '''Inserts the data at the given position of the linked list
        :param data: element to be inserted at the given position of the linked list
        :param position: position of the element to be inserted in the linked list
        :return: None'''
        if position < 1:
            print("Position must be greater than or equal to 1")
            return

        #Traversing to (position-1)th node
        current = self.head
        for _ in range(1,position-1):
            if current is None:
                print("Position exceeds length of list")
                return
            current = current._next

        #Create a node with given data
        newNode = Node(data)

        #Insert the node at given location
        newNode._next = current._next
        current._next = newNode

        self.size += 1


    def delete_at_first(self):
        '''deletes the first element from the linked list
        :return: updated head node of linked list'''
        if self.isEmpty():
            print("The linked list is empty")
            return None
        self.head = self.head._next
        self.size -= 1
        return self.head


    def delete_at_last(self):
        '''deletes the last element from the linked list
        :return: deleted node of linked list'''
        if self.isEmpty():
            print("The linked list is empty")
            return None
        current = self.head
        for _ in range(self.size):
            if current._next._next is None:
                data = current._next._data
                current._next = None
                self.size -= 1
                return data
            current = current._next


    def delete_at_position(self, position:int):
        '''deletes the element at the given position from the linked list.
        :param position: position of the element to be deleted from the linked list, position must be >= 1
        :return: deleted element at the given position from the linked list'''
        if position < 1:
            print("Position must be greater than or equal to 1")
            return

        current = self.head
        for idx in range(position):
            if current is None:
                print("Position exceeds length of list")
                return
            if position == idx+1:
                element = current._data
                current._next = current._next._next
                self.size -= 1
                return element
            current = current._next


    def search_index(self, element):
        '''Checks if element is present in the linked list
        :param element: element to be searched
        :return: index of the element present in the linked list'''
        current = self.head
        for idx in range(self.size):
            if element == current._data:
                return idx
            current = current._next
        return -1


    def display_linked_list(self):
        '''Displays the linked list
        :return: None'''
        current = self.head
        while current:
            print(current._data, end=' -> ')
            current = current._next
        print("None")


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_end(3)
    ll.insert_at_end(4)
    ll.insert_at_end(5)
    ll.insert_at_end(6)
    ll.insert_at_begining(1)
    ll.insert_at_position(11, 3)
    ll.display_linked_list()
    print(ll.search_index(3))
    ll.delete_at_position(1)
    ll.display_linked_list()
    ll.delete_at_first()
    ll.display_linked_list()
    ll.delete_at_last()
    ll.display_linked_list()

