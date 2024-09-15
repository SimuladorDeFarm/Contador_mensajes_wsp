from functions.crear_archivo import crear_archivo
from functions.es_fecha  import es_fecha


#abre el archivo con el chat, en un futuro debo modularizar el nombre
archivo = open("Chat.txt", "r")



# ask how many times someone speaked in one day
# pregunta cantas veces hablo cada uno un dia en concreto
def preguntar_dia(manu, tomas, jesus, dia):

    print("Dia ", dia)
    print("manu hablo: ", manu[dia])
    print("tomas hablo: ", tomas[dia])
    print("jesus hablo: ", jesus[dia])



def contar():


    tomas   = 0 #total de veces que hablo tomas
    manu    = 0 #total de veces que hablo manu
    jesus   = 0 ##total de veces que hablo jesus

    # *300 es el largo del array, debo cambiarlo por la cantidad de dias trasncurren
    tomas_frecuencia = [0] * 249
    manu_frecuencia = [0] * 249
    jesus_frecuencia = [0] * 249

    frec_acumulada = [0] *249

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

            #en el caso de machear un nombre guarda la frecuencia del susodicho
            if "Tomás" in linea:
                tomas_frecuencia[i] = tomas_frecuencia[i] + 1;
                tomas+=1
                #print("tomas = ", tomas)
            if "Manuel Dios Campos"   in linea:
                manu_frecuencia[i] = manu_frecuencia[i] + 1
                manu+=1
                #print("manu = ", manu)
            if "Jesus Gomez"   in linea:
                frec_acumulada[i] = frec_acumulada[i] + 1
                jesus_frecuencia[i] = jesus_frecuencia[i] + 1
                jesus+=1
            

        #lee la siguiente linea
        linea = archivo.readline()

    archivo.close()
    # Cierra el archivo después de leer
    
    #frec_acumulada[i] = frec_acumulada[i] / (i +1)


    #crear_archivo("Manu     ", manu_frecuencia  )
    #crear_archivo("Tomas    ", tomas_frecuencia )
    #crear_archivo("Jesus_acumulado    ", frec_acumulada )

    #preguntar_dia(manu_frecuencia, tomas_frecuencia, jesus_frecuencia, 51)


contar()
