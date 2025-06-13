### archivo principal para extraer y analizar textos

import requests
from stats_book import *
import sys



def main():
 
 if len(sys.argv) != 2:
        print("para un correcto funcionamiento usa dos argumentos python3 main.py <direccion  archivo de texto>")
        sys.exit(1)

 relative_path = sys.argv[1]
        
 contenido = get_book_text(relative_path)
 num_words = get_words_text(contenido)
 print(f"{num_words} words found in the document")
 dict_char = get_char_text(contenido)
 
 dict_char_ordenado = sorted_dict(dict_char)
 print(dict_char_ordenado)

    

main()

