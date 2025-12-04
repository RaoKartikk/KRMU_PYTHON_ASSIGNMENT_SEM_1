# 📚 Library Inventory Manager

**Student Name:** Kartik          
**Roll Number:** 2501730166  
**Course:** Python Programming - Assignment 3

---

## 📖 Overview

The **Library Inventory Manager** is a comprehensive Python application for managing library books. It implements object-oriented programming principles with features for adding books, tracking their status (available/issued), searching the catalog, and maintaining persistent storage using JSON.

---

## ✨ Features

- 📖 **Book Management:** Add, search, and track books by ISBN
- 🔍 **Multiple Search Options:** Search by ISBN or title
- 📊 **Status Tracking:** Issue and return books with automatic status updates
- 💾 **Persistent Storage:** JSON-based catalog saved automatically
- 📝 **Logging System:** Comprehensive logs stored in `logs/library.log`
- ⚠️ **Custom Exceptions:** Proper error handling for various scenarios
- 🔒 **Data Encapsulation:** Private attributes with property decorators
- 🎯 **Efficient Lookups:** O(1) ISBN search using dictionary data structure

---

## 🚀 How to Run

1. **Navigate to the project directory:**
   ```bash
   cd ASSIGNMENT-3
   ```

2. **Run the program:**
   ```bash
   python library_manager.py
   ```

3. **Use the menu to:**
   - Add new books
   - Issue/return books
   - View all books
   - Search the catalog
   - Exit the application

---

## 📋 Menu Options

```
=== LIBRARY MANAGER ===
1. Add Book
2. Issue
3. Return
4. View All
5. Search
6. Exit

Choice (1-6):
```

---

## 💡 Usage Examples

### Adding a Book
```text
Choice (1-6): 1
ISBN: 978-0-13-468599-1
Title: Clean Code
Author: Robert C. Martin
Year: 2008
✅ Added: Clean Code
```

### Issuing a Book
```text
Choice (1-6): 2
ISBN to issue: 978-0-13-468599-1
✅ Book issued
```

### Searching Books
```text
Choice (1-6): 5
1. ISBN  2. Title
Search by: 2
Title: clean
✅ [978-0-13-468599-1] Clean Code by Robert C. Martin (2008) - ISSUED
```

### Viewing All Books
```text
Choice (1-6): 4

3 Books:
1. [978-0-13-468599-1] Clean Code by Robert C. Martin (2008) - ISSUED
2. [978-0-596-51774-8] Head First Python by Paul Barry (2016) - AVAILABLE
3. [978-1-491-91059-7] Fluent Python by Luciano Ramalho (2015) - AVAILABLE
```

---

## 🏗️ Architecture

### Classes

#### `Book`
Represents individual books with private attributes:
- `_isbn`: Unique identifier (ISBN)
- `_title`: Book title
- `_author`: Author name
- `_year`: Publication year
- `_status`: Current status (available/issued)

**Methods:**
- `issue()`: Mark book as issued
- `return_book()`: Mark book as returned
- `to_dict()`: Serialize to dictionary for JSON storage

#### `LibraryInventory`
Manages the entire book collection:
- Uses dictionary for O(1) ISBN lookups
- Handles JSON persistence
- Provides search functionality

**Methods:**
- `add_book(book)`: Add new book to catalog
- `search_by_isbn(isbn)`: Fast lookup by ISBN
- `search_by_title(title)`: Search with partial matching
- `issue_book(isbn)`: Issue a book
- `return_book(isbn)`: Return a book
- `display_all()`: Get all books

---

## 🧠 Python Concepts Demonstrated

### Object-Oriented Programming
- **Classes & Objects:** Book and LibraryInventory classes
- **Encapsulation:** Private attributes with `_` prefix
- **Properties:** `@property` decorators for controlled access
- **Inheritance:** Custom exception classes

### Data Structures
- **Dictionary:** O(1) ISBN lookups
- **Lists:** Book collections and search results

### File Operations
- **JSON Serialization:** Save/load catalog data
- **Logging:** Persistent application logs
- **Path Management:** Using `pathlib` module

### Error Handling
- **Custom Exceptions:** 
  - `BookNotFoundError`
  - `BookAlreadyIssuedError`
  - `BookNotIssuedError`
- **Try-Except Blocks:** Graceful error recovery
- **Input Validation:** User input checks

### Advanced Features
- **List Comprehensions:** Efficient filtering
- **String Methods:** `lower()`, `strip()` for search
- **Logging Module:** Multi-level logging
- **File I/O:** JSON read/write operations

---

## 📂 File Structure

```
ASSIGNMENT-3/
├── library_manager.py   # Main application
├── catalog.json         # Persistent book catalog
├── logs/
│   └── library.log      # Application logs
└── README.md            # This file
```

---

## 📊 Data Format

### catalog.json Structure
```json
{
  "978-0-13-468599-1": {
    "isbn": "978-0-13-468599-1",
    "title": "Clean Code",
    "author": "Robert C. Martin",
    "year": 2008,
    "status": "issued"
  },
  "978-0-596-51774-8": {
    "isbn": "978-0-596-51774-8",
    "title": "Head First Python",
    "author": "Paul Barry",
    "year": 2016,
    "status": "available"
  }
}
```

---

## 🔧 Requirements

- **Python 3.6+** (for f-strings and pathlib)
- **Standard Library Only:** No external dependencies

---

## 📝 Features Highlights

### Automatic Logging
All operations are logged to `logs/library.log`:
```
INFO: Loaded 3 books
INFO: Added: 978-0-13-468599-1
INFO: Issued: Clean Code
ERROR: Book not found: 978-1-234-56789-0
```

### Data Persistence
- Catalog automatically saved after each modification
- Survives program restarts
- JSON format for easy inspection/editing

### Error Messages
Clear, user-friendly error messages:
- ✅ Success indicators
- ❌ Error indicators
- Detailed exception messages

---

## 🎯 Learning Objectives

1. **OOP Principles:** Understand classes, objects, and encapsulation
2. **Data Structures:** Efficient use of dictionaries and lists
3. **File I/O:** JSON serialization and logging
4. **Exception Handling:** Custom exceptions and error recovery
5. **Code Organization:** Clean, modular, maintainable code
6. **Documentation:** Clear docstrings and comments

---

## 🐛 Error Handling Examples

```python
# Attempting to issue an already-issued book
❌ Book already issued

# Searching for non-existent ISBN
❌ No book with ISBN: 978-1-234-56789-0

# Returning a book that wasn't issued
❌ Book not issued
```

---

## 👨‍💻 Author

**Kartik**              
Roll Number: 2501730166   
B.Tech CSE (AI & ML)  
K.R. Mangalam University

---

## 📄 License

This project is created for educational purposes as part of Python Programming coursework.
