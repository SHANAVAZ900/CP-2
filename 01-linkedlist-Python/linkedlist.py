"""The LinkedList code from before is provided below.
Add three functions to the LinkedList.
"get_position" returns the element at a certain position.
The "insert" function will add an element to a particular
spot in the list.
"delete" will delete the first element with that
particular value.
Then, use "Test Run" and "Submit" to run the test cases
at the bottom."""


class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        # Your code goes here
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        # Your code goes here
        if self.head:
            count = 1
            current = self.head
            if count == position:
                return current
            while position > count and current.next:
                current = current.next
                count += 1
                if count == position:
                    return current
            return None
        else:
            return None

    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        # Your code goes here
        if self.head:
            count = 1
            current = self.head
            while position - 1 > count:
                current = current.next
                count += 1
            temp = current.next
            current.next = new_element
            current.next.next = temp
        else:
            self.head = new_element

    def delete(self, value):
        """Delete the first node with a given value."""
        # Your code goes here
        current = self.head
        if current.value == value:
            self.head = current.next
            current = None
        while current:
            if current.value == value:
                prev.next = current.next
            prev = current
            current = current.next
