import random
import csv

def sueldos_aleatotorios(sueldos_trabajadores):

    for i in range(10):
        sueldos_trabajadores.append(random.randrange(300000,2500000))

def mayor_sueldo(sueldos_trabajadores):
    
    mayor_sueldo = 0
    for cifra in range (10):
        if(sueldos_trabajadores[cifra])>mayor_sueldo:
            mayor_sueldo = sueldos_trabajadores[cifra]
    return mayor_sueldo

def menor_sueldo(sueldos_trabajadores):
    
    menor_sueldo = sueldos_trabajadores[0]
    for cifra in range (10):
        if(sueldos_trabajadores[cifra])<menor_sueldo:
            menor_sueldo = sueldos_trabajadores[cifra]
    return menor_sueldo

def suma_sueldos(sueldos_trabajadores):
    
    acumulacion_sueldos = 0
    for cifra in range (10):
        acumulacion_sueldos = acumulacion_sueldos + sueldos_trabajadores[cifra]
    return acumulacion_sueldos

def multiplicacion_sueldos(sueldos_trabajadores):
    
    multiplicacion_sueldos = 1
    for cifra in range (10):
        multiplicacion_sueldos = multiplicacion_sueldos * sueldos_trabajadores[cifra]
    return multiplicacion_sueldos

def promedio_sueldos(sueldos_trabajadores):   
    
    promedio_sueldos = suma_sueldos(sueldos_trabajadores) / 10
    return promedio_sueldos

def media_geometrica(sueldos_trabajadores):

    media_geometrica = (multiplicacion_sueldos(sueldos_trabajadores)) ** (1/10)
    return media_geometrica

def mostrar_estadisticas(sueldos_trabajadores):

    sueldo_mayor = mayor_sueldo(sueldos_trabajadores)
    sueldo_menor = menor_sueldo(sueldos_trabajadores)
    sueldo_promedio = promedio_sueldos(sueldos_trabajadores)
    geometrica_media = media_geometrica(sueldos_trabajadores)
    print(f"El Sueldo más alto es: {sueldo_mayor}\nEl Sueldo más Bajo es: {sueldo_menor}\nEl Promedio de Sueldos es: {sueldo_promedio}\nLa Media Geométrica es: {geometrica_media}")

def sueldos_menor_800k(trabajadores,sueldos_trabajadores):
    
    contador = 0
    imprimir = "" # String vacío que permite ir almacenando valores para poder formatearlo y que salgan ordenados
    for cifra in range (10):
        if(sueldos_trabajadores[cifra]<800000):
            imprimir = imprimir + trabajadores[cifra] + "\t\t" + str(sueldos_trabajadores[cifra]) + "\n"
            contador = contador + 1
    print(f"Sueldos menores a $800.000\tTOTAL:{contador}\n")
    print(imprimir)

def sueldos_800k_2000k(trabajadores,sueldos_trabajadores):
    
    contador = 0
    imprimir = "" # String vacío que permite ir almacenando valores para poder formatearlo y que salgan ordenados
    for cifra in range (10):
        if(sueldos_trabajadores[cifra]>=800000 and sueldos_trabajadores[cifra]<=2000000):
            imprimir = imprimir + trabajadores[cifra] + "\t\t" + str(sueldos_trabajadores[cifra]) + "\n"
            contador = contador + 1
    print(f"Sueldos entre $800.000 y $2.000.000\tTOTAL:{contador}\n")
    print(imprimir)

def sueldos_mayor_2000k(trabajadores,sueldos_trabajadores):
    
    contador = 0
    imprimir = "" # String vacío que permite ir almacenando valores para poder formatearlo y que salgan ordenados
    for cifra in range (10):
        if(sueldos_trabajadores[cifra]>2000000):
            imprimir = imprimir + trabajadores[cifra] + "\t\t" + str(sueldos_trabajadores[cifra]) + "\n"
            contador = contador + 1
    print(f"Sueldos mayores a $2.000.000\tTOTAL:{contador}\n")
    print(imprimir)

def clasificar_sueldos(trabajadores,sueldos_trabajadores):

    sueldos_menor_800k(trabajadores,sueldos_trabajadores)
    sueldos_800k_2000k(trabajadores,sueldos_trabajadores)
    sueldos_mayor_2000k(trabajadores,sueldos_trabajadores)
    print(f"TOTAL SUELDOS:\t\t${suma_sueldos(sueldos_trabajadores)}")

def descuento_salud(sueldo):

    descuento_salud = (sueldo*7)/100
    return descuento_salud

def descuento_afp(sueldo):

    descuento_afp = (sueldo*12)/100
    return descuento_afp

def reporte_sueldos(trabajadores,sueldos_trabajadores):

    imprimir = "" # String vacío que permite ir almacenando valores para poder formatearlo y que salgan ordenados
    for cifra in range (10):
        salud_descuento = descuento_salud(sueldos_trabajadores[cifra])
        afp_descuento = descuento_afp(sueldos_trabajadores[cifra])
        sueldo_liquido = sueldos_trabajadores[cifra] - (salud_descuento + afp_descuento)
        imprimir = imprimir + trabajadores[cifra] + "\t\t"+ str(sueldos_trabajadores[cifra]) + "\t\t" + str(salud_descuento) + "\t\t" + str(afp_descuento) + "\t\t" + str(sueldo_liquido) + "\n"
    print(f"Nombre empleado\t\tSueldo Base\tDescuento Salud\t\tDescuento AFP\t\tSueldo Líquido\n")
    print(imprimir)

    with open('CRISTIAN_VALENZUELA_ET.txt', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(imprimir)

trabajadores = ["Juan Perez","Maria Garcia","Carlos Lopez","Ana Martinez","Pedro Rodriguez","Laura Hernandez","Miguel Sanchez","Isabel Gomez","Francisco Diaz","Elena Fernandez"]
sueldos_trabajadores = []

try:
    while(True):
        print("\nBienvenido al Sistema de Análisis de Datos de Trabajadores\n")
        opcion_menu = int(input("Por Favor Seleccione una opción:\n1) Asignar Sueldos Aleatorios.\n2) Clasificar Sueldos.\n3) Ver Estadísticas.\n4) Reporte de Sueldos.\n5) Salir del Programa.\n"))
        while (opcion_menu<1 or opcion_menu>5): # Validación números ingresados como opción del menú
                print("Por Favor Ingrese una opción Válida\n")
                opcion_menu =  int(input("Por Favor Seleccione una opción:\n1) Asignar Sueldos Aleatorios.\n2) Clasificar Sueldos.\n3) Ver Estadísticas.\n4) Reporte de Sueldos.\n5) Salir del Programa.\n"))
        if(opcion_menu==1):
            sueldos_aleatotorios(sueldos_trabajadores)
        if(opcion_menu==2):
            clasificar_sueldos(trabajadores,sueldos_trabajadores)
        if(opcion_menu==3):
            mostrar_estadisticas(sueldos_trabajadores)
        if(opcion_menu==4):
            reporte_sueldos(trabajadores,sueldos_trabajadores)
        if(opcion_menu)==5:
            print(f"Finalizando programa…\nDesarrollado por Cristian Valenzuela\nRUT 19.490.111-9")
            break
except ValueError:
    print("El tipo de datos ingresado, no es válido.")

