""" 
Alumno: Ormeño, Gustavo
Correo: gustavo.ormeno.055@gmail.com

PARTE 1: Solución a resolver el siguiente ejercicio de programación

Iniciamos el programa sumando los sueldos asignados en cada mes
usando estructuras repetitivas y condicionales, para después sacar 
el promedio """

"""La variable sumaMeses almacenará y sumará los sueldos 
cobrados en cada mes"""
sumaMeses = 0

"""Usando el ciclo for que va desde el mes 1 (Enero) al mes 
12 (Diciembre) se van sumando los valores correspondientes a
cada mes según el enunciado del ejercicio."""
for i in range(1,13):
    
    if i>=1 and i<=6:
        "De Enero a Junio"
        sumaMeses= sumaMeses + 300
    elif i>=7 and i<=10:
        "De Julio a Octubre"
        sumaMeses= sumaMeses + 500
    else:
        "Noviembre y Diciembre"
        sumaMeses= sumaMeses + 700

print("PARTE 1: Ejercicio sobre el sueldo de Juan...")

"""Muestra el mensaje de los resultados del sueldo 
promedio de Juan"""
print("Los resultados del sueldo promedio de Juan son:")

"""Muestra la suma anual de sueldos."""
print("->La suma anual de sueldos es: USD $" + str(sumaMeses))

"""Calcula el sueldo promedio, dividiendo la suma de sueldos
por la cantidad de meses"""
sueldoPromedio = sumaMeses / 12

"""Muestra el sueldo promedio."""
print("->El sueldo promedio anual es: USD $" + str(sueldoPromedio))

"""A continuación resolveremos si el sueldo promedio de Juan o
cualquier otro sueldo promedio se encuentra dentro de un sueldo bajo,
alto o normal, determinado por el procedimiento estadoSueldo y
compuesto con la estructura condicional if."""
def estadoSueldo(sueldoPromedio):
    if sueldoPromedio < 300:
        print("->El sueldo promedio es bajo.")
    elif sueldoPromedio >= 300 and sueldoPromedio <=900:
        print("->El sueldo promedio es normal.")
    elif sueldoPromedio > 900:
        print("->El sueldo promedio es superior al normal.")


"""Invocamos l procedimiento estadoSueldo para determinar 
el tipo de salario alto, bajo o normal de Juan."""
estadoSueldo(float(sueldoPromedio))


"----------------------------------------------------------------------------------------------------"
"""Procedimientos utilizados en la APLICACIÓN FINAL para determinar si un sueldo
promedio, o el ingreso de sueldos y posterior cálculo de su promedio, son altos,
bajos o normales."""

"""Procedimiento que verifica el estado de un sueldo ingresado. Utilizado
en la aplicación que se ve al final del codigo"""
def verificarSueldoPromedio():
    nombre = input("-Ingrese el NOMBRE del que percibe el sueldo:")
    sueldoNumerico = False
    while sueldoNumerico != True:
        try:
            sueldo = float(input("-Ingrese el SUELDO PROMEDIO (EN NÚMEROS) en dolares:"))
            print("\n")
            print("(Rpta)--> Analizando el sueldo de " + nombre.upper() + ", con monto USD $" +
                  str(sueldo) + ", el resultado es que:")
            estadoSueldo(float(sueldo))           
            sueldoNumerico = True       
        except ValueError:
            print("ERROR: Solo se aceptan números.")    
        continue
    

"""Procedimiento que verifica el estado de varios sueldos ingresados. Utilizado
en la aplicación que se ve al final del código"""
def verificarSueldosIngresados():
    nombre = input("-Ingrese su el NOMBRE del que percibe el sueldo:")
    cantMeses = 0
    sumaMeses = 0
    
    """Lista que contiene los valores posibles para las cantidades de meses."""
    lista = ['2','3','4','5','6','7','8','9','10','11','12']
    cantMeses = input("-Ingrese la CANTIDAD DE MESES (EN NÚMEROS) dentro de 1 año (de 2 hasta 12): ")
    
    """Corrobora que se haya ingresado un numero del 2 al 12"""
    if cantMeses not in lista:
        cantMeses = 0

    if int(cantMeses) >=2 and int(cantMeses) <=12:
        
        i = 0
        while i != int(cantMeses):
            try:
                sueldoMensual= float(input("Ingrese el SUELDO DEL MES " + str(int(i+1)) + 
                                           " de " + cantMeses + " (EN NÚMEROS): "))   
                sumaMeses = sumaMeses + float(sueldoMensual)
                i = i + 1
            except ValueError:
                print("ERROR: Solo se aceptan números.")
            continue    
        
        sueldoPromedio = sumaMeses / float(cantMeses)
        print("\n")
        print("(Rpta)-->Analizando el sueldo de " + nombre.upper() + 
              " de acuerdo a los " + cantMeses + 
              " mes/es ingresado/s, el resultado es que:")
        """Muestra la suma anual de sueldos y el sualdo promedio."""
        print("->La suma anual de sueldos es: USD $" + str(sumaMeses))
        print("->El sueldo promedio de " + nombre.upper() + " es: USD $" + str(sueldoPromedio))

        """Calcula el sueldo promedio, dividiendo la suma de sueldos 
        por la cantidad de meses"""
        estadoSueldo(float(sueldoPromedio))
    
    else:
        print("ERROR: La cantidad de meses debe estar dentro de 1 año (de 2 a 12).")
    
"----------------------------------------------------------------------------------------------------"



"""Aplicación que permite determinar si un sueldo promedio, o una serie de 
sueldos (calculando su promedio) e ingresados en dólares, es alto, bajo 
o medio, según las pautas fijadas en el ejercicio."""

try:

    opcion = 0
    while (opcion != '3'):
        """Muestra los mensajes del menu."""
        print("\n")
        print("¿Desea determinar si un sueldo promedio es bajo, normal o " +
        "superior?")
        print("Opciones:")
        print(" (1) Verificar sueldo promedio.")
        print(" (2) Verificar sueldo promedio a través de sueldos por cantidad de meses.")
        print(" (3) Salir.")
        opcion = input("-->Ingrese opción (1, 2 o 3):")
        if opcion == "1" or opcion == "2" or opcion == "3":
            """Verifica que opción ha sido elegida."""
            if (int(opcion) == 1 ):
                verificarSueldoPromedio()
            elif (int(opcion) == 2 ):
                verificarSueldosIngresados()
        else:
            print("ERROR: Debe ingresar (en números) la opción 1, 2 o 3.")
except Exception as ex:
    print(ex)
    print("ERROR: Debe seguir las instrucciones.")