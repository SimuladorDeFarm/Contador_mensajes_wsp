import re #comprueba si el texto contiene un patron
import pandas as pd #genera archico xlsx


archivo = open("Chat.txt", "r")

def crear_archivo(nombre, array):

    df = pd.DataFrame({
        'Día': list(range(1, len(array) + 1)),  # Genera una lista de números de posición (1, 2, 3, ...)
        'Frecuencia': array
    })

    # Guardar el DataFrame en un archivo Excel
    df.to_excel(f'{nombre}_frecuencia.xlsx', index=False)

    print("Archivo Excel creado exitosamente.")




def es_fecha(texto):
    # define the patron of regular expresion for a dd/mm/yyyy format
    # Definir el patrón de la expresión regular para el formato dd/mm/yyyy
    patron1 = r'^\d{2}/\d{2}/\d{4}$' # dia con 2 digitos, mes con 2 digitos
    patron2 = r'^\d{1}/\d{2}/\d{4}$' # dia con 1 digitos, mes con 2 digitos
    
    patron3 = r'^\d{1}/\d{1}/\d{4}$' # dia con 1 digitos, mes con 1 digitos
    patron4 = r'^\d{2}/\d{1}/\d{4}$' # dia con 2 digitos, mes con 1 digitos
    
    # Comprobar si el texto coincide todas las convianciones de patrones
    if re.match(patron1, texto) or re.match(patron2, texto) or re.match(patron3, texto) or re.match(patron4, texto) :
        return True
    else:
        return False

# ask how many times someone speaked in one day
# pregunta cantas veces hablo cada uno un dia en concreto
def preguntar_dia(manu, tomas, jesus, dia):

    print("manu hablo: ", manu[dia])
    print("tomas hablo: ", tomas[dia])
    print("jesus hablo: ", jesus[dia])



def contar():

    tomas   = 0
    manu    = 0
    jesus   = 0

    tomas_frecuencia = [0] * 300
    manu_frecuencia = [0] * 300
    jesus_frecuencia = [0] * 300

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
                tomas_frecuencia[i] = tomas_frecuencia[i] + 1;
                tomas+=1
                #print("tomas = ", tomas)
            if "Manuel Dios Campos"   in linea:
                manu_frecuencia[i] = manu_frecuencia[i] + 1
                manu+=1
                #print("manu = ", manu)
            if "Jesus Gomez"   in linea:
                jesus_frecuencia[i] = jesus_frecuencia[i] + 1
                jesus+=1
            

            
            
        #else:
            #print(es_fecha(fecha))

        linea = archivo.readline()
    # Cierra el archivo después de leer
    
    archivo.close()

    #print("manuel = ", manu)
    #print("tomas = ", tomas)
    #print("jesus =", jesus )

    #print("veces_manu = ", manu_frecuencia)
    #print("veces_tomas = ", tomas_frecuencia)
    #print("veces jesus", jesus_frecuencia)


    crear_archivo("jesus", jesus_frecuencia)
    #preguntar_dia(manu_frecuencia, tomas_frecuencia, jesus_frecuencia, 51)


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