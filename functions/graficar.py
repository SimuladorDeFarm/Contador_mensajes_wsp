import matplotlib.pyplot as plt


def graficar(y):
    # Suponiendo que este es tu vector de datos para el eje Y
     

    # El eje X será el índice de cada elemento en el vector Y
    x = range(len(y))

    # Crear el gráfico
    plt.plot(x, y, marker='o')

    # Etiquetas de los ejes
    plt.xlabel('Posiciones (índice)')
    plt.ylabel('Valores (eje Y)')

    # Título del gráfico
    plt.title('Gráfico de X vs Y')

    # Mostrar el gráfico
    plt.show()