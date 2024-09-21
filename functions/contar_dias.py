from functions.es_fecha  import es_fecha




def contar_dias(nombreArchivo):

    archivo = open(f'{nombreArchivo}.txt', "r")

    dia = "3" #inizializa dia con el numero del primer dia, debo estandarizarlo
    cantidad_dias = 0 #cuenta la cantidad de dias que van trasncurriendo
    fecha_anterior = "0" #guarda el numero del dia anterior
    i = 0 #i es la posicion de los arreglos

 
    linea = archivo.readline()
    # Verificar si la palabra "tomas" está en el string

    while linea:

        fecha_v = linea.split(",") 
        fecha = fecha_v[0]

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
            

        #lee la siguiente linea
        linea = archivo.readline()

    archivo.close()
    
    return i + 1