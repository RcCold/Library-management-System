# Library-management-System
### Python Library Management System - Group Project

For our Data Structures and Algorithms class, our group created this Library Management System using Python. We implemented several key data structures and algorithms we learned throughout the semester to build a functional system that can handle basic library operations.

## What Our Project Does

Our Library Management System lets users:

- Add new books to the library
- Search for books by ID or title
- Check out and return books
- Update book information
- Delete books from the system
- Sort the book list by title or author


## Data Structures We Used

### Linked List

We used a singly linked list as our main data structure to store all the books. Each node contains a book object and points to the next node. We chose this because it made it easy to add new books and update the collection.

### Hash Table

To make searching for books by ID faster, we implemented a hash table. This gives us O(1) lookup time in most cases, which is way better than searching through the whole linked list every time.

### Stack

We used a stack to keep track of book transactions (checkouts and returns). This was perfect since we only needed to know the most recent transactions.

## Algorithms We Implemented

### Sorting

We added two sorting algorithms that users can choose from:

- **QuickSort**: Usually faster but can be slower in some cases
- **MergeSort**: More consistent performance but uses more memory


### Searching

We implemented binary search for finding books by title. This works much faster than checking every book, but the books need to be sorted first.

## Challenges We Faced

One of the biggest challenges was making sure all the data structures worked together properly. For example, when a book is deleted from the linked list, we needed to make sure it was also removed from the hash table.

Error handling was another challenge - we had to add a lot of try/except blocks to handle invalid inputs and edge cases.

## What We Learned

This project helped us understand how to apply data structures and algorithms to solve real-world problems. We got to see firsthand how different data structures have different strengths and weaknesses:

- Linked lists are great for dynamic collections
- Hash tables make searching super fast
- Stacks are perfect for tracking history
- Sorting algorithms have different trade-offs


We also learned a lot about working as a team, dividing tasks, and integrating our code together.

## Time and Space Complexity

----------------------------------------------------------------
| Operation       | Average Time | Worst Time | Data Structure |
|-----------------|--------------|------------|----------------|
| Add Book        |     O(1)     |    O(n)    | Linked List    |
| Search by ID    |     O(1)     |    O(n)    | Hash Table     |
| Search by Title |   O(log n)   |    O(n)    | Binary Search  |
| Sort Books      |  O(n log n)  |    O(n²)   | QuickSort      |
----------------------------------------------------------------

Overall, this project gave us hands-on experience with the concepts we learned in class and showed us how they can be used to build something useful!

