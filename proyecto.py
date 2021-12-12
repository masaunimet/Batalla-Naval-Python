import random
from Usuarios import Usuarios
from Vehiculos_marinos import Buque
from Vehiculos_marinos import Barco
from Vehiculos_marinos import Submarino

def modulo1():
    """
        Trata sobre la toma y almacenamiento de datos del usuario:

        "username": Es el nickname o sobrenombre del usuario
        "verificador": va a verificar si el username esta en el registro
        "name": el nombre del usuario
        "edad": la edad del usuario
        "genero": el genero del usuario

        se hace el "objeto" de la información del usuario(username,name,edad,genero),en caso de que el usuario ya exista, saldra su informacion con solo poner su username

        retorna el objeto con sus parametros y su dirección en el archivo de texto
    """
    #"username" es el sobrenombre de la persona
    username = input("Ingrese su username:").lower()

    #el username va a ser el valor de retorno de la funcion nickname()
    username = nickname(username)

    #"verificador" es una variable que contendra los valores de retorno de verificar()
    verificador = verificar(username)

    #Si el primer valor de verificador es "True"
    if verificador[0] == True:

        #contenido va a ser una lista gracias al retorno de contenido_de_bd()
        contenido = contenido_de_bd()

        #contenido va a ser una lista del contenido dentro de la lista de "verificador[1]" y se hara una lista separandose con la palabra ","
        contenido = contenido[verificador[1]].split(",")

        print("\nBienvenido otra vez")

        #los datos de contenido funcionaran para hacer un objeto de usuario
        usuarios = Usuarios(contenido[0],contenido[1],contenido[2],contenido[3],contenido[4])

        print(f"\n{usuarios}")

        return editar(usuarios, verificador[1])

    #Si el primer valor de verificador es "False"
    else:
        
        #"name" es el nombre de la persona
        name = input("Ingrese su nombre:").capitalize()

        #el name va a ser el valor de retorno de la funcion nombre()
        name = nombre(name)

        #"edad" es la edad de la persona
        edad = input("Ingrese su edad:")

        #la edad va a ser el valor de retorno de la funcion Edad()
        edad = Edad(edad)

        #"genero" es el genero de la persona
        genero = input("Ponga 'M' para Masculino, 'F' para Femenino u 'O' para Otro:").upper()

        #el genero va a ser el valor de retorno de la funcion sexo()
        genero = sexo(genero)

        puntos = "0 pts"

        #los datos de (username,name,edad,genero) funcionaran para hacer un objeto de usuario
        usuarios = Usuarios(username,name,edad,genero,puntos)

        print(f"\n{usuarios}")

        #se abre el archivo de texto para agregarle a la ultima linea informacion con la palabra clave "alm"
        with open("almacenamiento.txt", "a") as alm:
            
            alm.write(f"{username},{name},{edad},{genero},{puntos}\n")

        return editar(usuarios, verificador[1])


