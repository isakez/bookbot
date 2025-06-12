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




