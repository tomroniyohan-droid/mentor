library = []

def add_book():
    book = input("Enter book name to add: ")
    library.append(book)
    print("Book added successfully!")

def issue_book():
    book = input("Enter book name to issue: ")
    if book in library:
        library.remove(book)
        print("Book issued successfully!")
    else:
        print("Book not available in library")

def return_book():
    book = input("Enter book name to return: ")
    library.append(book)
    print("Book returned successfully!")

def search_book():
    book = input("Enter book name to search: ")
    if book in library:
        print("Book is available in the library")
    else:
        print("Book not found")

while True:
    print("\n--- Library Management System ---")
    print("1. Add Book")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. Search Book")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_book()
    elif choice == 2:
        issue_book()
    elif choice == 3:
        return_book()
    elif choice == 4:
        search_book()
    elif choice == 5:
        print("Exiting Library System...")
        break
    else:
        print("Invalid choice! Please try again.")