
"""
Python Katas - Entregable
Autor: Miriam Lopez
Archivo con la resolución de los ejercicios prácticos Katas.

"""
# =========================================
# Ejercicio 1
# Enunciado:
# Escribe una función que reciba una c como parámetro y devuelva
# un diccionario con las frecuencias de cada letra en la cadena.
# Los espacios no deben ser considerados.
# =========================================

def ejercicio_1(cadena):
    """Función que reciba una c como parámetro y devuelva
       un diccionario con las frecuencias de cada letra en la cadena.

    Args:
        cadena (str): cadena de texto sobre la que s eva a ejecutar la funcion

    Returns:
        dict: frecuencias de cada letra en la cadena. clave: letra / valor: frecuecnia de esa letra
    """    
    frecuencias = {}

    for letra in cadena:
        if letra != " ":
            if letra in frecuencias:
                frecuencias[letra] += 1
            else:
                frecuencias[letra] = 1

    return frecuencias

#Comprobacion.   
#print(ejercicio_1("hola hola"))


# =========================================
# Ejercicio 2
# Enunciado:
# Dada una lista de números, obtén una nueva lista con el doble de cada valor.
# Usa la función map()
# =========================================

def ejercicio_2(lista_numeros):
    """Funcion que dada una lista de números, obtiene una nueva lista con el doble de cada valor

    Args:
        lista_numeros(list): list de numeros
    
    Returns:
        list: Nueva lista con el doble de cada valor original de list
    """    
    lista_dobles = []

    lista_dobles = list(map(lambda x: x * 2, lista_numeros))
    
    return lista_dobles
        
#Comprobacion.   
#print(ejercicio_2([1,2,3]))


# =========================================
# Ejercicio 3
# Enunciado:
# Escribe una función que tome una lista de palabras y una palabra objetivo
# como parámetros. La función debe devolver una lista con todas las palabras
# de la lista original que contengan la palabra objetivo.
# =========================================

def ejercicio_3(lista_palabras, palabra_objetivo):
    """función que toma una lista de palabras y una palabra objetivo como parámetros. La función devuelve
        una lista con todas las palabras de la lista original que contengan la palabra objetivo.

    Args:
        lista_palabras (list): lista de palabras
        palabra_objetivo (str): Palabra que vamos a comprobar si esta contenida en cada una de las palabras de la lista anterior.

    Returns:
        list: Nueva lista con todas las palabras de la lista original que contengan la palabra objetivo
    """    
    nueva_lista = []
    
    for palabra in lista_palabras:
        if palabra_objetivo in palabra:
            nueva_lista.append(palabra)


    return nueva_lista


#Comprobacion.   
#print(ejercicio_3(["lo","arbol","coche","ardilla", "caracol", "pimiento", "col"], "ol"))

# =========================================
# Ejercicio 4
# Enunciado:
# Genera una función que calcule la diferencia entre los valores de dos listas.
# Usa la función map()
# =========================================

def ejercicio_4(lista_1, lista_2):
    """Función que calcula la diferencia entre los valores de dos listas. map va a iterar hasta que acabe la lista mas corta si no tinene la misma longitud las dos listas y no lnazará error

    Args:
        lista_1 (list): primera lista
        lista_2 (list): segunda lista
    Returns: 
        list: Lista con la difernecia entre los dos valores.
    """
    lista_final = list(map(lambda x,y: abs(x-y) , lista_1, lista_2))
    return lista_final


#Comprobacion.   
#print(ejercicio_4([1,2,3,4], [4,1,1,2]))
#print(ejercicio_4([1,1,3,4], [4,1]))

# =========================================
# Ejercicio 5
# Enunciado:
# Escribe una función que tome una lista de números como parámetro y un valor
# opcional nota_aprobado, que por defecto es 5.
# La función debe calcular la media de los números en la lista y determinar
# si la media es mayor o igual que nota_aprobado.
# Si es así, el estado será "aprobado", de lo contrario, será "suspenso".
# La función debe devolver una tupla que contenga la media y el estado.
# =========================================

def ejercicio_5(lista_numeros, nota_aprobado=5):
    """lista de números como parámetro y un valor opcional nota_aprobado, que por defecto es 5. La función debe calcular la media de los números en la lista y determinar
    si la media es mayor o igual que nota_aprobado. Si es así, el estado será "aprobado", de lo contrario, será "suspenso".
    La función debe devolver una tupla que contenga la media y el estado.
    Para evitar que se lance un expecion por dividir entre 0, primero me aseguro de que la lista no este vacia

    Args:
        lista_numeros (list): lista de numeros/notas.
        nota_aprobado (int, optional): nota de aprobado, por defecto 5.

    Returns:
        tupla: media de las notas y el estado: aprobado/suspenso.
    """    
    if len(lista_numeros) == 0:
        return "Debes prorporciona runa lista que no esté vacía"
    media = sum(lista_numeros) / len(lista_numeros)
    
    if media >= nota_aprobado:
        estado = "aprobado"
    else:
        estado = "suspenso"

    return (media, estado)

