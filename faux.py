import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def stats_por_unidad(e, variables):
    """
    Calcula un resumen estadístico agrupado por unidad para todos los sujetos en un ejercicio dado.
    
    Parámetros:
    e (int): Número del ejercicio.
    variables (dict): Diccionario con las variables de datos.

    Retorna:
    pd.DataFrame: DataFrame con la media agrupada por unidad para cada sensor y un resumen estadístico.
    """

    sujetos = range(1, 6)  # Consideramos 5 sujetos
    unidades = range(1, 6)  # Unidades del 1 al 5
    columnas = ['gyr_x', 'gyr_y', 'gyr_z', 'acc_x', 'acc_y', 'acc_z', 'mag_x', 'mag_y', 'mag_z']
    resultados = []

    for u in unidades:
        datos_por_unidad = {col: [] for col in columnas}

        for s in sujetos:
            var_name = f's{s}e{e}u{u}'
            if var_name in variables:
                data = variables[var_name]
                for col in columnas:
                    # Agregar datos del sensor para esta unidad y sujeto
                    datos_por_unidad[col].extend(data[col])

        for col in columnas:
            valores = datos_por_unidad[col]
            media = pd.Series(valores).mean()
            mediana = pd.Series(valores).median()
            std_dev = pd.Series(valores).std()
            resultados.append({
                'Unidad': u,
                'Variable': col,
                'Media': media,
                'Mediana': mediana,
                'Desviación estándar': std_dev
            })

    df_resultados = pd.DataFrame(resultados)
    return df_resultados



def plot_dens(s, e, variables):
    """
    Genera una gráfica con una matriz 3x5 mostrando la densidad (density plot)
    para las señales de los sensores.

    Parámetros:
    s (int): Número del sujeto.
    e (int): Número del ejercicio.
    variables (dict): Diccionario con las variables de datos.
    """

    # Paleta de colores personalizada
    colores = {'acc_x': '#003f5c', 'acc_y': '#2f4b7c', 'acc_z': '#665191',
               'gyr_x': '#a05195', 'gyr_y': '#d45087', 'gyr_z': '#f95d6a',
               'mag_x': '#ff7c43', 'mag_y': '#ffa600', 'mag_z': '#ffd026'}

    fig, axes = plt.subplots(3, 5, figsize=(20, 12), sharex=False, sharey=False)
    fig.suptitle(f'Sujeto {s} - Ejercicio {e} (template)', fontsize=20)

    sensor_axes = ['acc', 'gyr', 'mag']
    units = range(1, 6)

    for i, sensor in enumerate(sensor_axes):
        for j, u in enumerate(units):
            var_name = f's{s}e{e}u{u}'
            data = variables[var_name]

            ax = axes[i, j]

            # Graficar densidad con colores personalizados
            sns.kdeplot(data[f'{sensor}_x'], ax=ax, label=f'{sensor}_x', fill=True, alpha=0.5, color=colores[f'{sensor}_x'])
            sns.kdeplot(data[f'{sensor}_y'], ax=ax, label=f'{sensor}_y', fill=True, alpha=0.5, color=colores[f'{sensor}_y'])
            sns.kdeplot(data[f'{sensor}_z'], ax=ax, label=f'{sensor}_z', fill=True, alpha=0.5, color=colores[f'{sensor}_z'])

            if i == 0:
                ax.set_title(f'Unidad {u}', fontsize=12)
            if j == 0:
                ax.set_ylabel(f'{sensor.upper()}', fontsize=12)
            ax.legend(fontsize=8)
            ax.grid(True)

    plt.tight_layout(rect=[0, 0, 1, 0.95])
    plt.show()



def plot_dist(s, e, variables):
    """
    Genera una gráfica con una matriz 3x5 para las señales de los sensores.
    
    Parámetros:
    s (int): Número del sujeto.
    e (int): Número del ejercicio.
    variables (dict): Diccionario con las variables de datos.
    """

    # Paleta de colores personalizada
    colores = {'acc_x': '#003f5c', 'acc_y': '#2f4b7c', 'acc_z': '#665191',
               'gyr_x': '#a05195', 'gyr_y': '#d45087', 'gyr_z': '#f95d6a',
               'mag_x': '#ff7c43', 'mag_y': '#ffa600', 'mag_z': '#ffd026'}

    fig, axes = plt.subplots(3, 5, figsize=(20, 12), sharex=True, sharey=True)
    fig.suptitle(f'Sujeto {s} - Ejercicio {e} (template)', fontsize=20)

    sensor_axes = ['acc', 'gyr', 'mag']
    units = range(1, 6)

    for i, sensor in enumerate(sensor_axes):
        for j, u in enumerate(units):
            var_name = f's{s}e{e}u{u}'
            data = variables[var_name]

            time = data['time index']

            ax = axes[i, j]
            ax.plot(time, data[f'{sensor}_x'], label=f'{sensor}_x', color=colores[f'{sensor}_x'])
            ax.plot(time, data[f'{sensor}_y'], label=f'{sensor}_y', color=colores[f'{sensor}_y'])
            ax.plot(time, data[f'{sensor}_z'], label=f'{sensor}_z', color=colores[f'{sensor}_z'])

            if i == 0:
                ax.set_title(f'Unidad {u}', fontsize=12)
            if j == 0:
                ax.set_ylabel(f'{sensor.upper()}', fontsize=12)
            ax.grid(True)
            ax.legend(fontsize=8)

    plt.tight_layout(rect=[0, 0, 1, 0.95])
    plt.show()


def plot_scatter(s, e, u, variables):
    """
    Genera un scatter plot matrix (9x9) para las variables de una unidad específica,
    con datos de un sujeto y ejercicio determinados.

    Parámetros:
    s (int): Número del sujeto.
    e (int): Número del ejercicio.
    u (int): Número de la unidad.
    variables (dict): Diccionario con las variables de datos (DataFrames).
    """

    # Identificar la clave correspondiente al sujeto, ejercicio y unidad
    var_name = f's{s}e{e}u{u}'
    
    # Extraer los datos correspondientes del diccionario
    if var_name not in variables:
        print(f"No se encontraron datos para: Sujeto {s}, Ejercicio {e}, Unidad {u}")
        return
    
    data = variables[var_name]

    # Comprobación para asegurarse de que las columnas necesarias están presentes
    expected_columns = ['acc_x', 'acc_y', 'acc_z', 'gyr_x', 'gyr_y', 'gyr_z', 'mag_x', 'mag_y', 'mag_z']
    if not all(col in data.columns for col in expected_columns):
        print(f"Los datos de la unidad {u} no contienen todas las columnas esperadas.")
        return

    # Crear el scatter plot matrix
    plt.figure(figsize=(20, 20))
    scatter_matrix = pd.plotting.scatter_matrix(
        data[expected_columns],
        alpha=0.6,
        figsize=(20, 20),
        diagonal="hist",  # Mostrar histogramas en la diagonal
        color="#003f5c",
        grid=True
    )

    # Ajustar los títulos y rotaciones para mejor visualización
    for ax in scatter_matrix.ravel():
        ax.set_xlabel(ax.get_xlabel(), fontsize=10, rotation=45)
        ax.set_ylabel(ax.get_ylabel(), fontsize=10, rotation=0)

    plt.suptitle(f'Scatter Plot Matrix: Sujeto {s} - Ejercicio {e} - Unidad {u}', fontsize=20)
    plt.tight_layout(rect=[0, 0, 1, 0.95])
    plt.show()
