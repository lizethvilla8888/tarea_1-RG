from math import log2

# Función que recibe un archivo de texto y retorna una cadena
print("Solución a la 1ra Tarea\nTeoría de la Información")
def leer_archivo():
    with open('capitulo.txt', 'r', encoding='utf-8') as f:
        texto = f.read()
    return texto

# Función para calcular el número de caracteres que hay en el texto
def num_caracteres():
    texto = leer_archivo()
    return len(texto)

# Función que recibe un diccionario, organiza sus claves según sus valores en orden descendente e imprime las claves y sus valores correspondientes en ese orden.
def ordenar(diccionario):
    claves = list(diccionario.keys()) 
    claves.sort(key=lambda c: diccionario[c], reverse=True)
    for clave in claves:
        valor = diccionario[clave]
        mensaje = f"La clave {clave} tiene un valor de {valor}"
        print(mensaje)
    return "\n"

# Función que retorna un diccionario donde las claves son símbolos individuales del texto y los valores son las frecuencias de aparición
def num_caracteres_individuales():
    texto = leer_archivo()
    diccionario = {}
    for caracter in texto:
        if caracter not in diccionario:
            diccionario[caracter] = 1
        else:
            num = diccionario[caracter]
            diccionario[caracter] = num + 1
    return diccionario

# Función que devuelve un diccionario en donde las claves son pares de símbolos consecutivos y su valor es el número total de veces que cada par aparece
def pares_repetidos():
    texto = leer_archivo()
    cadena = ""
    n = 0
    diccionario = {}
    for caracter in texto:
        cadena += caracter
        if n == 1:
            if cadena not in diccionario:
                diccionario[cadena] = 1
            else:
                npares = diccionario[cadena]
                diccionario[cadena] = npares + 1
            n = 0
            cadena = caracter
        n += 1
    return diccionario


from math import log2

def calcular_entropia_secuencia():
    # Calcular la entropía de la secuencia de caracteres en el archivo.
    frecuencia_caracteres = obtener_frecuencia_caracteres()
    numero_simbolos_diferentes = len(frecuencia_caracteres.keys())
    probabilidad_ocurrencia = 1 / numero_simbolos_diferentes
    entropia = log2(1 / probabilidad_ocurrencia)
    
    # Imprimir información sobre la secuencia.
    print("Número de caracteres diferentes en la secuencia: ", numero_simbolos_diferentes) 
    print("Número total de caracteres en la secuencia: ", obtener_numero_total_caracteres())
    print("La información total si los símbolos fueran igualmente probables: ", entropia * obtener_numero_total_caracteres())
    
    return entropia

def obtener_simbolos_repetidos(numero, diccionario):
    # Esta función devuelve una lista de símbolos que tienen la misma frecuencia que el número proporcionado.
    lista_simbolos = []
    for simbolo, frecuencia in diccionario.items():
        if frecuencia == numero:
            lista_simbolos.append(simbolo)
    return lista_simbolos

def calcular_entropia_secuencia_extendida(tipo_de_diccionario, divisor):
    # Esta función calcula la entropía de una secuencia extendida o pares de símbolos.
    probabilidad_maxima = 0
    valor_maximo = 0
    entropia = 0
    informacion = 0
    
    for frecuencia in tipo_de_diccionario.values():
        probabilidad_ocurrencia_por_simbolo = frecuencia / divisor
        informacion = log2(1 / probabilidad_ocurrencia_por_simbolo)
        entropia += informacion * probabilidad_ocurrencia_por_simbolo
        
        if probabilidad_maxima < probabilidad_ocurrencia_por_simbolo:
            probabilidad_maxima = probabilidad_ocurrencia_por_simbolo
            valor_maximo = frecuencia

    print("La mayor probabilidad de los símbolos de mayor ocurrencia es/son: ", probabilidad_maxima)
    print("Estos símbolos son: ", obtener_simbolos_repetidos(valor_maximo, tipo_de_diccionario))
    print("Cada símbolo se repite: ", valor_maximo, "veces")
    
    return entropia

def calcular_entropia_segundo_punto():
    print("Segundo punto: \n")
    entropia_del_punto_dos = calcular_entropia_secuencia_extendida(obtener_frecuencia_caracteres(), obtener_numero_total_caracteres())
    print("La información total : ", entropia_del_punto_dos * obtener_numero_total_caracteres())
    print("El orden de ocurrencia es: ", ordenar_frecuencia_caracteres(obtener_frecuencia_caracteres()))
    return entropia_del_punto_dos

def calcular_entropia_tercer_punto():
    print("Tercer punto: \n")
    frecuencia_pares = obtener_frecuencia_pares_fuente_extendida()
    numero_de_pares = sum(frecuencia_pares.values())
    print("El número de pares distintos: ", numero_de_pares)
    entropia_del_punto_tres = calcular_entropia_secuencia_extendida(frecuencia_pares, numero_de_pares)
    print("La información total : ", entropia_del_punto_tres * numero_de_pares)
    return entropia_del_punto_tres

def calcular_entropia_cuarto_punto():
    print("\nCuarto punto: \n")
    texto = leer_archivo()
    longitud = len(texto)
    frecuencia_caracteres = obtener_frecuencia_caracteres()
    frecuencia_pares = obtener_frecuencia_pares()
    
    probabilidad_condicional = {}
    for clave in frecuencia_pares.keys():
        for subclave in frecuencia_caracteres.keys():
            if clave[:len(subclave)] == subclave:
                probabilidad_condicional[clave] = frecuencia_pares[clave] / frecuencia_caracteres[subclave]
    
    entropia_condicional = {}
    for clave, valor in probabilidad_condicional.items():
        entropia = valor * log2(1 / valor)
        entropia_condicional[clave] = entropia
    
    entropia_estados = {}
    for clave in entropia_condicional:
        prefijo = clave[:-1]
        valor = entropia_condicional[clave]
        if prefijo in entropia_estados:
            entropia_estados[prefijo] += valor
        else:
            entropia_estados[prefijo] = valor
    
    for clave in frecuencia_caracteres:
        frecuencia_caracteres[clave] /= longitud
    
    entropias_ponderadas = {}  
    for clave in entropia_estados:
        entropias_ponderadas[clave] = entropia_estados[clave] * frecuencia_caracteres[clave]
    
    suma_entropias = sum(entropias_ponderadas.values())
    
    print("La entropía del cuarto punto es: ", suma_entropias, "\n")
    print("La información total en este caso sería: ", suma_entropias * obtener_numero_total_caracteres(), "\n")
    return "------------------------------------------------"

print("------------------------------------------------")
print("La entropía del primer punto es:","\n", calcular_entropia_secuencia(),"\n")
print("La entropía del segundo punto es: ", "\n", calcular_entropia_segundo_punto(),"\n")
print("La entropía del tercer punto es:", "\n", calcular_entropia_tercer_punto(),"\n")
print(calcular_entropia_cuarto_punto())