#Comprobacion.
#print(ejercicio_5([10,5,7,3]))
#print(ejercicio_5([5,5,5,4], 4))
#print(ejercicio_5([5,5,5,4]))
#print(ejercicio_5([3,5,5,4]))
#print(ejercicio_5([3,5,5,4]))
#print(ejercicio_5([]))



# =========================================
# Ejercicio 6
# Enunciado:
# Escribe una función que calcule el factorial de un número
# de manera recursiva.
# =========================================

def ejercicio_6(numero):
    """
    Calcular el factorial de un número. Usamos nua func recursiva

    Args:
        numero (int): Número entero del que se quiere calcular el factorial

    Returns:
        int: Factorial del número
    """
    if numero == 0:
        return 1
    return numero * ejercicio_6(numero-1)


#Comprobacion.
#print(ejercicio_6(9))

# =========================================
# Ejercicio 7
# Enunciado:
# Genera una función que convierta una lista de tuplas
# a una lista de strings. Usa la función map()
# =========================================

def ejercicio_7(lista_tuplas):
    """
    Conviertir una lista de tuplas en una lista de strings utilizando la función map().

    Args:
        lista_tuplas (list): Lista de tuplas

    Returns:
        list: Lista de strings generados a partir de las tuplas
    """
    iterador_map= map(str,lista_tuplas)
    lista_strings = list(iterador_map)
    return lista_strings

#Comprobacion.
#print(ejercicio_7([("Juan", 30), ("Ana", 25)]))

# =========================================
# Ejercicio 8
# Enunciado:
# Escribe un programa que pida al usuario dos números e intente dividirlos.
# Si el usuario ingresa un valor no numérico o intenta dividir por cero,
# maneja esas excepciones de manera adecuada.
# Muestra un mensaje indicando si la división fue exitosa o no.
# =========================================

def ejercicio_8():
    """ 
    Funcion que pide dos numeros al usuario e intenta dividirlos lanzando excepciones si los valores no son numericos o el denominador es 0.

    Args:
        NA

    Returns:
        NA / print por pantalla de un mensaje indicando si es exitosa la operacion o no y el resultado.
    """    
    try:
        dividendo = float(input("introduce el dividendo para efectuar la division: "))
        divisor = float(input("introduce el dividor para efectuar la division: "))

        resultado=dividendo/divisor
        print(f"La division fue exitosa. El resultado es: {resultado}")

    except ValueError:
        print("Por favor, introduce solo valores numéricos")

    except ZeroDivisionError:
        print("El divisor no puede ser 0")
    

#Comprobacion.
#ejercicio_8()
     

# =========================================
# Ejercicio 9
# Enunciado:
# Escribe una función que tome una lista de nombres de mascotas
# y devuelva una nueva lista excluyendo ciertas mascotas prohibidas en España.
# La lista de mascotas a excluir es:
# ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]
# Usa la función filter()
# =========================================

def ejercicio_9(lista_mascotas):
    """
    Funcion que filtra una lista de mascotas excluyendo las prohibidas en nuestro país

    Args:
        lista_mascotas (list): Lista de mascotas

    Returns:
        list: Lista de mascotas sin las mastocas que están excluidas
    """
    mascotas_prohibidas = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]
    mascotas_permitidas = list(
        filter(lambda mascota: mascota not in mascotas_prohibidas, lista_mascotas)
    )

    return mascotas_permitidas

#Comprobacion.
#print(ejercicio_9(["Gato", "Tigre", "Perro", "Oso", "Caballo"]))

# =========================================
# Ejercicio 10
# Enunciado:
# Escribe una función que reciba una lista de números y calcule su promedio.
# Si la lista está vacía, lanza una excepción personalizada
# y maneja el error adecuadamente.
# =========================================

def ejercicio_10(lista_numeros):
    """
    Calcula el promedio de una lista de números y lanza una excepcion personalizada si la lista esta vacia

    Args:
        lista_numeros (list): Lista de números

    Returns:
        float: Promedio de la lista de numeros
    """
    try:
       
       if len(lista_numeros)== 0:
           raise ValueError("La lista esta vacia")
       
       result = sum(lista_numeros)/len(lista_numeros)
       return result
    
    except ValueError as error:
        print(f"Error: {error}")


#Comprobacion.
#print(ejercicio_10([1,1,1,1]))
#print(ejercicio_10([]))


# =========================================
# Ejercicio 11
# Enunciado:
# Escribe un programa que pida al usuario que introduzca su edad.
# Si el usuario ingresa un valor no numérico o un valor fuera del rango esperado
# (menor que 0 o mayor que 120), maneja las excepciones adecuadamente.
# =========================================

def ejercicio_11():
    """
    Funcion que solicita la edad al usuario y valida que sea correcta

      Args: 
            NA

    Returns: 
            NA
    """

    try:
       edad = int(input("Introduce tu edad: "))

       if edad < 0:
            print("Error: la edad no puede ser negativa")
       elif edad > 120:
            print("Error: la edad no puede ser mayor que 120")
       else:
            print("Edad introducida correctamente")

    except ValueError:
        print("Error: Debes introducir un numero")


