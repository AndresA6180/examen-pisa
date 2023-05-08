archivo_Efinal= open ('texto.txt', 'w')
archivo_Efinal.write('Bienvenido a nuestro programa, \n este programa consiste de 3 quizzes diferentes de 10 preguntas cada uno. \n Pero en este caso tu eliges si quieres hacer uno de septimo, octavo, o noveno grado. \n Las repuestas deben darse solamente con numeros, no son necesarias las cifras, \n ni las comas en los numeros que son de 1000 para arriba y los decimales son con un punto. \n Para escribir una fraccion es asi: 8/9 Y al escribir ecuaciones no se debe poner espacios entre caracteres. Ejemplo: 6-y')
archivo_Efinal.close()

lectura = open('texto.txt','r')
linea = lectura.readline()

while len(linea) != 0:
    print(linea)
    linea = lectura.readline()
lectura.close


def grado7(quiz, puntos, pregunta):
    print('Eligio el grado 7')
    while quiz < 10:
        respuesta = input(lista7[pregunta])
        quiz = quiz + 1
        if respuesta == lista7[pregunta + 1]:
            print('Correcto')
            puntos = puntos + 1
            pregunta = pregunta + 2
        else:
            print('Incorrecto')
            print('Respuesta correcta: ' + lista7[pregunta + 1])
            pregunta = pregunta + 2
    return puntos
        

def grado8(quiz, puntos, pregunta):
    print('Eligio el grado 8')
    while quiz < 10:
        respuesta = input(lista8[pregunta])
        quiz = quiz + 1
        if respuesta == lista8[pregunta + 1]:
            print('Correcto')
            puntos = puntos + 1
            pregunta = pregunta + 2
        else:
            print('Incorrecto')
            print('Respuesta correcta: ' + lista8[pregunta + 1]) 
            pregunta = pregunta + 2
    return puntos
        
def grado9(quiz, puntos, pregunta):
    print('Eligio el grado 9')
    while quiz < 10:
        respuesta = input(lista9[pregunta])
        quiz = quiz + 1
        if respuesta == lista9[pregunta + 1]:
            print('Correcto')
            puntos = puntos + 1
            pregunta = pregunta + 2
        else:
            print('Incorrecto')
            print('Respuesta correcta: ' + lista9[pregunta + 1]) 
            pregunta = pregunta + 2
    return puntos
        
        

lista7 = ['¿Cual es el MCM (minimo comun multiplo) de 6 y 9? ', '18',
          '¿Cual es el resultado de 4/9 + 3/9? ', '7/9',
          'El resultado de 2.81 * 3.1 es: ', '8.711',
          'Resuelve: (8/5) / (10/9) Escribe tu respuesta como una fraccion ', '36/25',
          '¿Que fraccion es mayor, 7/5 o 8/2? ', '8/2',
          'Si 15 es el 30% de "y" , entonces "y" equivale a: ', '50',
          '¿Cual es el MCD (maximo comun divisor) de 9 y 18? ', '9',
          '¿Cuantos metros hay en 1.5 kilometros? ' , '1500',
          '((X + 5) * 3) / 10 = 6 | x = ? ' , '15',
          '¿Cuál es la probabilidad de sacar un 3 al lanzar un dado? ' , '1/6'
          ]

lista8 = ['3 + w = b, entonces w = ? ', 'b-3',
          'Un rectangulo tiene un largo de 5 y una altura de 7, ¿cual es su area? ', '35',
          'Resuelve: 2^6 ', '64',
          '¿Cual es la raiz cuadrada de 36? ', '6',
          'Calcula: 1/3 + 3/4 - 1/2 ', '7/12',
          'Un vendedor de frutas compró 200 guayabas a razón de 4 por $1.00 y 200 a 5 por $2.00.Luego las vendió a razón de 5 por $3.00. ¿Cuánto ganó? ', '110',
          'Un repostero uso media taza de azúcar para preparar dos docenas de galletas.¿Qué cantidad de azúcar necesitará para preparar cinco docenas? ', '5/4',
          'Los lados de un triángulo tienen longitudes de 6 cm, 10 cm y 11 cm. ¿Cuál será la longitud de los lados de un triángulo equilátero que tiene el mismo perímetro que el triángulo dado? ', '9',
          'Suponga que la operación a*b da como resultado la suma de los dígitos del producto de a y b. Por ejemplo, 4*7 = 10. Hallar (15*10)*(15 ⋅ 10). ', '9',
          'Resuelve 54^3 ', '157464'
          ]

