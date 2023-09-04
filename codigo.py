from math import log2

print("\n Solución a la tarea número 1 \n de Teoría de la Información \n")

#Funcion que recibe un archivo de texto y retorna una cadena
def leer_archivo():
    with open('ejemplo1.txt', 'r', encoding='utf-8') as archivo:
        contenido = archivo.read()
    return contenido

#Funcion para calcular el numero de caracteres que hay en el texto
def contar_caracteres():
    texto = leer_archivo()  # Utilizar el nombre de la función de lectura
    return len(texto)

#Funcion que recibe un diccionario organiza sus claves según sus valores en orden descendente e imprime las claves y sus valores correspondientes en ese orden.
def ordenar_diccionario(diccionario):
    claves = list(diccionario.keys())
    claves.sort(key=lambda x: diccionario[x], reverse=True)
    for clave in claves:
        valor = diccionario[clave]
        mensaje = f"La clave {clave} tiene un valor de {valor}"
        print(mensaje)
    return "\n"

#Funcion que retorna un diccionario donde las claves son simbolos individuales del texto y los valores son las frecuencia de aparicion
def contar_caracteres_individuales():
    "Retorna un diccionario donde las keys son el símbolo y Value es su frecuencia de aparición"
    texto = leer_archivo()  # Utilizar el nombre de la función de lectura
    diccionario = {}
    for caracter in texto:
        if caracter not in diccionario:
            diccionario[caracter] = 1
        else:
            num = diccionario[caracter]
            diccionario[caracter] = num + 1
    return diccionario

#Funcion que devuelve un diccionario en donde las claves son pares de simbolos consecutivos y su valor es el numero total de veces que cada par aparece 
def contar_repeticion_pares_fuente_extendida():
    "Retorna un diccionario de fuente extendida, dónde keys es el par y values el número total de pares"
    texto = leer_archivo()  # Utilizar el nombre de la función de lectura
    diccionario = {}
    cadena = ""
    num = 0
    for caracter in texto:
        cadena += caracter
        num += 1
        if num == 2:
            if cadena not in diccionario:
                diccionario[cadena] = 1
            else:
                numero_pares = diccionario[cadena]
                diccionario[cadena] = numero_pares + 1
            num = 0
            cadena = ""
    return diccionario

#Funcion que hace un conteo de los pares repetidos y retorna un diccionario con cada uno de ellos(claves) y el numero de veces que aparece(valor).
def contar_repeticion_pares():
    "Retorna un diccionario donde: keys son pares de símbolos y Value es su frecuencia de aparición"
    texto = leer_archivo()  # Utilizar el nombre de la función de lectura
    diccionario = {}
    cadena = ""
    num = 0
    for caracter in texto:
        cadena += caracter
        if num == 1:
            if cadena not in diccionario:
                diccionario[cadena] = 1
            else:
                numero_pares = diccionario[cadena]
                diccionario[cadena] = numero_pares + 1
            num = 0
            cadena = caracter
        num += 1
    return diccionario

# ) Funcion que calcula la entropía de una secuencia dada suponiendo que los símbolos del texto son igualmente probables
def calcular_entropia_secuencia():
    "Retorna la entropia de la secuencia"
    frecuencia_caracteres = contar_caracteres_individuales()
    numero_simbolos_dif = len(frecuencia_caracteres.keys())
    probabilidad_ocurrencia = 1 / numero_simbolos_dif
    entropia = log2(1 / probabilidad_ocurrencia)
    print("Número de caracteres diferentes : ", numero_simbolos_dif)
    print("Número total de caracteres : ", contar_caracteres())
    print("La información total del texto si los símbolos fueran igualmente probables: ", entropia * contar_caracteres())
    return entropia

# Funcion que encuentra los símbolos que se repiten un número específico de veces en un texto.
def encontrar_simbolos_con_repeticion(numero, diccionario):
    lista = []
    for clave, valor in diccionario.items():
        if valor == numero:
            lista.append(clave)
    return lista

# función imprime la mayor probabilidad de ocurrencia, el símbolo o pares de símbolos correspondientes a esa probabilidad y cuántas veces se repiten. 
def calcular_entropia_puntos_2_y_3(tipo_de_diccionario, divisor):
    lista = []
    prob_ocurrencia_mayor = 0
    valor_maximo = 0
    entropia = 0
    informacion = 0

    for valor in tipo_de_diccionario.values():
        probabilidad_ocurrencia_por_simbolo = valor / divisor
        informacion = log2(1 / probabilidad_ocurrencia_por_simbolo)
        entropia = entropia + informacion * probabilidad_ocurrencia_por_simbolo
        if prob_ocurrencia_mayor < probabilidad_ocurrencia_por_simbolo:
            prob_ocurrencia_mayor = probabilidad_ocurrencia_por_simbolo
            valor_maximo = valor

    print("La mayor probabilidad de el/los símbolo/s de mayor ocurrencia es/son: ", prob_ocurrencia_mayor)
    print("Esta probabilidad pertenece al símbolo: ", encontrar_simbolos_con_repeticion(valor_maximo, tipo_de_diccionario))
    print("De un símbolo que se repite: ", valor_maximo, "veces")
    return entropia

