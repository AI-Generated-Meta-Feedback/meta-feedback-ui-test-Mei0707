# Library Book Return System - Design Plan

## Part A: Design Plan

### 1. Algorithm Choice

**Selected Algorithm: Insertion Sort**

#### Why Insertion Sort?

- **Stability**: Insertion Sort is a stable sorting algorithm, which is critical for this problem
- **Simplicity**: Easy to implement correctly with minimal chance of bugs
- **Performance**: For 25 books, O(n²) time complexity is acceptable
- **Adaptive behavior**: Performs efficiently (approaching O(n)) when data is partially sorted

#### Is your algorithm stable? Why does stability matter here?

Yes, Insertion Sort is **stable**. A sorting algorithm is stable when it preserves the relative order of elements with equal keys.

**Why stability matters for this problem:**

Books on the same shelf must maintain their return order (the sequence in which they were returned). The book returned first should be placed back on the shelf first. If we used an unstable sort like Selection Sort, books from the same shelf could be rearranged incorrectly, violating the requirement that "the book returned first goes back on the shelf first."

**Example:**
- Input: (shelf: 5, order: 3), (shelf: 5, order: 1), (shelf: 5, order: 2)
- Required output: (shelf: 5, order: 1), (shelf: 5, order: 2), (shelf: 5, order: 3)
- An unstable sort might produce: (shelf: 5, order: 2), (shelf: 5, order: 1), (shelf: 5, order: 3) 

### 2. Sorting Strategy

#### When comparing two books, what determines which comes first?

**Primary criterion: Shelf Number**
- Books are first sorted by shelf number in ascending order (shelf 1 before shelf 2, etc.)

**Secondary criterion: Return Order**
- For books on the same shelf, they are sorted by return order in ascending order (book returned first comes first)

#### If both books belong to shelf 5, how do you decide their order?

Compare their `returnOrder` values. The book with the smaller `returnOrder` (returned earlier) comes first.

**Example:** 
- Book A: (shelf: 5, order: 2)
- Book B: (shelf: 5, order: 1)
- Result: Book B comes before Book A

#### Comparison Rule (clearly written):

```
Book A comes before Book B if:
  (A.shelfNumber < B.shelfNumber) 
  OR 
  (A.shelfNumber == B.shelfNumber AND A.returnOrder < B.returnOrder)
```

### 3. Complexity

#### Time complexity for 25 books in random order?

**Insertion Sort time complexity:**
- **Best case**: O(n) = O(25) - when books are already sorted
- **Average case**: O(n²) = O(625) - random order
- **Worst case**: O(n²) = O(625) - reverse sorted order

For 25 books in random order, we expect approximately **O(n²) = O(625)** comparisons.

#### Would this change if books were already mostly sorted by shelf number?

**Yes!** Insertion Sort is an **adaptive algorithm**.

If books are already mostly sorted by shelf number:
- Time complexity approaches **O(n)** 
- Each book would require fewer comparisons to find its correct position
- Only books on the same shelf might need reordering based on return order
- This makes Insertion Sort particularly efficient for "nearly sorted" data

**Example:** If we have 25 books where most are already grouped by shelf (e.g., all shelf 1 books together, all shelf 2 books together), the algorithm would perform significantly faster than O(n²).

---

## Part B: Implementation

```pseudocode
FUNCTION sortBooks(books)
    // Input: Array of book objects with shelfNumber and returnOrder fields
    // Output: Sorted array of books
    // Sorts by shelf number primarily, return order secondarily (stable)
    
    n = LENGTH(books)
    
    // Insertion Sort: iterate through unsorted portion
    FOR i = 1 TO n - 1
        // Select current book to insert into sorted portion
        currentBook = books[i]
        j = i - 1
        
        // Shift books that should come after currentBook
        // Move backwards through sorted portion
        WHILE j >= 0 AND comesBefore(currentBook, books[j])
            books[j + 1] = books[j]  // Shift book one position right
            j = j - 1
        END WHILE
        
        // Insert currentBook at correct position
        books[j + 1] = currentBook
    END FOR
    
    RETURN books
END FUNCTION


FUNCTION comesBefore(bookA, bookB)
    // Returns TRUE if bookA should come before bookB
    // Comparison logic: sort by shelf number, then by return order
    
    // If bookA has smaller shelf number, it comes first
    IF bookA.shelfNumber < bookB.shelfNumber THEN
        RETURN TRUE
    END IF
    
    // If same shelf, compare return order
    IF bookA.shelfNumber == bookB.shelfNumber THEN
        IF bookA.returnOrder < bookB.returnOrder THEN
            RETURN TRUE
        END IF
    END IF
    
    // Otherwise, bookA comes after bookB
    RETURN FALSE
END FUNCTION
```

**Key Points:**
- **Function signature**: `sortBooks(books)` takes an array and returns sorted array
- **Comparison logic**: Implemented in `comesBefore()` - checks shelf number first, then return order
- **Stability preserved**: Only shifts elements when strictly less than (not equal)
- **Comments**: Explain each key step of the algorithm

---

## Part C: Testing Strategy

### Test Case 1: All books from different shelves
```
Input: 
[(shelf: 5, order: 3), (shelf: 2, order: 1), (shelf: 8, order: 2), (shelf: 1, order: 1)]

Expected Output:
[(shelf: 1, order: 1), (shelf: 2, order: 1), (shelf: 5, order: 3), (shelf: 8, order: 2)]

Purpose: Verifies basic sorting by shelf number
```

### Test Case 2: Multiple books from the same shelf (tests stability)
```
Input:
[(shelf: 5, order: 3), (shelf: 2, order: 1), (shelf: 5, order: 1), (shelf: 5, order: 2)]

Expected Output:
[(shelf: 2, order: 1), (shelf: 5, order: 1), (shelf: 5, order: 2), (shelf: 5, order: 3)]

Purpose: Tests that return order is preserved for books on the same shelf (stability requirement)
```

### Test Case 3: Books already in correct order
```
Input:
[(shelf: 1, order: 1), (shelf: 2, order: 1), (shelf: 3, order: 1), (shelf: 3, order: 2)]

Expected Output:
[(shelf: 1, order: 1), (shelf: 2, order: 1), (shelf: 3, order: 1), (shelf: 3, order: 2)]

Purpose: Verifies algorithm correctly handles already-sorted input (best case scenario)
```

### Test Case 4: Books in reverse order
```
Input:
[(shelf: 10, order: 2), (shelf: 10, order: 1), (shelf: 5, order: 2), (shelf: 5, order: 1), (shelf: 2, order: 1)]

Expected Output:
[(shelf: 2, order: 1), (shelf: 5, order: 1), (shelf: 5, order: 2), (shelf: 10, order: 1), (shelf: 10, order: 2)]

Purpose: Tests worst-case scenario with reversed order and multiple books per shelf
```