#Comprobacion.
#ejercicio_11()


# =========================================
# Ejercicio 12
# Enunciado:
# Genera una función que al recibir una frase devuelva una lista
# con la longitud de cada palabra.
# Usa la función map()
# =========================================

def ejercicio_12(frase):
    """
    Devuelve una lista con la longitud de cada palabra de una frase.

    Args:
        frase (str): Frase de entrada.

    Returns:
        list: Lista con la longitud de cada palabra.
    """
    palabras = frase.split()
    longitudes = list(map(len, palabras))
    return longitudes
    
#Comprobacion.
#print(ejercicio_12("El coche es rojo"))

# =========================================
# Ejercicio 13
# Enunciado:
# Genera una función que, para un conjunto de caracteres,
# devuelva una lista de tuplas con cada letra en mayúsculas y minúsculas.
# Las letras no pueden estar repetidas.
# Usa la función map()
# =========================================

def ejercicio_13(conjunto_caracteres):
    """
    Funcion que convierte un conjunto de caracteres en una lista de tuplas con cada letra en mayúsculas y minúsculas. 
    Le meto el sorted porque si no no sale en order alfabetico porque el set del conjunto de caracteres no tiene order

    Args:
        conjunto_caracteres (set): Conjunto de caracteres.

    Returns:
        list: Lista de tupla (mayúscula, minúscula).
    """
    resultado = list(
        map(
            lambda letra: (letra.upper(), letra.lower()), conjunto_caracteres
            )
    )
    return sorted(resultado)


#Comprobacion.
#print(ejercicio_13({"a", "b", "c", "b", "b", "d", "d"}))
    
# =========================================
# Ejercicio 14
# Enunciado:
# Crea una función que retorne las palabras de una lista
# que comiencen con una letra específica.
# Usa la función filter()
# =========================================

def ejercicio_14(lista_palabras, letra):
    """
    funcion que devuelve las palabras que comienzan con una letra específica.

    Args:
        lista_palabras(list): Lista de palabras
        letra(str): Letra por la que deben comenzar las palabras

    Returns:
        list: Lista de palabras que comienzan por la letra especificada
    """
    resultado = list(
        filter(lambda palabra: palabra.startswith(letra), lista_palabras)
    )
    return resultado

#Comprobacion.
#print(ejercicio_14(["perro", "gato", "pajaro", "pez", "gallina"], "p"))


# =========================================
# Ejercicio 15
# Enunciado:
# Crea una función lambda que sume 3 a cada número
# de una lista dada.
# =========================================

def ejercicio_15(lista_numeros):
    """
    Funcion que sume 3 a cada número de una lista usando una función lambda

    Args:
        lista_numeros (list): Lista de números.

    Returns:
        list: Nueva lista sumando 3 a cada número de la lista original
    """
    resultado = list(map(lambda numero: numero + 3, lista_numeros))
    return resultado


#Comprobacion.
#print(ejercicio_15([1,2,5,0,3]))


# =========================================
# Ejercicio 16
# Enunciado:
# Escribe una función que tome una cadena de texto
# y un número entero n como parámetros y devuelva
# una lista de todas las palabras que sean más largas que n.
# Usa la función filter().
# =========================================

def ejercicio_16(texto, n):
    """
    Funcion que devuelve las palabras cuya longitud es mayor que n

    Args:
        texto (str): Cadena de texto.
        n (int): Longitud minima de las palabras.

    Returns:
        list: Lista de palabras con longitud mayor que n
    """
    palabras = texto.split()
    resultado = list(filter(lambda palabra: len(palabra) > n, palabras))
    return resultado

# Comprobacion
# print(ejercicio_16("Hay cuatro palabras con longitud mayor a 4", 4))

# =========================================
# Ejercicio 17
# Enunciado:
# Crea una función que tome una lista de dígitos
# y devuelva el número correspondiente.
# Ejemplo: [5,7,2] -> 572
# Usa la función reduce().
# =========================================

from functools import reduce

def ejercicio_17(lista_digitos):
    """
    Funcion que convierte una lista de dígitos n un número entero usando reduce().

    Args:
        lista_digitos (list): Lista de dígitos enteros.

    Returns:
        int: Número formado por los dígitos.
    """
    numero_str = reduce(lambda acc, d: acc + str(d), lista_digitos, "")
    numero = int(numero_str)
    return numero

#Comprobacion
#print(ejercicio_17([5, 7, 2]))

# =========================================
# Ejercicio 18
# Enunciado:
# Crea una lista de diccionarios con información
# de estudiantes (nombre, edad, calificación) y usa
# filter() para extraer los estudiantes con
# calificación mayor o igual a 90.
# =========================================

