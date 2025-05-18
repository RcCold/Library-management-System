class Book:
    # Represents a book with title, author, status, and unique ID
    id_counter = 1 
    
    def __init__(self, title, author):
        if not title or not author:
            raise ValueError("Title and author cannot be empty.")
        
        self.book_id = Book.id_counter
        Book.id_counter += 1 
        self.title = title
        self.author = author 
        self.status = "Available"

class Node:
    # Represents a node in the linked list
    def __init__(self, book):  
        if not isinstance(book, Book):
            raise TypeError("Expected a Book instance.")
        self.book = book
        self.next = None 

class SinglyLinkedlist:
    # Represents a singly linked list of Books
    def __init__(self):
        self.head = None 
    
    def append(self, book):
        if not isinstance(book, Book):
            raise TypeError("Expected a Book instance.")
        
        node = Node(book)
        if self.head is None:
            self.head = node
        else:
            current = self.head 
            while current.next:
                current = current.next
            current.next = node 

    def display(self, sort_by=None, algorithm='quicksort'):
        # Prints the books in the linked list sorted by a specified attribute
        if self.head is None:
            print("No books available.")
            return
        
        books = []
        current = self.head 
        while current:
            books.append(current.book)
            current = current.next 
        
        if sort_by:
            if algorithm == 'quicksort':
                SortingAlgorithms.quicksort(books, 0, len(books) - 1, sort_by)
            elif algorithm == 'mergesort':
                SortingAlgorithms.mergesort(books, sort_by)
        
        for book in books:
            print(f"ID: {book.book_id}, Title: {book.title}, Author: {book.author}, Status: {book.status}")

    def delete(self, book_id):
        if not isinstance(book_id, int) or book_id <= 0:
            raise ValueError("Book ID must be a positive integer.")
        
        current = self.head
        prev = None
        while current:
            if current.book.book_id == book_id:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                return True
            prev = current
            current = current.next
        return False
    
    def update(self, book_id, title=None, author=None):
        if not isinstance(book_id, int) or book_id <= 0:
            raise ValueError("Book ID must be a positive integer.")
        
        current = self.head
        while current:
            if current.book.book_id == book_id:
                if title:
                    current.book.title = title
                if author:
                    current.book.author = author
                return True
            current = current.next
        return False

class Stack:
    # Represents a stack to track book transactions 
    def __init__(self):
        self.items = []

    def push(self, transaction):
        if not isinstance(transaction, str) or not transaction.strip():
            raise ValueError("Transaction must be a non-empty string.")
        self.items.append(transaction)
    
    def pop(self):
        if not self.items:
            raise IndexError("Cannot pop from an empty stack.")
        return self.items.pop()
    
class HashTable:
    # Represents a hash table for efficient book searching
    def __init__(self):
        self.size = 10
        self.table = [[] for _ in range(self.size)]

    def hash_function(self, book_id):
        if not isinstance(book_id, int) or book_id <= 0:
            raise ValueError("Book ID must be a positive integer.")
        return book_id % self.size
    
    def insert(self, book):
        if not isinstance(book, Book):
            raise TypeError("Expected a Book instance.")
        index = self.hash_function(book.book_id)
        self.table[index].append(book)

    def search(self, book_id):
        if not isinstance(book_id, int) or book_id <= 0:
            raise ValueError("Book ID must be a positive integer.")
        
        index = self.hash_function(book_id)
        for book in self.table[index]:
            if book.book_id == book_id:
                return book
        return None

class SortingAlgorithms:
    @staticmethod
    def quicksort(books, low, high, key):
        if not books or low < 0 or high >= len(books) or low >= high:
            return
        try:
            pi = SortingAlgorithms.partition(books, low, high, key)
            SortingAlgorithms.quicksort(books, low, pi - 1, key)
            SortingAlgorithms.quicksort(books, pi + 1, high, key)
        except (AttributeError, TypeError) as e:
            print(f"Error during quicksort: {e}")
    
    @staticmethod
    def partition(books, low, high, key):
        try:
            pivot = getattr(books[high], key)
            i = low - 1
            for j in range(low, high):
                if getattr(books[j], key) <= pivot:
                    i += 1
                    books[i], books[j] = books[j], books[i]
            books[i + 1], books[high] = books[high], books[i + 1]
            return i + 1
        except AttributeError:
            print(f"Invalid sorting key: '{key}'")
            return low  # Return a valid index
    
    @staticmethod
    def mergesort(books, key):
        if not books or len(books) <= 1:
            return
        try:
            mid = len(books) // 2
            left_half = books[:mid]
            right_half = books[mid:]

            SortingAlgorithms.mergesort(left_half, key)
            SortingAlgorithms.mergesort(right_half, key)
            
            i = j = k = 0
            while i < len(left_half) and j < len(right_half):
                if getattr(left_half[i], key) < getattr(right_half[j], key):
                    books[k] = left_half[i]
                    i += 1
                else:
                    books[k] = right_half[j]
                    j += 1
                k += 1
            while i < len(left_half):
                books[k] = left_half[i]
                i += 1
                k += 1
            while j < len(right_half):
                books[k] = right_half[j]
                j += 1
                k += 1
        except AttributeError:
            print(f"Invalid sorting key: '{key}'")