def modulo2(usuario, linea):
    """
        La funcion trata sobre generar los vehiculos, el mapa y realizar el juego

        \tArgumentos => "usuario": es la informacion de la persona que esta jugando
        \t=>"linea": linea en donde se encuentra la informacion

        "desicion": es una variable para saber si el jugador quiere saber sobre el juego\n
        "bd": variable en donde se guardara toda la informacion del archivo de texto\n
        "datos": son los datos del usuario como edad y nombre\n
        "disparos_realizados": contendra la cantidad de disparos totales en la mejor partida\n
        "matriz": Es la matriz base 10x10\n
        "matriz_actualizada": es la matriz que vera el usuario cuando juegue\n
        "matriz_correcta":  es la matriz en donde estara la posicion de la flota\n
        "puntos_estrategia": es una variable que contiene(puntos, disparos, disparos repetidos y el tablero) de la funcion juego()
        "datos1": es una lista que contendra los username y disparos realizados de los que jugaron

        Se hace el llamado a objetos (buqueejemplo[3 espacios],barcoejemplo[2 espacios],submarinoejemplo[1 espacio]) que 
        funcionaran como ejemplo para desplegar la informacion que hace cada uno y tambien a (buque,barco,submarino1,2,3 y 4) para ponerlos en el tablero
        en lugares aleatorios y posiciones aleatorias(vertical,horizontal)

        No Retorna nada
    """
    #buqueejemplo es un objeto de Buque()
    buqueejemplo = Buque(3,10,10,1)

    #barcoejemplo es un objeto de Barco()
    barcoejemplo = Barco(2,10,10,1)

    #submarinoejemplo es un objeto de Submarino()
    submarinoejemplo = Submarino(1,10,10)

    desicion = input("\n¿Desea saber sobre el juego?Y/N\n").upper()

    #Mientras que desicion sea diferente a "Y" y "N"
    while desicion != "Y" and desicion != "N":

        desicion = input("Bienvanido a batalla naval!\n¿Desea saber sobre el juego?Y/N\n").upper()
    
    #Si desicion es "Y"
    if desicion == "Y":

        print(f"""\nbatalla naval es un juego en donde el usuario tiene que poner, en cordenadas, donde va a dispara para hundir la flota enemiga.
La flota enemiga esta conformada por:
        
Un buque que {buqueejemplo.info()}
        
Un barco que {barcoejemplo.info()}
        
Y tres submarinos que {submarinoejemplo.info()}
        
para poder ganar deberas hundir todos los vehiculos marinos enemigos, mientras menos disparos utilizes, mejor sera tu puntuación\n""")

    #Mientras que sea verdadero
    while True:

        #bd sera igual al valor de retorno de contenido_de_bd()
        bd = contenido_de_bd()
        datos =""
        matriz =[]
        disparos_realizados = 0
        coordenadas =[]
        contador = 0
        opcion = 0
        listanueva = ""
        datos1 =[]

        #buque es un objeto de Buque()
        buque = Buque(3,random.randrange(1,11), random.randrange(1,11), random.randrange(1,3))

        #barco es un objeto de Barco()
        barco = Barco(2,random.randrange(1,11), random.randrange(1,11), random.randrange(1,3))

        #submarino1 es un objeto de Submarino()
        submarino1 = Submarino(1,random.randrange(1,11), random.randrange(1,11))

        #submarino2 es un objeto de Submarino()
        submarino2 = Submarino(1,random.randrange(1,11), random.randrange(1,11))

        #submarino3 es un objeto de Submarino()
        submarino3 = Submarino(1,random.randrange(1,11), random.randrange(1,11))

        #submarino4 es un objeto de Submarino()
        submarino4 = Submarino(1,random.randrange(1,11), random.randrange(1,11))

        #Bucle de 10 iteraciones
        for y in range(10):

                matriz.append([])

                #Bucle de 10 iteraciones
                for x in range(10):

                    matriz[y].append("?")

        #La matriz tendra el valor de retorno de la funcion configuracion()
        matriz = configuracion(matriz,buque.tamaño,buque.ejex,buque.ejey,buque.lado)

        #La matriz tendra el valor de retorno de la funcion configuracion()
        matriz = configuracion(matriz,barco.tamaño,barco.ejex,barco.ejey,barco.lado)

        #La matriz tendra el valor de retorno de la funcion configuracion()
        matriz = configuracion(matriz,submarino1.tamaño,submarino1.ejex,submarino1.ejey,"Vertical")

        #La matriz tendra el valor de retorno de la funcion configuracion()
        matriz = configuracion(matriz,submarino2.tamaño,submarino2.ejex,submarino2.ejey,"Vertical")

        #La matriz tendra el valor de retorno de la funcion configuracion()       
        matriz = configuracion(matriz,submarino3.tamaño,submarino3.ejex,submarino3.ejey,"Vertical")

        #La matriz tendra el valor de retorno de la funcion configuracion()
        matriz = configuracion(matriz,submarino4.tamaño,submarino4.ejex,submarino4.ejey,"Vertical")
        
        #Bucle del tamaño de matriz
        for y in range(len(matriz)):

            #Bucle del tamaño de matriz[y]
            for x in range(len(matriz[y])):

                #Si la matriz[posiciony][posicionx] es igual a "N"
                if matriz[y][x] == "N":
                    
                    matriz[y][x] = "?"
                
                #Sino, si la matriz[posiciony][posicionx] es diferente de a "?" y diferente a "N"
                elif matriz[y][x] !="?" and matriz[y][x] != "N":

                    coordenadas.append([])

                    coordenadas[contador].append(y+1)
                    coordenadas[contador].append(x+1)

                    contador +=1

        #matriz_correcta va a tener el valor de retorno de mapa()
        matriz_correcta = mapa(coordenadas,1)

        #matriz_actualizada va a tener el valor de retorno de mapa()
        matriz_actualizada = mapa(coordenadas,0)

        #puntos_estrategia va a tener el valor de retorno de juego()
        puntos_estrategia = juego(matriz_correcta, matriz_actualizada)

        print(puntos_estrategia[3],"\n")

        #datos_usuario va a ser una lista del string del usuario
        datos_usuario = str(usuario).split(",")

        username = datos_usuario[0]

        #puntos_almacenados va a ser igual al ultimo elemento de datos_usuarios cortandole 4 caracteres del final y si hay espacios en blanco los elimina
        puntos_alamacenados = datos_usuario[-1][:-4].strip()

        print(username)
        print(puntos_estrategia[0],"Pts")
        print(puntos_estrategia[1],"Disparos realizados")
        print(puntos_estrategia[2],"Disparos repetidos")

        disparos_realizados = puntos_estrategia[1] + puntos_estrategia[2]

        #Si puntos_estrategia[1] es menor o igual que 9
        if puntos_estrategia[1] <= 9:

            print("¿Eres un Robot? lo que acabas de hacer es poco probable...")

        #Sino, si puntos_estrategia[1] es menor o igual que 45
        elif puntos_estrategia[1] <= 45:

            print("Excelente Estrategia")

        #Sino, si puntos_estrategia[1] es menor o igual que 70
        elif puntos_estrategia[1] <= 70:

            print("Buena Estrategia; pero hay que mejorar")

        #Sino, si puntos_estrategia[1] es mayor que 70
        elif puntos_estrategia[1] > 70:

            print("Considérese Perdedor, tiene que mejorar notablemente")

        #Si el numero de puntos_estrategia[0] es mayor al numero de puntos_alamacenados
        if int(puntos_estrategia[0]) > int(puntos_alamacenados):

            puntos_alamacenados = puntos_estrategia[0]

        puntos_alamacenados = (f"{str(puntos_alamacenados)} pts\n")

        datos_usuario[-1] = puntos_alamacenados

        #bucle del tamaño de datos_usuario
        for dato in range(len(datos_usuario)):

            #Si dato es diferente al tamaño de datos_usuario -1
            if dato != len(datos_usuario)-1:

                datos += datos_usuario[dato]+","
            
            #Sino
            else:

                datos += datos_usuario[dato]

        #El elemento de linea de bd va a ser igual a datos
        bd[linea] = datos

        #se abre el archivo de texto para sobreescribir la informacion con la palabra clave "bdw"
        with open("almacenamiento.txt", "w") as bdw:

            #Bucle de los elementos en bd
            for lineas in bd:

                bdw.write(lineas)

        #se abre el archivo de texto para leer la informacion con la palabra clave "ud"
        with open("usuarios_disparos.txt", "r") as ud:

            #lista va a ser una lista con toda la informacion del archivo de texto
            lista = ud.readlines()
        
        #Si el tamaño de la lista es diferente a 0
        if len(lista) != 0:
    
            #Bucle del tamaño de lista
            for contenido in range(len(lista)):

                datos1.append(lista[contenido].split(","))

                #si datos1[contenido][0](osea los usernames) es igual a username
                if datos1[contenido][0] == username:
                    
                    #Si los disparos realizados son menores a lo que hay registrado
                    if disparos_realizados < int(datos1[contenido][1][:-21].strip()):

                        opcion = 0
                        lista.pop(contenido)

                        #se abre el archivo de texto para sobreescribir la informacion con la palabra clave "ud2"
                        with open("usuarios_disparos.txt","w") as ud2:

                            #Bucle de los elementos de lista
                            for tamañodelista in lista:

                                listanueva +=tamañodelista

                            ud2.write(listanueva)
                        
                        break

                    #Sino
                    else:

                        opcion = 1    

                        break

        #Si la opcion es igual a 0
        if opcion ==0:

            with open("usuarios_disparos.txt","a") as ud:

                ud.write(f"{username}, {disparos_realizados} disparos realizados\n")

        seleccion = input("¿Quieres jugar de nuevo?Y/N").upper()

        #Mientras que seleccion sea diferente a "Y" y a "N"
        while seleccion != "Y" and seleccion != "N":

            seleccion = input("¿Quieres jugar de nuevo?Y/N").upper()

        #Si seleccion es igual a "N"
        if seleccion == "N":

            break