def ejercicio_18(lista_estudiantes):
    """
    Funcion que filtra estudiantes con calificaciónmayor o igual a 90

    Args:
        lista_estudiantes (list): Lista de diccionarios de estudiantes

    Returns:
        list: Lista de estudiantes con calificación >= 90.
    """
    resultado = list(filter(lambda estudiante: estudiante["calificacion"] >= 90, lista_estudiantes))
    return resultado

# Comprobacion
#estudiantes = [ {"nombre": "Ana", "edad": 20, "calificacion": 95}, {"nombre": "Luis", "edad": 22, "calificacion": 88},{"nombre": "Marta", "edad": 31, "calificacion": 90}]
#print(ejercicio_18(estudiantes))

# =========================================
# Ejercicio 19
# Enunciado:
# Crea una función lambda que filtre los números
# impares de una lista dada.
# =========================================

def ejercicio_19(lista_numeros):
    """
    Funcion que devuelve los números impares de una lista 

    Args:
        lista_numeros (list): Lista de números

    Returns:
        list: Lista con los números impares.
    """
    resultado = reduce(lambda nueva_lista, num_lista: nueva_lista + [num_lista] if num_lista % 2 != 0 else nueva_lista, lista_numeros, [])
    return resultado

# Comprobacion
#print(ejercicio_19([1, 2, 3, 4, 5, 6, 7]))

# =========================================
# Ejercicio 20
# Enunciado:
# Para una lista con elementos tipo integer y string,
# obtén una nueva lista sólo con los valores int.
# Usa la función filter().
# =========================================

def ejercicio_20(lista_elementos):
    """
    Funcion que filtra únicamente los valores int de una lista usando filter()

    Args:
        lista_elementos (list): Lista con enteros/strings

    Returns:
        list: Lista con solo valores int
    """
    resultado = list(filter(lambda elemento: type(elemento) == int, lista_elementos))
    return resultado

# Comprobacion
#print(ejercicio_20([1, "2", 3, "hola", 4]))

# =========================================
# Ejercicio 21
# Enunciado:
# Crea una función que calcule el cubo de un número
# dado mediante una función lambda.
# =========================================

def ejercicio_21(numero):
    """
    Funcion que calcula el cubo de un número
    usando una función lambda.

    Args:
        numero (int or float): Número a elevar al cubo.

    Returns:
        int or float: Cubo del número.
    """
    return (lambda numero: numero * numero * numero)(numero)

# Comprobacion
#print(ejercicio_21(4))

# =========================================
# Ejercicio 22
# Enunciado:
# Dada una lista numérica, obtén el producto total
# de los valores de dicha lista.
# Usa la función reduce().
# =========================================


def ejercicio_22(lista_numeros):
    """
    Funcion que calcula el producto total de una lista

    Args:
        lista_numeros (list): Lista de números

    Returns:
        int or float: Producto total.
    """
    resultado = reduce(lambda acumulador, numero: acumulador * numero, lista_numeros)
    return resultado

# Comprobacion
#print(ejercicio_22([2, 3, 4]))

# =========================================
# Ejercicio 23
# Enunciado:
# Concatena una lista de palabras
# Usa la función reduce().
# =========================================


def ejercicio_23(lista_palabras):
    """
    Funcion que concatena una lista de palabras en una sola cadena

    Args:
        lista_palabras (list): Lista de strings

    Returns:
        str: Cadena concatenada
    """
    resultado = reduce(lambda acumulador, palabra: acumulador + palabra, lista_palabras)
    return resultado

# Comprobacion
#print(ejercicio_23(["Esta", " ", "es", " ", "la", " ", "lista", " ", "conctenada."]))

# =========================================
# Ejercicio 24
# Enunciado:
# Calcula la diferencia total en los valores de una lista.
# Usa la función reduce().
# =========================================


def ejercicio_24(lista_numeros):
    """
    Funcion que calcula la diferencia total  de los valores de una lista

    Args:
        lista_numeros (list): Lista de números.

    Returns:
        int or float: Resultado de la diferencia acumulada.
    """
    resultado = reduce(lambda acumulador, numero: acumulador - numero, lista_numeros)
    return resultado

# Comprobacion
#print(ejercicio_24([20, 3, 2, 5]))

# =========================================
# Ejercicio 25
# Enunciado:
# Crea una función que cuente el número de caracteres
# en una cadena de texto dada.
# =========================================

def ejercicio_25(texto):
    """
    Funcion que cuenta el número de caracteres de una cadena de texto

    Args:
        texto (str): Cadena de texto

    Returns:
        int: Número de caracteres de la cadena
    """
    return len(texto)

# Comprobacion
#print(ejercicio_25("Buenos días"))

# =========================================
# Ejercicio 26
# Enunciado:
# Crea una función lambda que calcule el resto
# de la división entre dos números dados.
# =========================================

def ejercicio_26(a, b):
    """
    Funcion que calcula el resto de la división entre dos números.

    Args:
        a (int): Dividendo
        b (int): Divisor

    Returns:
        int: Resto de la división
    """
    return (lambda x, y: x % y)(a,b)

# Comprobacion
# print(ejercicio_26(4, 2))