lista9 = ['Determina las dos últimas cifras del número 2^222 ', '04',
          'La diferencia entre dos números es 30. Si añadimos 5 a ambos, el mayor ahora resulta ser el triple del menor. ¿Cuál era el menor al principio? ', '10',
          'Juan tenía $500; le dio el 30 % a su hermano y gastó el 15 % del resto. ¿Cuánto dinero le queda? ', '297.50',
          'Una parcela rectangular de 30 m por 40 m está rodeada por un paseo de 5 m de ancho. ¿Cuál es el área del paseo? ', '800',
          'La base de un rectángulo excede en 4 cm a su altura. Si su perímetro es de 40 cm. Calcula su área conociendo que las longitudes de sus lados son números enteros. ', '96',
          'Tenemos 400 cubitos de 1 cm de arista con los que hacemos el mayor cubo posible. ¿Cuántos cubitos nos sobran? ', '57',
          'Dos postes de 3 m y 7 m están separados 15 m. La altura de la intersección de las líneas que unen la cima de cada poste con la base del poste opuesto es de: ', '2.1',
          'Mi edad es igual a la raíz cuadrada del año de mi nacimiento. ¿Cuántos años cumpliré en el 2005? ', '69',
          'Si 3x + y = 2; x – 4y = 5, entonces si 8x – 6y = z, ¿cuál es el valor de z? ', '14',
          'El precio inicial de un producto es de $120. Por razones económicas aumenta en un 40 %. Al cabo de seis meses de este aumento se disminuye su precio en $25. ¿Cuál es el precio final del producto? ', '126'
          ]

nombre = input('Ingresa tu nombre: ')
edad = int(input('Ingresa tu edad: '))
grado = int(input('Ingresa tu grado. Puede ser 7, 8 o 9: '))
puntos = 0
pregunta = 0
quiz = 0



if grado == 7:
    puntos7 = grado7(quiz, puntos, pregunta)
    if puntos7 <= 4:
        print('Te recomendamos ir a asesorias,', nombre, ', obtuviste', puntos7, 'punto(s)')
    elif puntos7 > 4 and puntos7 <= 7:
        print('Estudia mas,', nombre, ', obtuviste', puntos7, 'punto(s)')
    elif puntos7 > 7:
        print('Felicidades', nombre, ', obtuviste', puntos7, 'punto(s)')
elif grado == 8:
    puntos8 = grado8(quiz, puntos, pregunta)
    if puntos8 <= 4:
        print('Te recomendamos ir a asesorias,', nombre, ', obtuviste', puntos8, 'punto(s)')
    elif puntos8 > 4 and puntos8 <= 7:
        print('Estudia mas,', nombre, ', obtuviste', puntos8, 'punto(s)')
    elif puntos8 > 7:
        print('Felicidades', nombre, ', obtuviste', puntos8, 'punto(s)')
elif grado == 9:
    puntos9 = grado9(quiz, puntos, pregunta)
    if puntos9 <= 4:
        print('Te recomendamos ir a asesorias,', nombre, ', obtuviste', puntos9, 'punto(s)')
    elif puntos9 > 4 and puntos9 <= 7:
        print('Estudia mas,', nombre, ', obtuviste', puntos9, 'punto(s)')
    elif puntos9 > 7:
        print('Felicidades', nombre, ', obtuviste', puntos9, 'punto(s)')
else:
    print('Elija un grado valido')


    