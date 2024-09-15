import re
import pandas as pd


# leer una linea de archivo de texto
# analizar usuario
# analizar fecha

archivo = open("Chat.txt", "r")

def crear_archivo(nombre, array):

    df = pd.DataFrame({
        'Día': list(range(1, len(array) + 1)),  # Genera una lista de números de posición (1, 2, 3, ...)
        'Frecuencia': array
    })

    # Guardar el DataFrame en un archivo Excel
    df.to_excel('veces_jesus.xlsx', index=False)

    print("Archivo Excel creado exitosamente.")







def es_fecha(texto):
    # Definir el patrón de la expresión regular para el formato dd/mm/yyyy
    patron = r'^\d{2}/\d{2}/\d{4}$'
    patron2 = r'^\d{1}/\d{2}/\d{4}$'
    
    patron3 = r'^\d{1}/\d{1}/\d{4}$'
    patron4 = r'^\d{2}/\d{1}/\d{4}$'
    
    # Comprobar si el texto coincide con el patrón
    if re.match(patron, texto) or re.match(patron2, texto) or re.match(patron3, texto) or re.match(patron4, texto) :
        return True
    else:
        return False


def preguntar_dia(manu, tomas, jesus, dia):

    print("manu hablo: ", manu[dia])
    print("tomas hablo: ", tomas[dia])
    print("jesus hablo: ", jesus[dia])


def contar():

    tomas   = 0
    manu    = 0
    jesus   = 0

    veces_dia_tomas = [0] * 300
    veces_dia_manu = [0] * 300
    veces_dia_jesus = [0] * 300

    dia = "3"
    
    fecha_anterior = "0"
    i = 0
    #linea = "27/12/2023, 14:07 - Tomás : Hola"
    texto = "tomas"
     
    linea = archivo.readline()
    # Verificar si la palabra "tomas" está en el string
    cantidad_dias = 0



    while linea:


        fecha_v = linea.split(",")
        fecha = fecha_v[0]

        #print(fecha)
        #print(es_fecha(fecha))

        
        #print("dia =", cantidad_dias)


        if es_fecha(fecha) == True:

            # Usar split para dividir el string por "/"
            #fecha_anterior = fecha
            #print("fecha anterior  =", fecha_anterior)
            
            dia_anterior = dia

            dia_vector = linea.split("/")
            dia = dia_vector[0]
            


            #print(linea)
            #print("i = ", i)
            if dia != dia_anterior:
                i+=1
                cantidad_dias+=1


            if "Tomás" in linea:
                veces_dia_tomas[i] = veces_dia_tomas[i] + 1;
                tomas+=1
                #print("tomas = ", tomas)
            if "Manuel Dios Campos"   in linea:
                veces_dia_manu[i] = veces_dia_manu[i] + 1
                manu+=1
                #print("manu = ", manu)
            if "Jesus Gomez"   in linea:
                veces_dia_jesus[i] = veces_dia_jesus[i] + 1
                jesus+=1
            

            
            
        #else:
            #print(es_fecha(fecha))

        linea = archivo.readline()
    # Cierra el archivo después de leer
    
    archivo.close()

    #print("manuel = ", manu)
    #print("tomas = ", tomas)
    #print("jesus =", jesus )

    #print("veces_manu = ", veces_dia_manu)
    #print("veces_tomas = ", veces_dia_tomas)
    #print("veces jesus", veces_dia_jesus)


    crear_archivo(manu, veces_dia_jesus)
    #preguntar_dia(veces_dia_manu, veces_dia_tomas, veces_dia_jesus, 51)


contar()
'''
i = 0;
while i < 3:

    if i == 1:
        linea = "27/12/2023, 14:07 - Tomás : Hola"
    if i == 2:
        linea = "27/12/2023, 14:07 - Manuel Dios Campos : Hola"
    if i == 0:
        linea = "27/12/2023, 14:07 - Jesus Gomez : Hola"

    if "Tomás" in linea:
        print("tomas está aquí")
        tomas+=1
    if "Manuel Dios Campos"   in linea:
        print("manu esta aqui")
        manu+=1
    if "Jesus Gomez"   in linea:
        print("manu esta aqui")
        jesus+=1
            
    i+=1


print("manuel = ", manu)
print("tomas = ", tomas)
print("jesus =", jesus )

'''