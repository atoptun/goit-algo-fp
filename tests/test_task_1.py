import pytest
from src.task_1 import LinkedList, Node


# LinkedList tests

def test_initialization():
    """Test that a new LinkedList is initialized correctly"""
    llist = LinkedList()
    assert llist.head is None


def test_insert_at_beginning_empty_list():
    """Test inserting into an empty list at the beginning"""
    llist = LinkedList()
    llist.insert_at_beginning(5)
    assert llist.head is not None
    assert llist.head.data == 5
    assert llist.head.next is None


def test_insert_at_beginning_multiple_elements():
    """Test inserting multiple elements at the beginning"""
    llist = LinkedList()
    llist.insert_at_beginning(5)
    llist.insert_at_beginning(10)
    llist.insert_at_beginning(15)
    
    # Check the order: 15 -> 10 -> 5
    assert llist.head is not None
    assert llist.head.data == 15
    assert llist.head.next is not None
    assert llist.head.next.data == 10
    assert llist.head.next.next is not None
    assert llist.head.next.next.data == 5
    assert llist.head.next.next.next is None


def test_insert_at_end_empty_list():
    """Test inserting into an empty list at the end"""
    llist = LinkedList()
    llist.insert_at_end(5)
    assert llist.head is not None
    assert llist.head.data == 5
    assert llist.head.next is None


def test_insert_at_end_multiple_elements():
    """Test inserting multiple elements at the end"""
    llist = LinkedList()
    llist.insert_at_end(5)
    llist.insert_at_end(10)
    llist.insert_at_end(15)
    
    # Check the order: 5 -> 10 -> 15
    assert llist.head is not None
    assert llist.head.data == 5
    assert llist.head.next is not None
    assert llist.head.next.data == 10
    assert llist.head.next.next is not None
    assert llist.head.next.next.data == 15
    assert llist.head.next.next.next is None


def test_insert_at_end_mixed_with_beginning():
    """Test mixing insertions at beginning and end"""
    llist = LinkedList()
    llist.insert_at_beginning(10)
    llist.insert_at_end(20)
    llist.insert_at_beginning(5)
    llist.insert_at_end(25)
    
    # Check the order: 5 -> 10 -> 20 -> 25
    current = llist.head
    expected_values = [5, 10, 20, 25]
    for expected in expected_values:
        assert current is not None
        assert current.data == expected
        current = current.next
    assert current is None


def test_insert_after_valid_node():
    """Test inserting after a valid node"""
    llist = LinkedList([10, 20])
    
    # Insert 15 after the first node (10)
    assert llist.head is not None  # Type guard
    llist.insert_after(llist.head, 15)
    
    # Check the order: 10 -> 15 -> 20
    assert llist.head.data == 10
    assert llist.head.next is not None
    assert llist.head.next.data == 15
    assert llist.head.next.next is not None
    assert llist.head.next.next.data == 20
    assert llist.head.next.next.next is None


def test_insert_after_none_node(capsys):
    """Test inserting after a None node"""
    llist = LinkedList()
    with pytest.raises(ValueError) as exc_info:
        llist.insert_after(None, 5) # type: ignore
    assert str(exc_info.value) == "The given previous node cannot be None."

    # List should remain empty
    assert llist.head is None


def test_delete_node_from_head():
    """Test deleting the head node"""
    llist = LinkedList([15, 10, 5])
    
    # Delete head node (15)
    llist.delete_node(15)
    
    # Check that 10 is now the head
    assert llist.head is not None
    assert llist.head.data == 10
    assert llist.head.next is not None
    assert llist.head.next.data == 5
    assert llist.head.next.next is None


def test_delete_node_from_middle():
    """Test deleting a node from the middle"""
    llist = LinkedList([15, 10, 5])
    # Delete middle node (10)
    llist.delete_node(10)
    
    # Check that 15 -> 5
    assert llist.head is not None
    assert llist.head.data == 15
    assert llist.head.next is not None
    assert llist.head.next.data == 5
    assert llist.head.next.next is None


def test_delete_node_from_tail():
    """Test deleting the tail node"""
    llist = LinkedList([15, 10, 5])
    # Delete tail node (5)
    llist.delete_node(5)
    
    # Check that 15 -> 10
    assert llist.head is not None
    assert llist.head.data == 15
    assert llist.head.next is not None
    assert llist.head.next.data == 10
    assert llist.head.next.next is None


def test_delete_node_not_found():
    """Test deleting a node that doesn't exist"""
    llist = LinkedList([10, 5])
    # Try to delete a non-existent node
    llist.delete_node(99)
    
    # List should remain unchanged
    assert llist.head is not None
    assert llist.head.data == 10
    assert llist.head.next is not None
    assert llist.head.next.data == 5
    assert llist.head.next.next is None


def test_delete_node_empty_list():
    """Test deleting from an empty list"""
    llist = LinkedList()
    llist.delete_node(5)
    assert llist.head is None


def test_delete_node_single_element():
    """Test deleting the only element in the list"""
    llist = LinkedList([5])
    llist.delete_node(5)
    assert llist.head is None


def test_search_element_found():
    """Test searching for an element that exists"""
    llist = LinkedList([15, 10, 5])
    result = llist.search_element(10)
    assert result is not None
    assert result.data == 10


def test_search_element_not_found():
    """Test searching for an element that doesn't exist"""
    llist = LinkedList([15, 10, 5])
    result = llist.search_element(99)
    assert result is None


def test_search_element_empty_list():
    """Test searching in an empty list"""
    llist = LinkedList()
    result = llist.search_element(5)
    assert result is None


