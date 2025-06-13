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

    for char in lista_caracteres:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1

    return char_dict

def my_sort(dict):
    return dict['num']

def sorted_dict(char_dict):
    llaves = list(char_dict.keys())
    valores = list(char_dict.values())
    lista_dict =[]
    i=0 
    for i in range(len(llaves)):
        if llaves[i].isalpha():

            lista_dict.append({"char":llaves[i],"num":valores[i]})
    
    lista_dict.sort(reverse = True, key=my_sort)

    return lista_dict



    








