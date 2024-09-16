import pandas as pd #genera archico xlsx


def crear_archivo(nombre, array, n):

    df = pd.DataFrame({
        'Día': list(range(1, n + 1)),  # Genera una lista de números de posición (1, 2, 3, ...)
        'Frecuencia': array
    })

    # Guardar el DataFrame en un archivo Excel
    df.to_excel(f'./tablas/{nombre}_frecuencia.xlsx', index=False)

    print("Archivo Excel creado exitosamente.")
