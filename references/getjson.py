import json
from urllib.request import urlopen
import json

# sample ISBN for testing: 1593276036

api = "https://www.googleapis.com/books/v1/volumes?q=isbn:"
isbn = input("Enter 10 digit ISBN: ").strip()
resp = urlopen(api + isbn)
book_data = json.load(resp)

volume_info = book_data["items"][0]["volumeInfo"]

#* Getting author info
# author = volume_info["authors"]
# prettify_author = author if len(author) > 1 else author[0]

#* Writing to a JSON file
json_object = json.dumps(volume_info, indent = 4)
file = 'book.json'
with open(file, "w") as f:
    f.write(json_object)
print('JSON Data Written to',file)

#* JSON info output of the book
# print(volume_info)

#* display title, author, page count, publication date
# print(f"\nTitle: {volume_info['title']}")
# print(f"Author: {prettify_author}")
# print(f"Page Count: {volume_info['pageCount']}")
# print(f"Publication Date: {volume_info['publishedDate']}")
# print("\n***\n")

#* ask user if they would like to enter another isbn to fetch another book
# user_update = input("Would you like to enter another ISBN? y or n ").lower().strip()
# if user_update != "y":
#     print("May the Zen of Python be with you. Have a nice day!")
#     break # as the name suggests, the break statement breaks out of the while loop