def modulo3():
    """
        La funcion sirve para comparar las estadisticas de los jugadores

        "datos_usuarios": es una matriz en donde se tiene el contenido de los usuarios "almacenamiento"\n
        "de5a18": es una variable que tiene el numero de personas con la edad de 5 hasta 18\n
        "de5a18_list": es una lista donde estan las personas con la edad de 5 hasta 18\n
        "de19a45": es una variable que tiene el numero de personas con la edad de 19 hasta 45\n
        "de19a45_list": es una lista donde estan las personas con la edad de 19 hasta 45\n
        "de46a60": es una variable que tiene el numero de personas con la edad de 45 hasta 60\n
        "de46a60_list": es una lista donde estan las personas con la edad de 46 hasta 60\n
        "de61a100": es una variable que tiene el numero de personas con la edad de 61 hasta 100\n
        "de61a100_list": es una lista donde estan las personas con la edad de 61 hasta 100\n
        "puntosmasculinos": es la cantidad de puntos que tiene el genero "Masculino" en el juego\n
        "puntosfemeninos": es la cantidad de puntos que tiene el genero "Femenino" en el juego\n
        "puntosotros": es la cantidad de puntos que tiene el genero "Otros" en el juego\n
        "disparos_realizados": es la cantidad de disparos que hicieron los usuarios\n
        "datos": Tiene la informacion del archivo de texto "usuarios_disparos"\n
        No retorna nada
    """

    datos_usuarios = []

    de5a18 = 0
    de5a18_list = []
    de19a45 =0
    de19a45_list = []
    de46a60 =0
    de46a60_list = []
    de61a100 =0
    de61a100_list = []
    puntosmasculinos = 0
    puntosfemeninos = 0
    puntosotros = 0
    disparos_realizados =0
    datos =[]

    #Base_datos va a tener el valor de retorno de contenido_de_bd()
    Base_datos = contenido_de_bd()

    #Bucle de los elementos en Base_datos
    for elementos in Base_datos:

        datos_usuarios.append(elementos.split(","))

    #Bucle del tamaño de datos_usuarios
    for x in range(len(datos_usuarios)):

        #parametro es igual a la edad de los usuarios
        parametro = datos_usuarios[x][2][:-6]
        #genero es igual al genero de los usuarios
        genero = datos_usuarios[x][3]

        #Si el parametro es mayor o igual que 5 y menor o igual que 18
        if int(parametro)>=5 and int(parametro)<=18:

            de5a18 +=1
            de5a18_list.append(datos_usuarios[x][0])

        #Si el parametro es mayor o igual que 19 y menor o igual que 45
        elif int(parametro)>=19 and int(parametro)<=45:

            de19a45 +=1
            de19a45_list.append(datos_usuarios[x][0])
        
        #Si el parametro es mayor o igual que 46 y menor o igual que 60
        elif int(parametro)>=46 and int(parametro)<=60:

            de46a60 += 1
            de46a60_list.append(datos_usuarios[x][0])

        #Si el parametro es mayor o igual que 61 y menor o igual que 100
        elif int(parametro)>=61 and int(parametro)<=100:

            de61a100 +=1
            de61a100_list.append(datos_usuarios[x][0])
        
        #Si genero es igual a Masculino
        if genero == "Masculino":

            puntosmasculinos +=int(datos_usuarios[x][-1][:-5])
        
        #Si genero es igual a Femenino
        elif genero == "Femenino":

            puntosfemeninos +=int(datos_usuarios[x][-1][:-5])

        #Si genero es igual a Otro
        elif genero == "Otro":

            puntosotros +=int(datos_usuarios[x][-1][:-5])

    #se abre el archivo de texto para leer la informacion con la palabra clave "ud"
    with open("usuarios_disparos.txt", "r") as ud:

        lista = ud.readlines()
    
    #Bucle del tamaño de lista
    for contenido in range(len(lista)):

        #datos va a ser una lista de listas con valor del archivo de texto "usuarios_disparos"
        datos.append(lista[contenido].split(","))

        #disparos_realizados va a ser la suma de los disparos registrados en el archivo de texto "usuarios_disparos"
        disparos_realizados += int(datos[contenido][-1][:-21])
    
    promedio = disparos_realizados/len(lista)
    
    print(f"\nEl intervalo de edad de nuestros jugadores es:\n1.De 5 a 18 años:{de5a18}\n{de5a18_list}")
    print(f"2.De 19 a 45 años:{de19a45}\n{de19a45_list}")
    print(f"3.De 46 a 60 años:{de46a60}\n{de46a60_list}")
    print(f"4.De 61 a 100 años:{de61a100}\n{de61a100_list}\n")

    print(f"Los puntos por genero Masulino son:{puntosmasculinos}\nFemenino son:{puntosfemeninos}\nOtros son:{puntosotros}")

    print(f"\nEl promedio hasta ahora para poder ganar es de: {promedio} disparos")

