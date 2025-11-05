class Book:
    """Represents a library book with shelf number and return order."""
    
    def __init__(self, shelf_number, return_order):
        """
        Initialize a Book object.
        
        Args:
            shelf_number (int): The shelf number where the book belongs (1-50)
            return_order (int): The sequence number indicating when the book was returned
        """
        self.shelf_number = shelf_number
        self.return_order = return_order
    
    def __repr__(self):
        """String representation of the book for easier debugging."""
        return f"(shelf: {self.shelf_number}, order: {self.return_order})"
    
    def __eq__(self, other):
        """Check if two books are equal (same shelf and order)."""
        if not isinstance(other, Book):
            return False
        return self.shelf_number == other.shelf_number and self.return_order == other.return_order


def comes_before(book_a, book_b):
    """
    Determines if book_a should come before book_b in the sorted order.
    
    Comparison logic:
    - Primary: Sort by shelf number (ascending)
    - Secondary: Sort by return order (ascending) for books on same shelf
    
    Args:
        book_a (Book): First book to compare
        book_b (Book): Second book to compare
    
    Returns:
        bool: True if book_a should come before book_b, False otherwise
    """
    # If book_a has smaller shelf number, it comes first
    if book_a.shelf_number < book_b.shelf_number:
        return True
    
    # If same shelf, compare return order
    if book_a.shelf_number == book_b.shelf_number:
        if book_a.return_order < book_b.return_order:
            return True
    
    # Otherwise, book_a comes after book_b
    return False


def sort_books(books):
    """
    Sorts books using Insertion Sort algorithm.
    
    Books are sorted by:
    1. Shelf number (primary, ascending)
    2. Return order (secondary, ascending) - preserves order for same shelf
    
    This is a stable sort, meaning books on the same shelf maintain their
    relative return order.
    
    Args:
        books (list): List of Book objects to sort
    
    Returns:
        list: Sorted list of Book objects
    
    Time Complexity:
        - Best case: O(n) when already sorted
        - Average case: O(n²)
        - Worst case: O(n²) when reverse sorted
    
    Space Complexity: O(1) - sorts in place
    """
    n = len(books)
    
    # Insertion Sort: iterate through unsorted portion
    for i in range(1, n):
        # Select current book to insert into sorted portion
        current_book = books[i]
        j = i - 1
        
        # Shift books that should come after current_book
        # Move backwards through sorted portion
        while j >= 0 and comes_before(current_book, books[j]):
            books[j + 1] = books[j]  # Shift book one position right
            j -= 1
        
        # Insert current_book at correct position
        books[j + 1] = current_book
    
    return books


# Example usage
if __name__ == "__main__":
    # Example from the problem statement
    books = [
        Book(5, 3),
        Book(2, 1),
        Book(5, 2)
    ]
    
    print("Before sorting:")
    print(books)
    
    sorted_books = sort_books(books)
    
    print("\nAfter sorting:")
    print(sorted_books)
    
    # Expected output: [(shelf: 2, order: 1), (shelf: 5, order: 2), (shelf: 5, order: 3)]