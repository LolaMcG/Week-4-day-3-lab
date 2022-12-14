from models.book import Book
from models.author import Author

import repositories.author_repository as author_repository
import repositories.book_repository as book_repository

# book_repository.delete_all()
# author_repository.delete_all()

author_1 = Author("Haruki Murakami")
author_repository.save(author_1)
author_2 = Author("Paulo Coelho")
author_repository.save(author_2)

book_1 = Book("Kafka On The Shore", author_1)
book_repository.save(book_1)
book_2 = Book("The Alchemist", author_2)
book_repository.save(book_2)