def juego(correcto, mesa):
    """
        La funcion consiste en que el usuario trate de descubrir y hundir la flota enemiga

        \tArgumento=>"correcto": es la matriz con la posicion de la flota enemiga
        \t=>"mesa": es el tablero que observa el usuario

        "puntos": son los puntos que va a tener el jugador\n
        "disparo": es una lista que guarda las posiciones en el eje x y eje y de donde se disparara\n
        "iteraciones": es el numero de veces de disparos realizados\n
        "disparos_repetidos": toma las veces que se realiza un disparo en un lugar ya conocido\n
        Retorna los valores puntos, disparos, disparos repetidos y el tablero
    """
    puntos =0
    iteraciones = 0
    disparos_repetidos =0

    #Mientras que sea verdadero
    while True:

        iteraciones +=1
        contador = 0
        disparo =[]

        #Se imprime el valor retornable de tablero()
        print(tablero(mesa))

        print("¿En donde desea disparar?\n")

        #Se escoge el punto con respecto al eje x
        posx = input("Posicion en x: ")

        #Si posx es igual a "codigo konami"
        #P.D: dejo esto aqui para que sea mas facil saber donde esta la flota(para corregir mas facil)
        if posx == "codigo konami":

            #Bucle del tamaño de correcto
            for lineas in range(len(correcto)):

                print(correcto[lineas])

        #Mientras que posx no sea un numero natural o sea menor que uno o mayor que 10
        while not posx.isdecimal() or int(posx) > 10 or int(posx) < 1:

            posx = input("Posicion en x: ")

        #Se escoge el punto con respecto al eje y
        posy = input("posicion en y: ")

        #Mientras que posy no sea un numero natural o sea menor que uno o mayor que 10
        while not posy.isdecimal() or int(posy) > 10 or int(posy) < 1:

            posy = input("Posicion en y: ")

        disparo.append(posy)
        disparo.append(posx)

        #Si en las posiciones suministradas en mesa es diferente a "?"
        if mesa[int(posy)][int(posx)]  != "?":

            print("\nDisparo Ya Realizado")

            disparos_repetidos +=1

        #Sino, si en las posiciones que pusimos hay una "O" en correcto
        elif correcto[int(posy)][int(posx)] == "O":

            print("\n¡Le diste!")

            #En el lugar que le diste, la mesa cambiara a "O"
            mesa[int(posy)][int(posx)] = "O"

            puntos +=10
        
        #Sino, si en las posiciones que pusimos es diferente a "O" en correcto
        elif correcto[int(posy)][int(posy)] != "O":

            print("\nFallaste")

            #En el lugar que le diste, la mesa cambiara a "X"
            mesa[int(posy)][int(posx)] = "X"

            puntos -=2

            #Si los puntos son menores a 0
            if puntos < 0:
 
                puntos = 0
        
        #Bucle de los elementos de mesa
        for listas in mesa:

            #Bucle de los elementos de listas
            for contenido in listas:

                #Si el contenido es igual a "O"
                if contenido == "O":

                    contador +=1

        #Si el contador es mayor o igual que 9
        if contador >= 9:

            break

        print(puntos,"pts\n")

    return [puntos, iteraciones, disparos_repetidos, tablero(mesa)]