def test_search_element_single_element_found():
    """Test searching in a single-element list - found"""
    llist = LinkedList([5])
    result = llist.search_element(5)
    assert result is not None
    assert result.data == 5


def test_search_element_single_element_not_found():
    """Test searching in a single-element list - not found"""
    llist = LinkedList([5])
    result = llist.search_element(10)
    assert result is None


def test_reverse_empty_list():
    """Test reversing an empty list"""
    llist = LinkedList()
    llist.reverse()
    assert llist.head is None


def test_reverse_single_element():
    """Test reversing a single-element list"""
    llist = LinkedList([5])
    llist.reverse()
    assert llist.head is not None
    assert llist.head.data == 5
    assert llist.head.next is None


def test_reverse_multiple_elements():
    """Test reversing a list with multiple elements"""
    llist = LinkedList([15, 10, 5])
    llist.reverse()
    
    # Check the order: 5 -> 10 -> 15
    assert llist.to_list() == [5, 10, 15]


def test_to_list_empty():
    """Test converting an empty list to a Python list"""
    llist = LinkedList()
    assert llist.to_list() == []


def test_to_list_multiple_elements():
    """Test converting a list with multiple elements to a Python list"""
    llist = LinkedList([15, 10, 5])
    assert llist.to_list() == [15, 10, 5]


def test_sort_empty_list():
    """Test sorting an empty list"""
    llist = LinkedList()
    llist.sort()
    assert llist.head is None


def test_sort_single_element():
    """Test sorting a single-element list"""
    llist = LinkedList([5])
    llist.sort()
    assert llist.to_list() == [5]


def test_sort_multiple_elements_ascending():
    """Test sorting a list with multiple elements in ascending order"""
    llist = LinkedList([15, 5, 10])
    llist.sort(reverse=False)
    assert llist.to_list() == [5, 10, 15]


def test_sort_multiple_elements_descending():
    """Test sorting a list with multiple elements in descending order"""
    llist = LinkedList([15, 5, 10])
    llist.sort(reverse=True)
    assert llist.to_list() == [15, 10, 5]


def test_sort_already_sorted():
    """Test sorting an already sorted list"""
    llist = LinkedList([5, 10, 15])
    llist.sort(reverse=False)
    assert llist.to_list() == [5, 10, 15]
    llist.sort(reverse=True)
    assert llist.to_list() == [15, 10, 5]


def test_sort_string_elements():
    """Test sorting a list with string elements"""
    llist = LinkedList(["banana", "apple", "cherry"])
    llist.sort(reverse=False)
    assert llist.to_list() == ["apple", "banana", "cherry"]
    llist.sort(reverse=True)
    assert llist.to_list() == ["cherry", "banana", "apple"]


def test_str_representation_empty():
    """Test string representation of an empty list"""
    llist = LinkedList()
    assert str(llist) == ""


def test_str_representation_multiple_elements():
    """Test string representation of a list with multiple elements"""
    llist = LinkedList([15, 10, 5])
    assert str(llist) == "15 -> 10 -> 5"



# Node tests ============================================

def test_node_initialization_with_data():
    """Test that a Node is initialized correctly with data"""
    node = Node(5)
    assert node.data == 5
    assert node.next is None


def test_node_linking():
    """Test linking nodes together"""
    node1 = Node(1)
    node2 = Node(2)
    node1.next = node2
    
    assert node1.next is node2
    assert node2.next is None


# Integration tests

def test_complex_scenario():
    """Test a complex scenario with multiple operations"""
    llist = LinkedList()
    
    # Build list: 15 -> 10 -> 5 -> 20 -> 25
    llist.insert_at_beginning(5)
    llist.insert_at_beginning(10)
    llist.insert_at_beginning(15)
    llist.insert_at_end(20)
    llist.insert_at_end(25)
    
    # Verify initial state
    assert llist.search_element(10) is not None
    assert llist.search_element(99) is None
    
    # Delete middle element
    llist.delete_node(10)
    
    # Verify deletion
    assert llist.search_element(10) is None
    
    # Insert after head
    assert llist.head is not None  # Type guard
    llist.insert_after(llist.head, 12)
    
    # Final list should be: 15 -> 12 -> 5 -> 20 -> 25
    current = llist.head
    expected_values = [15, 12, 5, 20, 25]
    for expected in expected_values:
        assert current is not None
        assert current.data == expected
        current = current.next
    assert current is None


def test_scenario_from_main_function():
    """Test the exact scenario from the main function"""
    llist = LinkedList()

    # Вставляємо вузли в початок
    llist.insert_at_beginning(5)
    llist.insert_at_beginning(10)
    llist.insert_at_beginning(15)

    # Вставляємо вузли в кінець
    llist.insert_at_end(20)
    llist.insert_at_end(25)

    # Check initial list: 15 -> 10 -> 5 -> 20 -> 25
    current = llist.head
    expected_values = [15, 10, 5, 20, 25]
    for expected in expected_values:
        assert current is not None
        assert current.data == expected
        current = current.next
    assert current is None

    # Видаляємо вузол
    llist.delete_node(10)

    # Check after deletion: 15 -> 5 -> 20 -> 25
    current = llist.head
    expected_values = [15, 5, 20, 25]
    for expected in expected_values:
        assert current is not None
        assert current.data == expected
        current = current.next
    assert current is None

    # Пошук елемента у зв'язному списку
    element = llist.search_element(15)
    assert element is not None
    assert element.data == 15


if __name__ == "__main__":
    pytest.main([__file__])