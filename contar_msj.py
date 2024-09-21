from functions.crear_archivo    import crear_archivo
from functions.es_fecha         import es_fecha
from functions.contar_dias      import contar_dias
from functions.crear_archivo    import recorre_crear_archivo
from functions.recoger_dia      import recoger_dia
from functions.recoger_fecha    import recoger_fecha


#agrega el nombre del archivo sin la extencion
#agrega el nombre de los integrantes del grupo (no uses emojis)

nombreArchivo = "Chat"
personas = ["Tomás","Manuel Dios Campos", "Jesus Gomez"]

#abre el archivo con el chat, en un futuro debo modularizar el nombre
archivo = open(f'{nombreArchivo}.txt', "r")

#print(contar_dias())

# ask how many times someone speaked in one day
# pregunta cantas veces hablo cada uno un dia en concreto


def contar():
    
    #print(len(personas))


    j = len(personas)
    n = contar_dias(nombreArchivo)
    frecuencia = [[0] * n for _ in range(j)] #vector de 2 dimenciones
    frecuencia_total = [0] * n

    tomas_frecuencia = [0] * n
    manu_frecuencia = [0] * n
    jesus_frecuencia = [0] * n

    frec_acumulada = [0] * n

    dia = "3" #inizializa dia con el numero del primer dia, debo estandarizarlo
    cantidad_dias = 0 #cuenta la cantidad de dias que van trasncurriendo
    fecha_anterior = "0" #guarda el numero del dia anterior
    i = 0 #i es la posicion de los arreglos

 
    linea = archivo.readline()

    while linea:

        '''
        Algunos mensajes mandados son tan largos que usan la siguiente linea del
         archivo, asique en vez de aparecer fecha, hora, persona, mensaje solo parece
         mensaje ej: linea 22 del archivo, 
        '''

        '''
        para solucionar el problema anterior hay que identificar cuales son
        las linas reales y las que que contienen error, las lineas reales
        inician con  fecha en formato dd/mm/yyyy por lo que creamos una funcion
        que resive como parametro la fecha (todo el contenido del string hasta la primera ",") y en el caso de ser una linea real el programa se ejecuta, sino
        entonces no hace nada y pasa a la siguiente linea del archivo

        ej: 30/12/2024              -> se ejecuta
            todos tontos menos yo   -> No se ejecuta y pasa a la siguiente linea 
        '''
        #fecha_v = linea.split(",") 
        fecha = recoger_fecha(linea)
        
        if es_fecha(fecha) == True:

            # Usar split para dividir el string por "/"            
            dia_anterior = dia 
            dia = recoger_dia(linea)
            
            
            # el dia cambio cuando el dia actual y el anterior son diferentes
            if dia != dia_anterior: 
                i+=1
                #frec_acumulada[i] = frec_acumulada[i-1]
                #frec_acumulada[i-1] = frec_acumulada[i-1] / i
                 
                cantidad_dias+=1
            
            z = 0
            while z < j :

                if  personas[z] in linea:
                    frecuencia[z][i] = frecuencia[z][i] + 1   
                    frecuencia_total[i] = frecuencia_total[i] + 1
                    #print(i)
                    #print(n)
                z+=1 




        #lee la siguiente linea
        linea = archivo.readline()

    archivo.close()

    print(frecuencia_total)
    

    recorre_crear_archivo(personas, frecuencia, j, n)
    crear_archivo("frecuencia_total", frecuencia_total, n)

contar()

