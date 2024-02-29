"""A basic (singly) linked list implementation.

Two classes are defined here: Node and LList. The definition of the Node class
is followed by some utility functions and a mergesort function that sorts any
linked list of Node instances whose values are comparable.

The LList class provides methods with which to append, prepend, insert, and re-
move instances of Node to instances of LList. Methods to sort and deduplicate
instances of LList are also provided.
"""


class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None


def _middle(head):
    slow = fast = head
    if fast.next is None or fast.next.next is None:
        return slow
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    return slow


def _merge(left, right):
    """Iteratively merge two sorted linked lists of Node instances."""
    head = Node()
    current = head

    while left and right:
        if left.val <= right.val:
            current.next = left
            left = left.next
        else:
            current.next = right
            right = right.next
        current = current.next

    if left and not right:
        current.next = left
    if not left and right:
        current.next = right

    return head.next


def mergesort(head):
    """Merge sort a linked list of Node instances."""
    if head == None or head.next == None:
        return head

    mid = _middle(head)
    mid_next = mid.next
    mid.next = None

    return _merge(mergesort(head), mergesort(mid_next))


class LList:
    def __init__(self):
        self.head = None

    def prepend(self, val):
        newnode = Node(val)
        if self.head is None:
            self.head = newnode
        else:
            newnode.next = self.head
            self.head = newnode

    def append(self, val):
        newnode = Node(val)
        if self.head is None:
            self.head = newnode
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = newnode

    def remove(self, val):
        """Remove the first node whose value is val.

        If val does not occur, then leave self unchanged.
        """
        if self.head:
            if self.head.val == val:
                self.head = self.head.next
            else:
                node = self.head
                while node:
                    if node.next:
                        if node.next.val == val:
                            node.next = node.next.next
                            break
                    node = node.next

    def insert_after(self, current, val):
        pass

    def __str__(self):
        """Return a string representation."""

        string = ""
        if self.head is None:
            return string
        node = self.head
        while node.next:
            string += str(node.val) + ", "
            node = node.next
        string += str(node.val)
        return string

    def sort(self):
        """Sort in nondecreasing order."""
        self.head = mergesort(self.head)

    def dedup(self):
        pass

