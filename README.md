# Python 3 OOP Project - Book Reading Application

## Project Description

This Python 3 project is a Book Reading Application that employs
Object-Oriented Programming (OOP) principles.
The application allows users to create accounts as either administrators or normal users.
Administrators can add books with ISBN, author names, book titles, and book content.
Normal users have the option to continue reading from their book history or open a new book to read from.

## Features

### User Authentication

- Users can create accounts as administrators or normal users.
- Administrators can log in with their credentials to access admin-specific features.
- Normal users can log in to access their book history or read new books.

### Administrator Features

- Administrators can add books to the system with the following information:
  - ISBN (International Standard Book Number)
  - Author Name
  - Book Title
  - Book Content

### Normal User Features

- Normal users can open and read books from their history or start reading a new book.

## Object-Oriented Design

### Classes

1. `User` Class:
   - Properties:
     - Username
     - Password
     - User Type (admin or normal)
   - Methods:
     - Login
     - Logout

2. `Book` Class:
   - Properties:
     - ISBN
     - Author Name
     - Book Title
     - Book Content
   - Methods:
     - Display Book Information
     - Add Book
     - Read Book

## Usage

To use this Book Reading Application, follow these steps:

1. Run the Python application.
2. Create a new user account (administrator or normal user).
3. Log in with your credentials.
4. Administrators can add books to the library.
5. Normal users can view their book history and start reading books.

## Conclusion

This Python 3 OOP project provides a user-friendly interface for reading books. Administrators can manage the books, and normal users can enjoy reading their favorite books.

Happy reading!