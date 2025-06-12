import requests

url = 'https://gutendex.com/books/'

r = requests.get(url)

print(f"status code: {r.status_code}")

response_dict = r.json()

print(response_dict.keys())

book_dict = response_dict['results']
print(book_dict[0].keys())
print(book_dict[0]['formats']['text/plain; charset=us-ascii'])

book_url = book_dict[0]['formats']['text/plain; charset=us-ascii']

book_response = requests.get(book_url)

if book_response.status_code == 200:

    with open("frankestein.txt", "w",encoding='utf-8') as f:
        f.write(book_response.text)
    print("archivo guardado como frankstein.txt")
else:
    print(f"error en la request. status code: {book_response.status_code}")