# =========================================
# Ejercicio 27
# Enunciado:
# Crea una función que calcule el promedio
# de una lista de números.
# =========================================

def ejercicio_27(lista_numeros):
    """
    Funcion que calcula el promedio de una lista de números

    Args:
        lista_numeros (list): Lista de números

    Returns:
        float: Promedio
    """
    promedio = sum(lista_numeros) / len(lista_numeros)
    return promedio

# Comprobacion
#print(ejercicio_27([2, 5, 5, 8]))

# =========================================
# Ejercicio 28
# Enunciado:
# Crea una función que busque y devuelva
# el primer elemento duplicado en una lista dada.
# =========================================

def ejercicio_28(lista):
    """
    Funcion que devuelve el primer elemento duplicadode una lista

    Args:
        lista (list): Lista de elementos

    Returns:
        any: Primer elemento duplicado
    """
    vistos = []
    for elemento in lista:
        if elemento in vistos:
            return elemento
        vistos.append(elemento)
    return None

# Comprobacion
#print(ejercicio_28([1, 3, 5, 3, 7, 1]))
#print(ejercicio_28([1, 3, 5, 4, 7, 0]))


# =========================================
# Ejercicio 29
# Enunciado:
# Crea una función que convierta una variable
# en una cadena de texto y enmascare todos los
# caracteres con '#', excepto los últimos cuatro.
# =========================================

def ejercicio_29(valor):
    """
    Funcion que convierte un valor en texto y enmascara todos los caracteres excepto los últimos cuatro con #

    Args:
        valor (any): Variable a convertir y enmascarar

    Returns:
        str: Cadena enmascarada
    """
    texto = str(valor)
    resultado = ""
    longitud = len(texto)

    for i in range(longitud):
        if i < longitud - 4:
            resultado = resultado + "#"
        else:
            resultado = resultado + texto[i]

    return resultado

# Comprobacion
#print(ejercicio_29(123456789))
#print(ejercicio_29("ABCDEFGHIJ"))

# =========================================
# Ejercicio 30
# Enunciado:
# Crea una función que determine si dos palabras
# son anagramas, es decir, si están formadas por
# las mismas letras pero en diferente orden.
# =========================================

def ejercicio_30(palabra1, palabra2):
    """
    Funcion que determina si dos palabras son anagramas

    Args:
        palabra1 (str): Primera palabra
        palabra2 (str): Segunda palabra

    Returns:
        bool: True si son anagramas, False si no son anagramas.
    """
    return sorted(palabra1) == sorted(palabra2)

# Comprobacion
#print(ejercicio_30("hola", "halo"))
#print(ejercicio_30("hola", "adios"))

 #=========================================
# Ejercicio 31
# Enunciado:
# Crea una función que solicite al usuario ingresar
# una lista de nombres y luego solicite un nombre
# para buscar en esa lista. Si el nombre está en la
# lista, se imprime un mensaje indicando que fue
# encontrado, de lo contrario, se lanza una excepción.
# =========================================

def ejercicio_31():
    """
    Funcion que pide una lista de nombres y un nombre para byuscar y si no lo encuentra lanza una excepción.

     Args:
   
    Returns:
    """
    
    nombres = []

    while True:
        nombre = input("Introduce un nombre (o 'stop' sin comillas para terminar): ")
        if nombre == "stop":
            break

        nombres.append(nombre)

    nombre_buscar = input("Introduce el nombre a buscar: ")

    if nombre_buscar in nombres:
        print("El nombre está en la lista")
    else:
        raise Exception("El nombre no está en la lista.")


# Comprobacion
#ejercicio_31()

# =========================================
# Ejercicio 32
# Enunciado:
# Crea una función que tome un nombre completo y
# una lista de empleados, busque el nombre completo
# en la lista y devuelva el puesto del empleado si
# está en la lista. De lo contrario, devuelve un
# mensaje indicando que la persona no trabaja aquí.
# =========================================

def ejercicio_32(nombre, empleados):
    """
    Funcion que busca un empleado por su nombre y devuelve su puesto.

    Args:
        nombre (str): Nombre completo del empleado.
        empleados (list): Lista de diccionario con empleados.

    Returns:
        str: Puesto del empleado o mensaje indicando que no trabaja aquí.
    """
    for empleado in empleados:
        if empleado["nombre"] == nombre:
            return empleado["puesto"]
    return "La persona no trabaja aquí."

# Comprobacion
#empleados = [
#     {"nombre": "Juan Perez", "puesto": "Administrador"},
#     {"nombre": "Ana Lopez", "puesto": "Analista"},
#     {"nombre": "Luis Gomez", "puesto": "Desarrollador"}
#]
#print(ejercicio_32("Ana Lopez", empleados))
#print(ejercicio_32("Luis Perez", empleados))

# =========================================
# Ejercicio 33
# Enunciado:
# Crea una función lambda que sume elementos
# correspondientes de dos listas dadas.
# =========================================

