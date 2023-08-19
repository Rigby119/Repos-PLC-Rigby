'''
Algoritmo del reto
1.- DEFINIR lista_preguntas cómo una lista
2.- AGREGAR preguntas a la lista
3.- DEFINIR lista_respuestas cómo una lista
4.- AGREGAR repuestas a la lista de respuestas
5.- DEFINIR opciones cómo una lista
6.- AGREGAR las opciones de respuesta a la lista de opciones (A, B, C y D)
7.- DEFINIR la variable correcto IGUALANDOLA a 0
8.- IMPRIMIR un texto de bienvenida e instrucciones
9.- PEDIR el nombre del usuario y GUARDARLO en la variable nombre
10.- PARA CADA valor del 0 a la longitud de lista_preguntas:
    10.1.- DEFINIR ciclo cómo una variable booleana verdadera
    10.2.- IMPRIMIR la pregunta correspondiente
    10.3.- PEDIR la respuesta y GUARDARLA en la variable respuesta
    10.4.- SI respuesta esta EN la lista de opciones:
        10.4.1.- SI respuesta es IGUAL A la respuesta correspondiente:
            10.4.1.1.- SUMAR 1 a correcto
        10.4.2.- DECLARAR ciclo cómo falsa
    10.5.- SI NO:
        10.5.1.- IMPRIMIR "Por favor, introduzca la letra en mayúsculas"
11.- SI correcto es MENOR QUE el entero de la división de la longitud de lista_preguntas entre 2:
    11.1.- IMPRIMIR un mensaje de reprobado usando el nombre
12.- SI NO:
    12.1.- IMPRIMIR un mensaje de felicidades usando el nombre
'''
lista_preguntas=["¿Cuál es el símbolo atómico de el oro?\n\nA) Ar\nB) Or\nC) O\nD) Au\n",
                 "¿?\n\nA) \nB) \nC) \nD) \n",
                 "¿?\n\nA) \nB) \nC) \nD) \n",
                 "¿?\n\nA) \nB) \nC) \nD) \n",
                 "¿?\n\nA) \nB) \nC) \nD) \n",
                 "¿?\n\nA) \nB) \nC) \nD) \n",
                 "¿?\n\nA) \nB) \nC) \nD) \n",
                 "¿?\n\nA) \nB) \nC) \nD) \n",
                 "¿?\n\nA) \nB) \nC) \nD) \n",
                 "¿?\n\nA) \nB) \nC) \nD) \n",
                 "¿?\n\nA) \nB) \nC) \nD) \n",
                 "¿?\n\nA) \nB) \nC) \nD) \n",
                 "¿?\n\nA) \nB) \nC) \nD) \n",
                 "¿?\n\nA) \nB) \nC) \nD) \n",
                 "¿?\n\nA) \nB) \nC) \nD) \n"]
lista_respuestas=["D",
                  "A",
                  "A",
                  "A",
                  "A",
                  "A",
                  "A",
                  "A",
                  "A",
                  "A",
                  "A",
                  "A",
                  "A",
                  "A",
                  "A"]
opciones=["A","B","C","D"]
correcto=0
nombre=input("Bienvenido usuario\n\n¿Cómo te llamas?\n>>> ")

print(f"\nBienvenido a PREGUNTA2, {nombre}.\n")
print("\nEn este juego tendrás que contestar varias preguntas seleccionando la respuesta correcta.")
print("\nDeberás ingresar una letra mayúscula (A, B, C o D) para contestar las preguntas.")
input("\n¿Todo listo? (presiona enter)\n>>> ")

for i in range(0, len(lista_preguntas)):
    ciclo=True
    while ciclo:
        print(f"\n{i+1}.- {lista_preguntas[i]}")
        respuesta=input(">>> ")
        if respuesta in opciones:
            if respuesta==lista_respuestas[i]:
                correcto+=1
            ciclo=False
        else:
            print("\nPor favor, introduzca la letra de su elección en mayúsculas")

if correcto<(len(lista_preguntas)//2):
    print(f"\nLamentablemente, {nombre}, no has pasado el examen, tú calificacion es de {correcto} de {len(lista_preguntas)} preguntas")
else:
    print(f"\nFelicidades, {nombre}, has pasado el examen, tú calificacion es de {correcto} de {len(lista_preguntas)} preguntas")