def configuracion(matriz,tamaño,x,y,lado):

    """
        La funcion es para colocar los buques, barcos y submarinos en el mapa

        \tArgumento=>"matriz": es el mapa donde se colocaran los barcos
        \t=>"tamaño": el tamaño que tiene el vehiculo en espacio
        \t=>"x": es la posicion en x donde estara el vehiculo
        \t=>"y": es la posicion en y donde estara el vehiculo
        \t=>"lado": es si esta vertical u horizontal el vehiculo

        Retorno es la matriz con el vehiculo puesto ahi
    """

    #Mientras que la posicion de la matriz sea diferente a "?"
    while matriz[y-1][x-1] != "?":

        x = random.randrange(1,11)
        y = random.randrange(1,11)

    #Si el lado es igual a 1
    if lado == 1:

        lado = "Vertical"
    
    #Sino, si el lado es igual a 1
    elif lado == 2:

        lado = "Horizontal"
       
    #bucle del tamaño de la matriz
    for ys in range(len(matriz)):

        #Si ys es igual a la posicion "y" menos 1
        if ys == y -1:

            #bucle del tamaño de la matriz[ys]
            for xs in range(len(matriz[ys])):

                #Si ys es igual a la posicion "x" menos 1
                if xs == x-1:

                    #Se coloca un espacio de vehiculo en las posiciones de la matriz[en y][en x]
                    matriz[ys][xs] = str(tamaño)

                    #Si lado es igual a "Vertical"
                    if lado == "Vertical":

                        #Si ys es igual a 0
                        if ys == 0:

                            #Si es un buque
                            if tamaño ==3:

                                matriz[ys+1][xs] = str(tamaño)
                                matriz[ys+2][xs] = str(tamaño)
                                
                            #Sino, si es un barco
                            elif tamaño ==2:

                                #Si la matriz un espacio mas abajo es diferente a "N"
                                if matriz[ys+1][xs] != "N":

                                    matriz[ys+1][xs] = str(tamaño)
                                
                                #Sino
                                else:

                                    #Si ocurre un error
                                    try:

                                        matriz[ys][xs+1] = str(tamaño)
                                        lado = "Horizontal"
                                    
                                    #En especifico "IndexError"
                                    except(IndexError):

                                        matriz[ys][xs-1] = str(tamaño)
                                        lado = "Horizontal"

                            #matriz va a tener el valor de retorno de espacios()
                            matriz = espacios(matriz,lado,tamaño)

                        #Sino, si ys es igual a 9        
                        elif ys == 9:

                            #Si es un buque
                            if tamaño == 3:

                                matriz[ys-1][xs] = str(tamaño)
                                matriz[ys-2][xs] = str(tamaño)

                            #Si es un barco    
                            elif tamaño ==2:

                                #Si la matriz un espacio mas arriba es diferente a "N"
                                if matriz[ys-1][xs] != "N":

                                    matriz[ys-1][xs] = str(tamaño)
                                
                                #Sino
                                else:

                                    #Si ocurre un error
                                    try:

                                        matriz[ys][xs-1] = str(tamaño)
                                        lado = "Horizontal"
                                    
                                    #En especifico "IndexError"
                                    except(IndexError):

                                        matriz[ys][xs+1] = str(tamaño)
                                        lado = "Horizontal"

                            #matriz va a tener el valor de retorno de espacios()
                            matriz = espacios(matriz,lado,tamaño)

                        #Sino, si ys es menor que 9 y mayor que 0
                        elif ys<9 and ys>0:
                                
                            #Si es un buque
                            if tamaño ==3:

                                matriz[ys+1][xs] = str(tamaño)
                                matriz[ys-1][xs] = str(tamaño)

                            #Sino, si es un barco 
                            elif tamaño ==2:

                                #Si la matriz un espacio mas abajo es diferente a "N"
                                if matriz[ys+1][xs] != "N":

                                    matriz[ys+1][xs] = str(tamaño)
                                
                                #Sino
                                else:

                                    #Si ocurre un error
                                    try:

                                        matriz[ys][xs+1] = str(tamaño)
                                        lado = "Horizontal"

                                    #En especifico "IndexError"
                                    except(IndexError):

                                        matriz[ys][xs-1] = str(tamaño)
                                        lado = "Horizontal"

                            #matriz va a tener el valor de retorno de espacios()
                            matriz = espacios(matriz,lado,tamaño)

                    #Sino, si lado es igual a "Horizontal"
                    elif lado == "Horizontal":
                        
                        #Si xs es igual a 0
                        if xs == 0:

                            #Si es un buque
                            if tamaño == 3:

                                matriz[ys][xs+1] = str(tamaño)
                                matriz[ys][xs+2] = str(tamaño)
                            
                            #Sino, si es un barco
                            elif tamaño ==2:

                                #Si la posicion de la matriz es un lado más a la derecha diferente a "N"
                                if matriz[ys][xs+1] != "N":

                                    matriz[ys][xs+1] = str(tamaño)
                                
                                #Sino
                                else:

                                    #Si ocurre un error
                                    try:
                                        matriz[ys-1][xs] = str(tamaño)
                                        lado = "Vertical"
                                    
                                    #En especifico "IndexError"
                                    except(IndexError):

                                        matriz[ys+1][xs] = str(tamaño)
                                        lado = "Vertical"

                            #matriz va a tener el valor de retorno de espacios()
                            matriz = espacios(matriz,lado,tamaño)

                        #Sino, si xs es igual a 9
                        elif xs == 9:

                            #Si es un buque
                            if tamaño == 3:

                                matriz[ys][xs-1] = str(tamaño)
                                matriz[ys][xs-2] = str(tamaño)

                            #Sino, si es un barco
                            elif tamaño == 2:

                                #Si la posicion de la matriz es un lado más a la izquierda diferente a "N"
                                if matriz[ys][xs-1] != "N":

                                    matriz[ys][xs-1] = str(tamaño)
                                
                                #Sino
                                else:

                                    #Si ocurre un error
                                    try:

                                        matriz[ys-1][xs] = str(tamaño)
                                        lado = "Horizontal"

                                    #En especifico "IndexError"
                                    except(IndexError):

                                        matriz[ys+1][xs] = str(tamaño)
                                        lado = "Horizontal"

                            #matriz va a tener el valor de retorno de espacios()
                            matriz = espacios(matriz,lado,tamaño)

                        #Sino, si xs es mayor a 0 y menor a 9
                        elif xs<9 and xs>0:

                            #Si es un buque
                            if tamaño == 3:

                                matriz[ys][xs+1] = str(tamaño)
                                matriz[ys][xs-1] = str(tamaño)
                                
                            #Sino, si es un barco
                            elif tamaño ==2:

                                #Si la posicion de la matriz es un lado más a la derecha diferente a "N"
                                if matriz[ys][xs+1] != "N":

                                    matriz[ys][xs+1] = str(tamaño)
                                
                                #Sino
                                else:

                                    #Si ocurre un error
                                    try:

                                        matriz[ys+1][xs] = str(tamaño)
                                        lado = "Horizontal"

                                    #En especifico "IndexError"
                                    except(IndexError):

                                        matriz[ys-1][xs] = str(tamaño)
                                        lado = "Horizontal"

                            #matriz va a tener el valor de retorno de espacios()
                            matriz = espacios(matriz,lado,tamaño)

    return matriz