def ejercicio_33(lista1, lista2):
    """
    Funcion que suma los elementos correspndientes de dos listas

    Args:
        lista1 (list): Primera lista de números
        lista2 (list): Segunda lista de números

    Returns:
        list: Lista con la suma de los elementos correspondientes
    """
    return list(map(lambda x, y: x + y, lista1, lista2))

# Comprobacion
#print(ejercicio_33([1, 2, 3], [4, 5, 6]))



# =========================================
# Ejercicio 34
# Enunciado:
# Crea la clase Arbol. Define un árbol genérico con un tronco y ramas como atributos.
# Los métodos disponibles son:
# - crecer_tronco: aumenta la longitud del tronco en una unidad.
# - nueva_rama: agrega una nueva rama de longitud 1 a la lista de ramas.
# - crecer_ramas: aumenta en una unidad la longitud de todas las ramas existentes.
# - quitar_rama: elimina una rama en una posición específica.
# - info_arbol: devuelve información sobre la longitud del tronco, el número de ramas y las longitudes de las ramas.
#
# Código a seguir:
# 1. Inicializar un árbol con un tronco de longitud 1 y una lista vacía de ramas.
# 2. Implementar crecer_tronco.
# 3. Implementar nueva_rama.
# 4. Implementar crecer_ramas.
# 5. Implementar quitar_rama.
# 6. Implementar info_arbol.
#
# Caso de uso:
# 1. Crear un árbol.
# 2. Hacer crecer el tronco una unidad.
# 3. Añadir una nueva rama.
# 4. Hacer crecer todas las ramas una unidad.
# 5. Añadir dos nuevas ramas.
# 6. Retirar la rama situada en la posición 2.
# 7. Obtener información sobre el árbol.
# =========================================


class Arbol:
    """
    Clase que representa a un árbol con  tronco y ramas.
    """

    def __init__(self):
        """
        Inicializa un arbol con tronco de longitud 1 y sin ramas
        """
        self.tronco = 1
        self.ramas = []

    def crecer_tronco(self):
        """
        Aumenta la longitud del tronco en uno
        """
        self.tronco += 1

    def nueva_rama(self):
        """
        Agrega una nueva rama de longitud 1 a la lista de ramas.
        """
        self.ramas.append(1)

    def crecer_ramas(self):
        """
        Aumenta en una unidad la longitud de todas las ramas
        """
        self.ramas = list(map(lambda r: r + 1, self.ramas))

    def quitar_rama(self, posicion):
        """
        Elimina una rama en una posición en concreto

        Args:
            posicion (int): Posición de la rama a eliminar

        Returns:
            bool: True si se eliminó, False si la posición no es valida
        """
        indice = posicion - 1  # ya que empieza en 0 y no en 1 como en nuestro orden logico
        if 0 <= indice < len(self.ramas):
            self.ramas.pop(indice)
            return True
        return False

    def info_arbol(self):
        """
        Devuelve la info del árbol: longitud del tronco, número de ramas y longitud de estas.

        Returns:
            dict: Diccionario con la información del árbol
        """
        return {
            "longitud_tronco": self.tronco,
            "numero_ramas": len(self.ramas),
            "longitudes_ramas": self.ramas
        }


# Comprobacion
#  arbol = Arbol()                 # 1. Crear un árbol
# arbol.crecer_tronco()           # 2. Crecer tronco
# arbol.nueva_rama()              # 3. Añadir 1 rama
# arbol.crecer_ramas()            # 4. Crecer todas las ramas
# arbol.nueva_rama()              # 5. Añadir 2 ramas nuevas (primera)
# arbol.nueva_rama()              # 5. Añadir 2 ramas nuevas (segunda)
# arbol.quitar_rama(2)            # 6. Quitar rama en posición 2
# print(arbol.info_arbol())       # 7. Info del árbol



# =========================================
# Ejercicio 36
# Enunciado:
# Crea la clase UsuarioBanco, que represente a un
# usuario de un banco con su nombre, saldo y si
# tiene o no cuenta corriente.
#
# La clase debe proporcionar métodos para realizar
# operaciones bancarias básicas:
# - retirar_dinero: retira una cantidad del saldo
#   del usuario y lanza una excepción si no es posible.
# - transferir_dinero: realiza una transferencia
#   desde otro usuario al usuario actual y lanza
#   una excepción si no es posible.
# - agregar_dinero: agrega una cantidad al saldo
#   del usuario.
#
# Código a seguir:
# 1. Inicializar un usuario con su nombre, saldo y
#    si tiene o no cuenta corriente (True / False).
# 2. Implementar el método retirar_dinero.
# 3. Implementar el método transferir_dinero.
# 4. Implementar el método agregar_dinero.



