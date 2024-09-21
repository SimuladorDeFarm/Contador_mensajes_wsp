import pandas as pd #genera archico xlsx

def crear_archivo(nombre, array, n):

    df = pd.DataFrame({
        'Día': list(range(1, n + 1)),  # Genera una lista de números de posición (1, 2, 3, ...)
        'Frecuencia': array
    })

    # Guardar el DataFrame en un archivo Excel
    df.to_excel(f'./tablas/{nombre}_frecuencia.xlsx', index=False)

    print("Archivo Excel creado exitosamente.")


def recorre_crear_archivo(personas, frecuencia, j, n):

    array_aux = [0] * n
    z = 0
    x = 0
    while z < j:
        x = 0
        while x < n:
            array_aux[x] = frecuencia[z][x]
            x+=1

        #print(array_aux)
        crear_archivo(personas[z], array_aux, n)
        z+=1

