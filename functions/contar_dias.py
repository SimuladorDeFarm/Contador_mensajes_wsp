from es_fecha  import es_fecha

archivo = open("Chat.txt", "r")



def contar_dias():
    
    i = 0
    dia = "3"
    
    
    linea = archivo.readline()

    fecha_v = linea.split(",") 
    fecha = fecha_v[0]

    while linea:    

        if es_fecha(fecha) == True:

            dia_anterior = dia 

            dia_vector = linea.split("/")
            dia = dia_vector[0] #guarda el dia ej 24/12/2024 -> dia = 24            

            if dia != dia_anterior: 
                i+=1
                #frec_acumulada[i] = frec_acumulada[i-1]
                #frec_acumulada[i-1] = frec_acumulada[i-1] / i
                
        linea = archivo.readline()
    
    return i 