class UsuarioBanco:

    def __init__(self, nombre, saldo, cuenta_corriente):
        """
        Inicializa un usuario con su nombre, saldo y si tiene o no cuenta corriente
        """
        self.nombre = nombre
        self.saldo = saldo
        self.cuenta_corriente = cuenta_corriente

    def retirar_dinero(self, cantidad):
        """
        Retirar una cantidad de dinero
        """
        if not self.cuenta_corriente:
            raise Exception("El usuario no tiene cuenta corriente")

        if cantidad > self.saldo:
            raise Exception("Saldo insuficiente")

        self.saldo -= cantidad
    
    def transferir_dinero(self, otro_usuario, cantidad):
        """
        Transferir una cantidad de dinero a otro usuario
        """
        if not self.cuenta_corriente or not otro_usuario.cuenta_corriente:
            raise Exception("Ambos usuarios deben tener cuenta corriente")

        if self.saldo < cantidad:
            raise Exception("Saldo insuficiente para la transferencia")

        otro_usuario.saldo = otro_usuario.saldo + cantidad
        self.saldo -= cantidad
        
    def agregar_dinero(self, cantidad):
        """
       Agregar una cantidad de dinero al saldo
        """
        self.saldo = self.saldo + cantidad

        

# Comprobacion
# alicia = UsuarioBanco("Alicia",100,True)
# bob = UsuarioBanco("Bob",50,True)
# print(alicia.saldo)
# print(bob.saldo)
# bob.agregar_dinero(20)
# print(alicia.saldo)
# print(bob.saldo)
# alicia.transferir_dinero(bob,80)
# print(alicia.saldo)
# print(bob.saldo)
# alicia.retirar_dinero(50)
# print(alicia.saldo)
# print(bob.saldo)




# =========================================
# Ejercicio 37
# Enunciado:
# Crea una función llamada procesar_texto que procesa un texto según la opción especificada:
# contar_palabras, reemplazar_palabras, eliminar_palabra.
# Estas opciones son otras funciones que tenemos que definir primero y llamar dentro de la función procesar_texto.
#
# Código a seguir:
# 1. Crear una función contar_palabras para contar el número de veces que aparece cada palabra en el texto.
#    Debe devolver un diccionario.
# 2. Crear una función reemplazar_palabras para reemplazar una palabra_original del texto por una palabra_nueva.
#    Debe devolver el texto con el reemplazo de palabras.
# 3. Crear una función eliminar_palabra para eliminar una palabra del texto.
#    Debe devolver el texto con la palabra eliminada.
# 4. Crear la función procesar_texto que tome un texto, una opción (entre "contar", "reemplazar", "eliminar")
#    y un número de argumentos variable según la opción indicada.
#
# Caso de uso:
# Comprueba el funcionamiento completo de la función procesar_texto.
# =========================================

def contar_palabras(texto):
    """
    Cuenta cuántas veces aparece cada palabra

    Args:
        texto (str): Texto en el que contar el numero de apariciones de la palabra

    Returns:
        dict: Diccionario con las palabras como claves y sus conteos como valores.
    """
    palabras = texto.split()
    conteo = {}
    for palabra in palabras:
        if palabra in conteo.keys():
            conteo[palabra] += 1
        else:
            conteo.update({palabra:1})
    return conteo

#texto = "hola mundo hola python mundo hola"
#resultado = contar_palabras(texto)

#print("Texto:", texto)
#print("Resultado del conteo:")
#print(resultado)

def reemplazar_palabras(texto, palabra_original, palabra_nueva):
    """
    Reemplaza una palabra del texto por otra

    Args:
        texto (str): Texto inicial
        palabra_original (str): Palabra a reemplazar
        palabra_nueva (str): Palabra que sustituye a la original.

    Returns:
        str: Texto finalcon la palabra reemplazada
    """
    return texto.replace(palabra_original, palabra_nueva)

#print(reemplazar_palabras(texto, "hola", "adios"))


def eliminar_palabra(texto, palabra):
    """
    Elimina una palabra del texto

    Args:
        texto (str): Texto inicial
        palabra (str): Palabra a eliminar

    Returns:
        str: Texto final con la palabra eliminada
    """
    palabras = texto.split()
    resultado = []
    for p in palabras:
        if p != palabra:
            resultado.append(p)

    return " ".join(resultado)
    
#print(eliminar_palabra("hola mundo hola python", "hola"))


def procesar_texto(texto, opcion, *args):
    """
    Procesa un texto según la opción indicada: contar, reemplazar o eliminar

    Args:
        texto (str): Texto
        opcion (str): Opción de procesamiento: contar, reemplazar o eliminar
        *args: Argumentos variables según la opción:
            "contar": no necesita argumentos adicionales
            "reemplazar": palabra_original, palabra_nueva
            "eliminar": palabra

    Returns:
        dict or str: Diccionario si opcion es contar o texto modificado si opcion reemplazar o eliminar
    """
    if opcion == "contar":
        return contar_palabras(texto)

    elif opcion == "reemplazar":
        if len(args) != 2:
            raise Exception("La opción reemplazar requiere dos argumentos")
        return reemplazar_palabras(texto, args[0], args[1])

    elif opcion == "eliminar":
        if len(args) != 1:
            raise Exception("La opción eliminar requiere un argumento")
        return eliminar_palabra(texto, args[0])

    else:
        raise Exception("Opción no valida")