def espacios(matriz,lado,tamaño):
    """
        La funcion trata sobre validar los espacios continuos para que no halla vehiculos continuos a otros

        \tArgumentos=>"matriz": es el mapa al cual se le va a modificar
        \t=>"lado": si esta en "Horizontal" o "Vertical"
        \t=>"tamaño": el tamaño de espacios que ocupa el vehiculo en la matriz

        Retorna la matriz actualizada(validando los espacios continuos a vehiculos)
    """

    #Bucle del tamaño de la matriz
    for y in range(len(matriz)):

        #Bucle del tamaño de la matriz[y]
        for x in range(len(matriz[y])):

            #Si la matriz[posicion y][posicion x] es igual al tamaño
            if matriz[y][x] == str(tamaño):

                #Si el lado es igual a "Vertical"
                if lado == "Vertical":

                    #Si la posicion en "y" y "x" es igual a 9
                    if y == 9 and x == 9:

                        #Si es un submarino
                        if tamaño == 1:

                            matriz[y][x-1] = "N"
                            matriz[0][x] = "N"
                            matriz[0][x-1] = "N"
                            matriz[y][0] = "N"
                            matriz[y-1][x] = "N"
                            matriz[y-1][x-1] = "N"
                            matriz[y-1][0] = "N"
                            matriz[0][0] = "N"
                        
                        #Sino, si es un barco o buque
                        elif tamaño == 3 or tamaño ==2:

                            matriz[y][x-1] = "N"
                            matriz[0][x] = "N"
                            matriz[0][x-1] = "N"
                            matriz[y][0] = "N"

                    #Sino, si la posicion en x es 9
                    elif x ==9:

                        matriz[y][0] = "N"
                        matriz[y][x-1] = "N"
                    
                        #Si la matriz esta un lugar más arriba es diferente al vehiculo
                        if matriz[y-1][x] != str(tamaño):

                            matriz[y-1][x] = "N"
                            matriz[y-1][x-1] = "N"
                            matriz[y-1][0] = "N"
                        
                        #Si ocurre un error
                        try:

                            #Si la matriz esta un lugar más abajo es diferente al vehiculo
                            if matriz[y+1][x] != str(tamaño):
                            
                                matriz[y+1][x] = "N"
                                matriz[y+1][x-1] = "N"
                                matriz[y+1][0] = "N"
                        
                        #Si el error es IndexError
                        except(IndexError):

                            continue

                    #Sino, si y es menor que 9  o x menor que 9
                    elif y<9 or x < 9:

                        matriz[y][x+1] = "N"
                        matriz[y][x-1] = "N"

                        #Si la matriz esta un lugar más arriba es diferente al vehiculo
                        if matriz[y-1][x] != str(tamaño):

                            matriz[y-1][x] = "N"
                            matriz[y-1][x-1] = "N"
                            matriz[y-1][x+1] = "N"
                        
                        #Si ocurre un error
                        try:
                            
                            #Si la matriz esta un lugar más abajo es diferente al vehiculo
                            if matriz[y+1][x] != str(tamaño):

                                matriz[y+1][x] = "N"
                                matriz[y+1][x-1] = "N"
                                matriz[y+1][x+1] = "N"

                        #Si ocurre el error "IndexError"
                        except(IndexError):

                            matriz[0][x+1] = "N"
                            matriz[0][x] = "N"
                            matriz[0][x-1] = "N"

                            continue
                
                #Si el lado es "Horizontal"
                elif lado == "Horizontal":

                    #Si "y" y "x" es igual a 9
                    if y ==9 and x==9:

                        matriz[0][x] = "N"
                        matriz[y][0] = "N"
                        matriz[y-1][x] = "N"
                        matriz[y-1][0] = "N"

                    #Sino, si "y" es igual a 9
                    elif y ==9:
                        
                        matriz[0][x] = "N"
                        matriz[y-1][x] = "N"

                        #Si la matriz esta un lugar más a la izquierda es diferente al vehiculo
                        if matriz[y][x-1] != str(tamaño):

                            matriz[y][x-1] = "N"
                            matriz[y-1][x-1] = "N"
                            matriz[0][x-1] = "N"
                        
                        #Si ocurre un error
                        try:
                    
                            #Si la matriz esta un lugar más a la derecha es diferente al vehiculo 
                            if matriz[y][x+1] != str(tamaño):

                                matriz[y][x+1] = "N"
                                matriz[0][x+1] = "N"
                                matriz[y-1][x+1] = "N"
                        
                        #Si el error es "IndexError"
                        except(IndexError):

                            continue

                    #Sino, si "y" es menor que 9 o "x" menor que 9
                    elif y<9 or x<9:

                        matriz[y+1][x] = "N"
                        matriz[y-1][x] = "N"

                        #Si la matriz esta un lugar más a la izquierda es diferente al vehiculo
                        if matriz[y][x-1] != str(tamaño):

                            matriz[y][x-1] = "N"
                            matriz[y-1][x-1] = "N"
                            matriz[y+1][x-1] = "N"

                        #Si ocurre un error
                        try:
                            
                            #Si la matriz esta un lugar más a la derecha es diferente al vehiculo
                            if matriz[y][x+1] != str(tamaño):

                                matriz[y][x+1] = "N"
                                matriz[y+1][x+1] = "N"
                                matriz[y-1][x+1] = "N"

                        #Si el error es "IndexError"
                        except(IndexError):

                            matriz[y+1][0] = "N"
                            matriz[y][0] = "N"
                            matriz[y-1][0] = "N"

                            continue
            continue

    return matriz

def nickname(username):

    """
        Es una funcion para regresar el username sin espacios en blanco y de 30 caracteres
        \tArgumento => "username" es un string que ingreso el usuario para su sobrenombre
        Retorna el username
    """

    #"x" es una lista de cada palabra del username
    x = username.split()

    #Mientras que el tamaño de username sea mayor a 30 o 0 o el tamaño de x sea 0 o el username sea espacios en blanco
    while len(username) > 30 or len(x) > 1 or len(username) == 0 or username.isspace():

        username = input("Ingrese su username:").lower()

        #"x" es una lista de cada palabra del username
        x = username.split()

    #username sera igual a el mismo sin espacios en blanco    
    username = username.strip()

    return username

