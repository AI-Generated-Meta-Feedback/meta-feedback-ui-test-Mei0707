from CODE import Book, sort_books


def test_case_1():
    """
    Test Case 1: All books from different shelves
    
    Purpose: Verifies basic sorting by shelf number
    """
    print("=" * 60)
    print("Test Case 1: All books from different shelves")
    print("=" * 60)
    
    # Input: books from different shelves in random order
    books = [
        Book(5, 3),
        Book(2, 1),
        Book(8, 2),
        Book(1, 1)
    ]
    
    print("Input:")
    print(books)
    
    # Expected output: sorted by shelf number
    expected = [
        Book(1, 1),
        Book(2, 1),
        Book(5, 3),
        Book(8, 2)
    ]
    
    print("\nExpected Output:")
    print(expected)
    
    # Sort the books
    result = sort_books(books)
    
    print("\nActual Output:")
    print(result)
    
    # Verify result
    assert result == expected, f"Test Case 1 FAILED: Expected {expected}, got {result}"
    print("\n✓ Test Case 1 PASSED\n")


def test_case_2():
    """
    Test Case 2: Multiple books from the same shelf (tests stability)
    
    Purpose: Tests that return order is preserved for books on the same shelf
    """
    print("=" * 60)
    print("Test Case 2: Multiple books from same shelf (stability)")
    print("=" * 60)
    
    # Input: multiple books from shelf 5 in wrong order
    books = [
        Book(5, 3),
        Book(2, 1),
        Book(5, 1),
        Book(5, 2)
    ]
    
    print("Input:")
    print(books)
    
    # Expected output: shelf 2 first, then shelf 5 books in return order
    expected = [
        Book(2, 1),
        Book(5, 1),
        Book(5, 2),
        Book(5, 3)
    ]
    
    print("\nExpected Output:")
    print(expected)
    
    # Sort the books
    result = sort_books(books)
    
    print("\nActual Output:")
    print(result)
    
    # Verify result
    assert result == expected, f"Test Case 2 FAILED: Expected {expected}, got {result}"
    print("\n✓ Test Case 2 PASSED (Stability verified)\n")


def test_case_3():
    """
    Test Case 3: Books already in correct order
    
    Purpose: Verifies algorithm correctly handles already-sorted input (best case)
    """
    print("=" * 60)
    print("Test Case 3: Books already in correct order")
    print("=" * 60)
    
    # Input: books already sorted
    books = [
        Book(1, 1),
        Book(2, 1),
        Book(3, 1),
        Book(3, 2)
    ]
    
    print("Input:")
    print(books)
    
    # Expected output: same as input
    expected = [
        Book(1, 1),
        Book(2, 1),
        Book(3, 1),
        Book(3, 2)
    ]
    
    print("\nExpected Output:")
    print(expected)
    
    # Sort the books
    result = sort_books(books)
    
    print("\nActual Output:")
    print(result)
    
    # Verify result
    assert result == expected, f"Test Case 3 FAILED: Expected {expected}, got {result}"
    print("\n✓ Test Case 3 PASSED (Best case handled correctly)\n")


def test_case_4():
    """
    Test Case 4: Books in reverse order
    
    Purpose: Tests worst-case scenario with reversed order and multiple books per shelf
    """
    print("=" * 60)
    print("Test Case 4: Books in reverse order")
    print("=" * 60)
    
    # Input: books in reverse order
    books = [
        Book(10, 2),
        Book(10, 1),
        Book(5, 2),
        Book(5, 1),
        Book(2, 1)
    ]
    
    print("Input:")
    print(books)
    
    # Expected output: sorted by shelf, then by return order
    expected = [
        Book(2, 1),
        Book(5, 1),
        Book(5, 2),
        Book(10, 1),
        Book(10, 2)
    ]
    
    print("\nExpected Output:")
    print(expected)
    
    # Sort the books
    result = sort_books(books)
    
    print("\nActual Output:")
    print(result)
    
    # Verify result
    assert result == expected, f"Test Case 4 FAILED: Expected {expected}, got {result}"
    print("\n✓ Test Case 4 PASSED (Worst case handled correctly)\n")


def run_all_tests():
    """Run all test cases."""
    print("\n" + "=" * 60)
    print("RUNNING ALL TEST CASES")
    print("=" * 60 + "\n")
    
    try:
        test_case_1()
        test_case_2()
        test_case_3()
        test_case_4()
        
        print("=" * 60)
        print("ALL TESTS PASSED! ✓")
        print("=" * 60)
        
    except AssertionError as e:
        print(f"\n❌ TEST FAILED: {e}")
        return False
    
    return True


if __name__ == "__main__":
    run_all_tests()