class SearchingAlgorithms:
    @staticmethod
    def binary_search(books, target, key):
        if not books:
            print("Error: Book list is empty.")
            return None
        try:
            low, high = 0, len(books) - 1
            while low <= high:
                mid = (low + high) // 2
                if getattr(books[mid], key) == target:
                    return books[mid]
                elif getattr(books[mid], key) < target:
                    low = mid + 1
                else:
                    high = mid - 1
        except AttributeError:
            print(f"Invalid search key: '{key}'")
        return None

book_list = SinglyLinkedlist()
transaction_stack = Stack()
book_hash_table = HashTable()

def main():
    while True: 
        try:
            print("\nLibrary Management System")
            print("1. Add a book")
            print("2. Display book list")
            print("3. Search for a book")
            print("4. Check out a book")
            print("5. Return a book")
            print("6. Update book details")
            print("7. Delete a book")
            print("8. Search book by title")
            print("9. Exit")

            choice = input("Enter your choice: ").strip()
            
            if choice == "1":
                title = input("Enter book title: ").strip()
                author = input("Enter book author: ").strip()
                if not title or not author:
                    print("Error: Title and author cannot be empty.")
                    continue
                book = Book(title, author)
                book_list.append(book)
                book_hash_table.insert(book)
                print(f"Book '{title}' by {author} added successfully!")

            elif choice == "2":
                print("\nBook List:")
                sort_by = input("Sort by (title/author) or press Enter to skip: ").strip()
                if sort_by in ["title", "author"]:
                    algorithm = input("Choose sorting algorithm (quicksort/mergesort) [default: quicksort]: ").strip()
                    if algorithm not in ['quicksort', 'mergesort']:
                        algorithm = 'quicksort'
                    book_list.display(sort_by, algorithm)
                else:
                    book_list.display()
            
            elif choice == "3":
                try:
                    book_id = int(input("Enter book ID to search: ").strip())
                    found_book = book_hash_table.search(book_id)
                    if found_book:
                        print(f"Found: {found_book.title} by {found_book.author}")
                    else:
                        print("Book not found.")
                except ValueError:
                    print("Error: Please enter a valid numeric book ID.")

            elif choice == "4":
                try:
                    book_id = int(input("Enter book ID to check out: ").strip())
                    found_book = book_hash_table.search(book_id)
                    if found_book:
                        if found_book.status == "Available":
                            found_book.status = "Checked out"
                            transaction_stack.push(f"Checked out book with ID {book_id}")
                            print(f"Book '{found_book.title}' checked out successfully!")
                        else:
                            print("Book is already checked out.")
                    else:
                        print("Book not found.")
                except ValueError:
                    print("Error: Please enter a valid numeric book ID.")

            elif choice == "5":
                try:
                    book_id = int(input("Enter book ID to return: ").strip())
                    found_book = book_hash_table.search(book_id)
                    if found_book:
                        if found_book.status == "Checked out":
                            found_book.status = "Available"
                            transaction_stack.push(f"Returned book with ID {book_id}")
                            print(f"Book '{found_book.title}' returned successfully!")
                        else:
                            print("Book is already available.")
                    else:
                        print("Book not found.")
                except ValueError:
                    print("Error: Please enter a valid numeric book ID.")

            elif choice == "6":
                try:
                    book_id = int(input("Enter book ID to update: ").strip())
                    title = input("Enter new title (leave blank to keep unchanged): ").strip() or None
                    author = input("Enter new author (leave blank to keep unchanged): ").strip() or None
                    if book_list.update(book_id, title, author):
                        print("Book updated successfully!")
                    else:
                        print("Book not found.")
                except ValueError:
                    print("Error: Please enter a valid numeric book ID.")

            elif choice == "7":
                try:
                    book_id = int(input("Enter book ID to delete: ").strip())
                    if book_list.delete(book_id):
                        print("Book deleted successfully!")
                    else:
                        print("Book not found.")
                except ValueError:
                    print("Error: Please enter a valid numeric book ID.")
            
            elif choice == "8":
                title = input("Enter book title to search: ").strip()
                if not title:
                    print("Error: Title cannot be empty.")
                    continue
                books = []
                current = book_list.head
                while current:
                    books.append(current.book)
                    current = current.next
                books.sort(key=lambda x: x.title)
                found_book = SearchingAlgorithms.binary_search(books, title, 'title')
                if found_book:
                    print(f"Found: {found_book.title} by {found_book.author}")
                else:
                    print("Book not found.")
            
            elif choice == "9":
                print("Exiting the library management system. Goodbye!")
                break 
            
            else: 
                print("Invalid choice. Please pick a number from 1 to 9.")
        
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