def nombre(name):

    """
        La funcion trata sobre que el nombre inicie en mayuscula y sean caracteres alfabeticos
        \tArgumento => "name" es un string que ingreso el usuario para su nombre

        "new_name": va a ser el valor en donde se verifique el nombre\n
        "name_list": toda la info se guardara en la lista y los espacios seran la clave para ello\n
        Retorna el nombre
    """
    new_name = ""

    #la lista "name_list" valera todos las palabras de "name sin espacios"
    name_list = name.split()

    #Bucle por el tamaño de name_list
    for names in range(len(name_list)):

        #"new_name" va a concatenr la informacion que hay dentro de la lista "name_list"
        new_name += name_list[names].capitalize()
    
    #"name" va a valer lo que es "new_name"
    name = new_name

    #Mientras que el nombre no sea alfabetico
    while not name.isalpha():

        name = input("Ingrese su nombre:").capitalize()

        new_name = ""

        #la lista "name_list" valera todos las palabras de "name sin espacios"
        name_list = name.split()

        #Bucle por el tamaño de name_list
        for names in range(len(name_list)):

            #"new_name" va a concatenr la informacion que hay dentro de la lista "name_list"
            new_name += name_list[names].capitalize()

        #"name" va a valer lo que es "new_name"
        name = new_name

    return name

def Edad(edad):

    """
        La funcion trata sobre que la edad inicie sea de caracter numerico
        \tArgumento => "edad" es un string que ingreso el usuario para su edad
        Retorna la edad
    """

    #Mientras que la edad no sea un numero natural o el numero sea menor a 5 o mayor a 100
    while not edad.isdecimal() or int(edad) <5 or int(edad) > 100:

        edad = input("Ingrese su edad:")
    
    edad += " anios"
    
    return edad

def sexo(genero):

    """
        La funcion trata sobre que el genero sea Masculino, Femenino u Otro
        \tArgumento => "genero" es un string que ingreso el usuario para su genero
        Retorna el genero
    """

    #Mientras que genero sea diferente a "M" y "F" y "O"
    while genero != 'M' and genero != 'F' and genero != 'O':

        genero = input("Ponga 'M' para Masculino, 'F' para Femenino u 'O' para Otro:").upper()

    #Si genero es "M" 
    if genero == "M":

        genero = "Masculino"

    #Si genero es "F"     
    elif genero =="F":

        genero = "Femenino"

    #Si genero es "O" 
    elif genero == "O":

        genero ="Otro"
    
    return genero

def mapa(lugares_claves,codigo):
    """
        Tiene la funcion de crear una matriz que funcione como mapa o tablero

        \tArgumento=>"lugares_claves": una lista en donde se encuentra localizada la flota
        \t=>"codigo": si se quiere crear solamente un tablero normal "else" o si se quiere crear la matriz con los barcos

        "matriz" es una lista de listas donde tendra cada punto como una x o contador x o y\n
        "contador_x" es un numero que sirve como punto de referencia en el tablero en el eje x\n
        "contador_y" es un numero que sirve como punto de referencia en el tablero en el eje y\n
        Retorna la matriz lista
    """

    matriz = []

    contador_x = 1
    contador_y = 1

    #Si codigo es 1
    if codigo == 1:

        #Bucle de 11 iteraciones
        for y in range(11):

            matriz.append([])

            #Bucle de 11 iteraciones
            for x in range(11):

                #Si y es 0 y x es diferente de 0
                if y == 0 and x !=0:

                    matriz[y].append(str(contador_y))

                    contador_y +=1

                #Sino, si y es igual a 0 y x es igual a 0
                elif y ==0 and x ==0:

                    matriz[y].append(" ")
                
                #Sino
                else:

                    #Si x es 0
                    if x == 0:

                        matriz[y].append(str(contador_x))

                        contador_x +=1
                    
                    #Sino
                    else:

                        matriz[y].append("?")

        #bucle de los elementos de lugares_clave
        for cordenadas in lugares_claves:

            matriz[cordenadas[0]][cordenadas[1]] = "O"

    #Sino
    else:

        #Bucle de 11 iteraciones
        for y in range(11):

            matriz.append([])

            #Bucle de 11 iteraciones
            for x in range(11):

                #Si y es 0 y x es diferente de 0
                if y == 0 and x !=0:

                    matriz[y].append(str(contador_y))

                    contador_y +=1

                #Sino, si y es igual a 0 y x es igual a 0
                elif y ==0 and x ==0:

                    matriz[y].append(" ")
                
                #Sino
                else:

                    #Si x es 0
                    if x == 0:

                        matriz[y].append(str(contador_x))

                        contador_x +=1
                    
                    #Sino
                    else:

                        matriz[y].append("?")
    
    return matriz

def tablero(matriz):
    """
        Es utilizado para ordenar una matriz y hacerla parecer un tablero en la pantalla
        \tArgumentos => "matriz" es una lista de listas donde tendra cada posicion como una "x" o contador de los ejes x y/o y

        "tablero" es un string que contendra la informacion de la matriz organizada

        Retorna el parametro "tablero"
    """

    tablero = ""
    
    #bucle del tamaño de la matriz
    for lista in range(len(matriz)):

        #bucle del tamaño de matriz[lista]
        for posicion in range(len(matriz[lista])):

            #Si posicion es menor que 0 y posicion es mayor que 0
            if posicion <10 and posicion>0:

                tablero += matriz[lista][posicion]
                tablero += "-"

            #Sino, si posicion es 0
            elif posicion ==0:

                tablero += matriz[lista][posicion]

                #Si lista es menor que 10
                if lista <10:

                    tablero += "  "
                
                #Sino
                else:

                    tablero += " "
                
            #Sino
            else:
                tablero += matriz[lista][posicion]
                tablero += "\n"
    return tablero