texto = "hola mundo hola python"


# texto = "hola mundo hola mundo hola hola"
# print(procesar_texto(texto, "contar"))
# print(procesar_texto(texto, "reemplazar", "hola", "adios"))
# print(procesar_texto(texto, "eliminar", "hola"))


# =========================================
# Ejercicio 38
# Enunciado:
# Genera un programa que nos diga si es de noche, de día o tarde según la hora proporcionada por el usuario.
# =========================================

def ejercicio_38():
    """
    Solicita al usuario una hora y determina en que momento del dia estamos: de día, tarde o noche. Determinaremos que es de día si la hora se encuentra entre
    las 08 y las 14, de tarde si estamos entre la 15 y las 20 (ambos inclusive), y de noche si son de las 21 en adelante.

    Args:
        None

    Returns:
        str: Mensaje indicando si es de noche, de día o tarde.
    """
    hora = int(input("Introduce la hora (0-23): "))

    if hora < 0 or hora > 23:
        raise Exception("Hora no valida. Debe estar entre 0 y 23")

    # Noche: 0-8 y 21-23
    if hora <= 8 or hora >= 21:
        return "Es de noche"
    # Día: 8-15
    elif 8 <= hora < 15:
        return "Es de día"
    # Tarde: 15-20
    else:
        return "Es de tarde"


# Comprobacion
#print(ejercicio_38())
    



# =========================================
# Ejercicio 39
# Enunciado:
# Escribe un programa que determine qué calificación en texto tiene un alumno en base a su calificación numérica.
# Reglas:
# - 0 - 69: insuficiente
# - 70 - 79: bien
# - 80 - 89: muy bien
# - 90 - 100: excelente
# =========================================

def ejercicio_39():
    """
    Solicita al usuario una calificación numérica y devuelve su equivalente en texto.

    Args:
        None

    Returns:
        str: Calificación en texto según la nota numérica.
    """
    nota = int(input("Introduce la calificación (0-100): "))
    if nota < 0 or nota > 100:
     raise Exception("La calificación debe estar entre 0 y 100.")
    if nota <= 69:
        return "insuficiente"
    elif nota <= 79:
        return "bien"
    elif nota <= 89:
        return "muy bien"
    else:
        return "excelente"


# Comprobacion
#print(ejercicio_39())




# =========================================
# Ejercicio 40
# Enunciado:
# Escribe una función que tome dos parámetros:
# - figura: una cadena que puede ser "rectangulo", "circulo" o "triangulo"
# - datos: una tupla con los datos necesarios para calcular el área de la figura
# =========================================

def ejercicio_40(figura, datos):
    """
    Calcula el área de una figura geométrica según el tipo de forma

    Args:
        figura (str): Tipo de figura: "rectangulo", "circulo" o "triangulo"
        datos (tuple): Datos necesarios para calcular el área
            - "rectangulo": base, altura
            - "circulo": radio
            - "triangulo": base, altura

    Returns:
        float: Área calculada de la figura.
    """
    if figura == "rectangulo":
        base = datos[0]
        altura = datos[1]
        return base * altura

    elif figura == "triangulo":
        base = datos[0]
        altura = datos[1]
        return (base * altura) / 2

    elif figura == "circulo":
        radio = datos[0]
        return 3.1416 * (radio ** 2)

    else:
        raise Exception("Figura no contemplada. Debe ser 'rectangulo', 'circulo' o 'triangulo'.")


# Comprobacion
# print(ejercicio_40("rectangulo", (5, 3)))
# print(ejercicio_40("triangulo", (5, 3)))  
# print(ejercicio_40("circulo", (2,)))       


# =========================================
# Ejercicio 41
# Enunciado:
# Programa que determine el monto final de una compra tras aplicar un descuento:
# 1. Solicita el precio original del artículo.
# 2. Pregunta si tiene un cupón de descuento (sí/no).
# 3. Si responde que sí, solicita el valor del cupón.
# 4. Aplica el descuento si el cupón es válido (mayor que cero).
# 5. Muestra el precio final con descuento o sin él.
# 6. Usa if, elif y else.
# =========================================

def ejercicio_41():
    """
    Funcion que solicita datos de una compra al usuario y calcula el precio final aplicando un cupón descuento

    Args:
        None

    Returns:
        float: Precio final de la compra.
    """
    precio_original = float(input("Introduce el precio del artículo: "))

    if precio_original <= 0:
        raise Exception("El precio debe ser mayor que cero")

    tiene_cupon = input("¿Tiene un cupón de descuento? Responda (si/no): ").lower()

    if tiene_cupon == "si":
        descuento = float(input("Introduce el valor del cupón: "))

    if descuento <= 0:
            raise Exception("El valor del descuento debe ser mayor que cero")
    
    precio_final = precio_original - descuento

    if precio_final < 0:
        precio_final = 0

    else:
        precio_final = precio_original

    return precio_final


# Comprobacion
#print("Precio final:", ejercicio_41())