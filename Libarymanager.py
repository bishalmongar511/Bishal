# Initialize empty lists, set, and dictionary
books_list= []
authors_set = set()
books_dict = {}

# Add books
books_list.append("Python programming")
authors_set.add("John smit")
books_dict["Python programming"] = "John smit"

books_list.append("Data structure and Algorithms")
authors_set.add("Jane Doe")
books_dict["Data structure and Algorithms"] = "Jane Doe"

books_list.append("Machine Learning Basics")
authors_set.add("Alice Johnson")
books_dict["Machine Learning Basics"] = "Alice Johnson"

#Search for a book
search_title = input("Enter the title of the book to search: ")
if search_title in books_list:
    print(f"Book found! Author: {books_dict[search_title]}")
else:
    print("Books not found!")

#Display all books
print("list of Books: ")
for book in books_list:
    print(book)

# Remove a book 
remove_title = input("Enter the title of the book to remove or else enter to skip: ")
if remove_title in books_list:
     remove_author = books_dict[remove_title]
     books_list.remove(remove_title)
     authors_set.remove(remove_author)
     del books_dict[remove_title]
     print("Book removed successfully!")
     print("Book avaliable: ", books_list)

else:
    print("Book not found!")