def verificar(username):
    """
        Toma el valor del username para verificar si ya esta en la base de datos
        \tArgumento => "username" es el nombre de la persona

        "info_completa": es una lista que contendra toda la informacion del archivo de texto\n
        "usernames": es una lista que tendra guardada todos los username del archivo de texto\n
        Retorna una lista con el valor True o False, mientras que otro es la linea de información de donde se encuentra la informacion sobre el usuario
    """

    info_completa = []
    usernames = []

    #"info_completa" es una lista que contiene toda informacion de almacenamiento.txt
    info_completa = contenido_de_bd()
    
    #bucle del tamaño de info_completa
    for x in range(len(info_completa)):

        #buche de cada letra en info_completa[x]
        for letra in info_completa[x]:

            #Si la letra es ","
            if letra == ",":
                
                #"y" es una variable que almacena en que numero esta la primera ","
                y = info_completa[x].find(",")

                #usernames almacena todos los usernames de el archivo de texto
                usernames.append(info_completa[x][:y])

                #Si el username es igual a algun username de almacenamiento 
                if usernames[x] == username:

                    return [True, x]

                break

    return [False, len(info_completa)]

def contenido_de_bd():

    """
        Hace que el contenido dentro del almacenamiento.txt quede guardado en una lista

        \tArgumento => "lista" es una lista donde va a guardado el: username, name, edad, sexo, puntos

        "lista": es una lista que tendra toda la informacion del archivo de texto

        Retorna la lista con los valores mencionados
    """

    lista = []

    #se abre el archivo de texto para leer las lineas de informacion con la palabra clave "alm"
    with open("almacenamiento.txt","r") as alm:

        #Por cada linea del archivo de texto
        for linea in alm:

            #la informacion queda guardada en una lista sin los saltos de linea
            lista.append(linea)

    return lista

def editar(usuarios, linea):

    """
        La funcion trata sobre la edicion de cierto valor en el almacenamiento
        \tArgumento => "usuarios" es un string con la información de la persona
        \t=> "linea" es el numero de la linea en donde se encuentra la informacion de "usuarios"

        "nuevo_valor": es la variable que contendra toda la informacion más lo que quiere cambiar el usuario\n
        "seleccion" es un string con el valor de "Y" para hacer la edicion y "N" para no hacerla\n
        "seleccion2" es un string con el valor de numeros del 1 al 4 con el objetivo de editar el username, nombre, edad o genero\n
        Retorna la nueva informacion completa del usuario
    """
    nuevo_valor = ''

    seleccion = input("\n¿Desea editar alguno de sus valores?Y/N").upper()

    #Mientras que seleccion sea diferente a "Y" o "N"
    while seleccion != "Y" and seleccion != "N":

        seleccion = input("\n¿Desea editar alguno de sus valores?Y/N").upper()
    
    #Si seleccion es "Y"
    if seleccion == "Y":

        print('¿Qué atributo desea modificar?\n1 - Username\n2 - Nombre\n3 - Edad\n4 - Género\n')

        seleccion2  = input('Seleccione una opción:')

        #Mientras que seleccion2 sea diferente a 1 y 2 y 3 y 4
        while seleccion2 !="1" and seleccion2 !="2" and seleccion2 !="3" and seleccion2 !="4":

            seleccion2  = input('Seleccione una opción:')

        #transforma el string a un numero entero
        seleccion2 = int(seleccion2)

        #datos va a valer los valores retornados de "contenido_de_bd()"
        datos = contenido_de_bd()

        #usuario es igual a la linea del usuario, ademas de dividirlo en lista con la palabra clave "," y quitarle el salto de linea
        usuario = datos[linea][:-1].split(',')
        
        #se selecciona el parametro de la lista deseado y se cambia por lo que pone el usuario
        usuario[seleccion2 - 1] = input("\nIngrese el nuevo valor:")

        #Si seleccion2 es 1
        if seleccion2 == 1:

            #se hace el llamado de la funcion "nickname()" para que se compruebe el valor
            usuario[seleccion2 - 1] = nickname(usuario[seleccion2 - 1])

        #Sino, si seleccion2 es 2
        elif seleccion2 == 2:

            #se hace el llamado de la funcion "nombre()" para que se compruebe el valor
            usuario[seleccion2 - 1] = nombre(usuario[seleccion2 - 1])

        #Sino, si seleccion2 es 3
        elif seleccion2 == 3:

            #se hace el llamado de la funcion "Edad()" para que se compruebe el valor
            usuario[seleccion2 - 1] = Edad(usuario[seleccion2 - 1])
        
        #Sino, si seleccion2 es 4
        elif seleccion2 == 4:
            
            #se hace el llamado de la funcion "Edad()" para que se compruebe el valor
            usuario[seleccion2 - 1] = sexo(usuario[seleccion2 - 1])

        #Bucle del tamaño de usuario
        for i in range(len(usuario)):

            #Si i es diferente al tamaño del usuario-1
            if i != len(usuario) -1:

                # todos los valores de la lista del usuario son puestos en un string con coma
                nuevo_valor += usuario[i] + ','

            #Sino
            else:

                #El valor final de la lista es puesto en el string
                nuevo_valor += usuario[i] + "\n"

        #se almacena la la nueva informacion en la linea que tiene que ir el usuario
        datos[linea] = nuevo_valor

        #se abre el archivo de texto para escribir las lineas de informacion con la palabra clave "alm"
        with open("almacenamiento.txt", "w") as alm:
            
            #se escribe el documento desde 0 con la informacion de "datos"
            alm.writelines(datos)
        
        return [nuevo_valor, linea]
    #sino
    else:

        return [usuarios, linea]

def batalla_naval():
    """
        Es la funcion que contiene todas las funciones del programa
        1. modulo1() que se encarga de la toma y almacenamiento de datos del usuario
        2. modulo2() que se enarga de generar los vehiculos, el mapa y realizar el juego
        3.modulo3() que se encarga de comparar estadisticas con los demas usuarios
    """

    print("¡Bienvenidos a batalla naval!\n")

    #modulo1_datos va a tener los valores de retorno de modulo1()
    modulo1_datos = modulo1()

    print(modulo1_datos[0])

    #modulo2_datos tiene el valor de retorno del primer y segundo elemento de modulo1_datos 
    modulo2(modulo1_datos[0],modulo1_datos[1])

    modulo3()

def main():

    batalla_naval()

main()