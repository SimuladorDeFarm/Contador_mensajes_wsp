from functions.crear_archivo import crear_archivo
from functions.es_fecha  import es_fecha
from functions.contar_dias import contar_dias

#abre el archivo con el chat, en un futuro debo modularizar el nombre
archivo = open("Chat.txt", "r")

#print(contar_dias())

# ask how many times someone speaked in one day
# pregunta cantas veces hablo cada uno un dia en concreto
def preguntar_dia(manu, tomas, jesus, dia):

    print("Dia ", dia)
    print("manu hablo: ", manu[dia])
    print("tomas hablo: ", tomas[dia])
    print("jesus hablo: ", jesus[dia])






def contar():
    
    personas = ["Tomás","Manuel Dios Campos", "Jesus Gomez", "Lukas Santi Exdev Linux Alumno Destacado Sangria"]
    #print(len(personas))



    tomas   = 0 #total de veces que hablo tomas
    manu    = 0 #total de veces que hablo manu
    jesus   = 0 ##total de veces que hablo jesus

    # *300 es el largo del array, debo cambiarlo por la cantidad de dias trasncurren

    j = len(personas)
    n = contar_dias()
    frecuencia = [[0] * n for _ in range(j)]

    tomas_frecuencia = [0] * n
    manu_frecuencia = [0] * n
    jesus_frecuencia = [0] * n

    frec_acumulada = [0] * n

    dia = "3" #inizializa dia con el numero del primer dia, debo estandarizarlo
    cantidad_dias = 0 #cuenta la cantidad de dias que van trasncurriendo
    fecha_anterior = "0" #guarda el numero del dia anterior
    i = 0 #i es la posicion de los arreglos

 
    linea = archivo.readline()
    # Verificar si la palabra "tomas" está en el string

    while linea:

        '''
        Algunos mensajes mandados son tan largos que usan la siguiente linea del
         archivo, asique en vez de aparecer fecha, hora, persona, mensaje solo parece
         mensaje ej: linea 22 del archivo, 
        '''
        fecha_v = linea.split(",") 
        fecha = fecha_v[0]

        '''
        para solucionar el problema anterior hay que identificar cuales son
        las linas reales y las que que contienen error, las lineas reales
        inician co  fecha en formato dd/mm/yyyy por lo que creamos una funcion
        que resive como parametro la fecha (todo el contenido del string hasta la primera ",") y en el caso de ser una linea real el programa se ejecuta, sino
        entonces no hace nada y pasa a la siguiente linea del archivo
        '''
        if es_fecha(fecha) == True:

            # Usar split para dividir el string por "/"            
            dia_anterior = dia 

            dia_vector = linea.split("/")
            dia = dia_vector[0] #guarda el dia ej 24/12/2024 -> dia = 24
            
            
            # el dia cambio cuando el dia actual y el anterior son diferentes
            if dia != dia_anterior: 
                i+=1
                #frec_acumulada[i] = frec_acumulada[i-1]
                #frec_acumulada[i-1] = frec_acumulada[i-1] / i
                
                cantidad_dias+=1
            
            z = 0
            while z < j :

                if  personas[z] in linea:
                    frecuencia[z][i] = frecuencia[z][i] +1   
                
                z+=1 



        #lee la siguiente linea
        linea = archivo.readline()

    archivo.close()

    for fila in frecuencia:
        print(fila)

    array_aux = [0] * n
    z = 0
    x = 0
    while z < j:
        x = 0
        while x < n:
            array_aux[x] = frecuencia[z][x]
            x+=1

        print(array_aux)
        crear_archivo(personas[z], array_aux, n)
        z+=1


contar()

