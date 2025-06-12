### Funcion para acceder y leer los bloques de texto



def get_book_text(filepath):

    with open(filepath) as f:

        file_contents = f.read()


    return file_contents



def get_words_text(contenido):

    lista_palabras = contenido.split()
    num_palabras = len(lista_palabras)
    #print(lista_palabras)
    return num_palabras


def get_char_text(contenido):
    char_dict = {}
    lista_caracteres = contenido.lower()
    lista_caracteres = list(lista_caracteres)
    count = 0
    for char in lista_caracteres:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1

    return char_dict

