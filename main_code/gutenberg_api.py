import requests
import sys

url = 'https://gutendex.com/books/'

r = requests.get(url)

print(f"status code: {r.status_code}")

response_dict = r.json()

# print(response_dict.keys())

book_dict = response_dict['results']

def show_results(page):
  i=0
  for i in range(11*(page-1),11*page):

    print(f'{i}: {book_dict[i]['title']}')

  return None

user_input = None
page = 1

print('just say yes/next/exit')

while user_input != 'exit':


  show_results(page)  

  print('do you want to download?')
  user_input = input().lower()

  if user_input == 'yes':

    print('wchich number?')
    book_number = int(input())

    book_url = book_dict[book_number]['formats']['text/plain; charset=us-ascii']
    book_title = book_dict[book_number]['title']
    book_response = requests.get(book_url)
    file_path= f"/home/isaac/proyectos/bookbot/books/{book_title}.txt"

    if book_response.status_code == 200:

      with open(file_path, "w",encoding='utf-8') as f:
          f.write(book_response.text)
      print(f"archivo guardado como {file_path}")
    else:
      print(f"error en la request. status code: {book_response.status_code}")

  if user_input == 'next':
     page += 1
     

  if user_input == 'exit':
    sys.exit()
    




