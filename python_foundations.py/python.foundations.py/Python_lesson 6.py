# Initialize an empty list
favorite_books_list = []

first_book = (input("What is your first favorite book?: "))
second_book = (input("What is your second favorite book?: "))
third_book = (input("What is your third favorite book?: "))

favorite_books_list.append(first_book)
favorite_books_list.append(second_book)
favorite_books_list.append(third_book)
print(favorite_books_list)

favorite_books_list.sort()
print(favorite_books_list)
favorite_books_list.reverse()
print(favorite_books_list)