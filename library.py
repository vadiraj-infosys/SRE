import csv

books = dict()
path = "Books.csv"

while(True):
    print("""
    1. Enter book details
    2. View books
    3. Search book
    4. Remove book
    5. Exit
    """)

    choice = input("Enter you choice: ")

    if choice == "1":
        bookid = int(input("Enter Book Id: "))
        booktitle = input("Enter Book Title: ")
        bookpages = int(input("Enter Book Pages: "))
        bookprice = float(input("Enter Book Price: "))

        if bookid in books.keys():
            print("Book already exists")
            continue
        else:
            books[bookid] = [booktitle, bookpages, bookprice]
            with open('Books.csv', 'a', newline='') as books_csv:
                writer = csv.writer(books_csv)
                bookdetails = [bookid,booktitle,bookprice,bookpages]
                writer.writerow(bookdetails)
            continue

    if choice == "2":
        with open('Books.csv', 'r') as books_csv:
            reader = csv.reader(books_csv)
            for r in reader:
                print(r)
        continue

    if choice == "3":
        id = int(input("Enter the book id: "))
        if id in books.keys():
            print(books[id])
        else:
            print("Book not found")
        continue

    if choice == "4":
        id = int(input("Enter the book id: "))
        if id in books.keys():
            books.pop(id)
        else:
            print("Book not found")

    if choice == "5":
        break
