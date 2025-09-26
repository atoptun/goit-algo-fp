from typing import Optional


class Node:
    """A node in a singly linked list."""
    def __init__(self, data):
        self.data = data
        self.next: Node | None = None


class LinkedList:
    """A singly linked list."""
    def __init__(self, items: list | None = None):
        self.head: Node | None = None
        if items:
            for item in items:
                self.insert_at_end(item)

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            raise ValueError("The given previous node cannot be None.")
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next # type: ignore
        cur = None

    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def sort(self, *, reverse: bool = False):
        
        self.head = self._merge_sort(self.head, reverse)

    def _merge_sort(self, head: Optional[Node], reverse: bool) -> Optional[Node]:
        if head is None or head.next is None:
            return head

        mid = self._get_middle(head)
        second_half = mid.next
        mid.next = None

        left = self._merge_sort(head, reverse)
        right = self._merge_sort(second_half, reverse)

        sorted_list = self._sorted_merge(left, right, reverse)
        return sorted_list
    
    def _get_middle(self, head: Node) -> Node:
        if head is None:
            return head
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next  # type: ignore
            fast = fast.next.next
        return slow  # type: ignore

    def _sorted_merge(self, left: Optional[Node], right: Optional[Node], reverse: bool) -> Optional[Node]:
        dummy = Node(0)
        tail = dummy

        while left and right:
            if (left.data < right.data) != reverse:
                tail.next = left
                left = left.next
            else:
                tail.next = right
                right = right.next
            tail = tail.next
        tail.next = left if left else right
        return dummy.next

    def to_list(self) -> list:
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements

    def __str__(self) -> str:
        current = self.head
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        return " -> ".join(elements)


def main():
    llist = LinkedList([201, 5, 2511, 10, 151])
    print("Initial list:\n", llist)

    llist.reverse()
    print("Reversed list:\n", llist)

    llist.sort()
    print("Sorted list:\n", llist)

    llist.sort(reverse=True)
    print("Sorted in descending order:\n", llist)


if __name__ == "__main__":
    main()