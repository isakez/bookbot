### archivo principal para extraer y analizar textos

import requests
from stats import *

relative_path = '/home/isaac/proyectos/bookbot/books/frankenstein.txt'

def main():

 contenido = get_book_text(relative_path)
 num_words = get_words_text(contenido)
 
 print(f"{num_words} words found in the document")
    
main()