# funcion que calcula la entropía , incluyendo la información total y el orden de ocurrencia de caracteres individuales en el texto. Luego, devuelve la entropía calculada.
def calcular_entropia_punto_2():
    print("Segundo punto: \n")
    entropia_del_punto_dos = calcular_entropia_puntos_2_y_3(contar_caracteres_individuales(), contar_caracteres())
    print("La información total : ", entropia_del_punto_dos * contar_caracteres())
    print("El orden de ocurrencia es: ", ordenar_diccionario(contar_caracteres_individuales()))
    return entropia_del_punto_dos

#  función calcula la entropía  Analizando la probabilidad de ocurrencia por pares de caracteres
def calcular_entropia_punto_3():
    print("Tercer punto: \n")
    frecuencia_pares = contar_repeticion_pares_fuente_extendida()
    numero_de_pares = sum(frecuencia_pares.values())
    print("El número de pares distintos: ", numero_de_pares)
    entropia_del_punto_tres = calcular_entropia_puntos_2_y_3(frecuencia_pares, numero_de_pares)
    print("La información total : ", entropia_del_punto_tres * numero_de_pares)
    return entropia_del_punto_tres

# función calcula la entropía Suponiendo que hay dependencia de primer orden
def calcular_entropia_punto_4():
    """Las entropías de los estados ponderadas por la probabilidad de ocurrencia de los estados."""
    print("\n", "Cuarto punto: \n")
    texto = leer_archivo()
    longitud = len(texto)
    estados = contar_caracteres_individuales()
    pares = contar_repeticion_pares()
    prob_condicional = {}
    for clave_pares in pares.keys():
        for sub_clave_estados in estados.keys():
            if clave_pares[:len(sub_clave_estados)] == sub_clave_estados:
                prob_condicional[clave_pares] = pares[clave_pares] / estados[sub_clave_estados]

    entropy_dict = {}
    for clave_prob_condicional, valor_prob_condicional in prob_condicional.items():
        entropy = valor_prob_condicional * log2(1 / valor_prob_condicional)
        entropy_dict[clave_prob_condicional] = entropy

    entropia_estados = {}
    for clave_entropy_dict in entropy_dict:
        prefijo = clave_entropy_dict[:-1]
        valor = entropy_dict[clave_entropy_dict]
        if prefijo in entropia_estados:
            entropia_estados[prefijo] += valor
        else:
            entropia_estados[prefijo] = valor

    for clave_estados in estados:
        estados[clave_estados] /= longitud

    entropias_ponderadas = {}
    for clave_entropia_estados in entropia_estados:
        entropias_ponderadas[clave_entropia_estados] = entropia_estados[clave_entropia_estados] * estados[clave_entropia_estados]

    suma_entropias_ponderadas = sum(entropias_ponderadas.values())

    print("La entropía del cuarto punto es:", suma_entropias_ponderadas, "\n")
    print("La información total en este caso sería:", suma_entropias_ponderadas * contar_caracteres(), "\n")
    return "------------------------------------------------"


def calcular_entropia_punto_5():
    print("Quinto punto (Dependencia de segundo orden):\n")
    texto = leer_archivo()
    longitud = len(texto)
    pares = contar_repeticion_pares_fuente_extendida()

    # Crear un diccionario para almacenar las probabilidades condicionales de segundo orden
    prob_condicional_2do_orden = {}

    # Calcular las probabilidades condicionales de segundo orden
    for clave_pares in pares.keys():
        for sub_clave_pares in pares.keys():
            if clave_pares[:len(sub_clave_pares)] == sub_clave_pares:
                prob_condicional_2do_orden[clave_pares] = pares[clave_pares] / pares[sub_clave_pares]

    # Calcular las entropías de los estados de segundo orden ponderadas por sus probabilidades
    entropia_estados_2do_orden = {}
    for clave_prob_condicional, valor_prob_condicional in prob_condicional_2do_orden.items():
        entropy = valor_prob_condicional * log2(1 / valor_prob_condicional)
        entropia_estados_2do_orden[clave_prob_condicional] = entropy

    # Sumar las entropías ponderadas para obtener la entropía total
    suma_entropias_ponderadas_2do_orden = sum(entropia_estados_2do_orden.values())

    print("La entropía del quinto punto (Dependencia de segundo orden) es:", suma_entropias_ponderadas_2do_orden, "\n")
    print("La información total en este caso sería:", suma_entropias_ponderadas_2do_orden * longitud, "\n")






print("------------------------------------------------")
print("La entropía del primer punto es:", "\n", calcular_entropia_secuencia(), "\n")
print("La entropía del segundo punto es: ", "\n", calcular_entropia_punto_2(), "\n")
print("La entropía del tercer punto es:", "\n", calcular_entropia_punto_3(), "\n")
print(calcular_entropia_punto_4())

print("La entropía del quinto punto es:", "\n",calcular_entropia_punto_5(), "\n")



print ("todo fin")


