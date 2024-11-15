Valentina Cabrera y Valentina Bustamante

# Ejercicio 1

## Modelos de Clasificación (30%)

Considere el conjunto de datos **Satisfacción de Clientes**. Implemente la versión de clasificación para cada uno de los modelos estudiados en clases, y prediga la variable respuesta, probabilidad para la variable *target* (última columna). Construir una tabla de error que contenga las métricas usuales de clasificación: **precision**, **recall**, **f1-score**, **AUC**. Además, agregue matrices de confusión (ver `confusion_matrix`) y curvas ROC (ver `plot_roc`). Los resultados deben estar registrados en una tabla de error (ver Tabla 1) que resuma cada *score* obtenido por modelo implementado.

### Descripción de Tipos de Variables
- Calcular número de observaciones, media, desviación estándar, mínimo, máximo, cuartiles.
- Realizar conteo de datos faltantes y su porcentaje.
- Generar histograma o diagrama de barras para la variable respuesta e independientes según corresponda.
- Seleccionar un mínimo de 10 variables independientes para este análisis.
- Análisis de simetría, datos atípicos y dispersión mediante `boxplot()`.
- Análisis bivariado. Trazado de `scatterplot()` y `regplot()` para un mínimo de 10 pares de variables explicativas. En cada figura agregar un análisis y descripción.

### Imputación y Reducción de Dimensionalidad
- Realizar imputación de datos faltantes por medio de **Imputación Iterativa Múltiple**.
- Reducción de dimensionalidad eliminando columnas altamente correlacionadas usando el **Variance Inflation Factor (VIF)**. Para esto se recomienda usar la librería `variance_inflation_factor()`.
  - Un VIF ≥ 10 indica alta multicolinealidad entre la variable independiente correspondiente y las demás.
  - **Recomendación**: Eliminar una columna a la vez, la que tenga el máximo VIF ≥ 10. Luego recalcular el VIF e identificar nuevas columnas con VIF ≥ 10 hasta que todos los valores de VIF sean < 10.
  - Justificar las variables que se eliminan. Se puede proponer una metodología alternativa de reducción de dimensionalidad.

### Tabla de Modelos de Clasificación

| Modelo                        | Precision | Recall | Accuracy | F1-Score | AUC |
|------------------------------|-----------|--------|----------|----------|-----|
| Clasificación Bayesiana      | ...       | ...    | ...      | ...      | ... |
| K-NN                         | ...       | ...    | ...      | ...      | ... |
| L1/L2 Penalty Logistic Regression | ... | ...    | ...      | ...      | ... |
| Random Forest                | ...       | ...    | ...      | ...      | ... |
| XGBoost                      | ...       | ...    | ...      | ...      | ... |
| SVM                          | ...       | ...    | ...      | ...      | ... |

*Cuadro 1: Modelo de clasificación para predicción de satisfacción de clientes.*


# Ejercicio 2

## Modelos de Regresión (70%)

1. **Contexto del problema**: Para realizar predicción de series de tiempo, en la validación cruzada es crucial considerar el orden natural del tiempo. Por ejemplo, usted desearía predecir 7 días futuros, con 31 datos históricos de un mes, no lo contrario. No requerimos predecir el pasado, porque este ya es conocido. Con base en esto, es necesario construir manualmente una validación cruzada, que no realice ninguna desorganización no natural de los pliegues de entrenamiento, validación y prueba, respetando el orden temporal.

2. **Análisis Exploratorio**: Considere cada “subject, exercise, unit (archivos: si, ei, ui)” del dataset suministrado (ver **Fisioterapia Dataset**) y realice un análisis exploratorio de datos sobre cada serie de tiempo correspondiente a "magnetic field, angular rate, acceleration" (ver **Time Series Forecasting: Exploratory Data Analysis**).

3. **Definir funciones de división de datos**: Defina funciones en Python para dividir el conjunto de datos en entrenamiento, validación y test con base en las Figuras 1-3. Observe que en las tres figuras aparecen ejemplos para τ = 1, 2, 3; debe extenderlo hasta los diferentes horizontes: τ = 7, 14, 21, 28. Al final, debe unir las predicciones de cada punto para obtener el horizonte predicho completo de τ días. Antes de construir los pliegues, separe de la serie los últimos τ = 7, 14, 21, 28 datos. El objetivo es que cuando obtenga el modelo final, pueda dibujar este dataset de test separado al inicio, junto a su predicción, y los datos de entrenamiento (*train*) junto a su predicción.

4. **Implementación de pliegues personalizados**: Nótese que `TimeSeriesSplit` no es una librería que funcione aquí, debido a que los pliegues que entrega no coinciden con los de las Figuras 1-3 que son los solicitados en este examen, por favor, no intente usarla, implemente sus propios pliegues. Al final de la construcción de la función que entrega dichas divisiones, debe visualizarlas dentro de su JBook usando las funciones de Python adecuadas para esto. El objetivo es verificar y confirmar que ha construido adecuadamente los pliegues de entrenamiento, validación y prueba, y que sus figuras coinciden con las Figuras 1-3.

5. **Ajuste de modelos predictivos**: Para cada conjunto de parámetros, ajuste cada modelo predictivo en el conjunto de entrenamiento y, dentro de sus iteraciones de búsqueda, evalúe su modelo en el conjunto de validación usando las siguientes métricas: **MAPE, MAE, RMSE, MSE y el R²**.

6. **Tabla de métricas del residuo**: Realice una tabla donde resuma los *scores* obtenidos para el residual (residuo en el conjunto de entrenamiento) y agregue además las respectivas pruebas de hipótesis para independencia y normalidad. Para esto, usando Pandas, construya una tabla con las siguientes columnas: **MAPE, MAE, RMSE, MSE, R², LJung-Box test (p-value), Jarque-Bera (p-value)**, y agregue las figuras para Serie de residuos, **QQPlot**, **ACF de residuos**.

7. **Tabla de error de predicción**: Realice una tabla donde resuma los *scores* obtenidos por cada modelo en el conjunto de test (error de predicción) y agregue además la prueba de hipótesis para independencia. Para esto, usando Pandas construya una tabla con las siguientes columnas: **MAPE, MAE, RMSE, MSE, R², LJung-Box test (p-value)**.

8. **Conjuntos de validación y test**: Considere conjuntos de validación y test de longitud τ = 7, 14, 21, 28. Para el conjunto de entrenamiento, considere todos los casos asociados con las combinaciones:
$$
   \text{dim}(X_{\text{train}}^{(j)}) = (M_{\text{rows}}^{(j)}, N_{\text{cols}}^{(j)}) \quad \text{con} \quad M_{\text{rows}}^{(j)}, N_{\text{cols}}^{(j)} = 7, 14, 21, 28
   $$

9. **Visualización de boxplots**: Dibuje tres *boxplots* (uno para cada set: entrenamiento, validación y test) donde represente los errores obtenidos en el ítem anterior en el eje y. Verifique que las medianas de los tres *boxplots* son cercanas.

10. **Gráfica de series de tiempo**: Dibuje para cada combinación la serie de tiempo original, el conjunto de validación, el conjunto de test y la predicción del conjunto de test. Tenga en cuenta cada uno de los horizontes τ = 7, 14, 21, 28.

11. **Modelos a utilizar**: Los modelos que debe considerar para este ejercicio son los que aparecen en la Tabla 2 y deben ser usados para predecir las series (**magnetic field, angular rate, acceleration**).

| Modelo                    | MAPE  | RMSE  | R²    | Ljung-Box p-value | Jarque-Bera p-value |
|---------------------------|-------|-------|-------|-------------------|---------------------|
| K-NN                      | ...   | ...   | ...   | ...               | ...                 |
| Linear Regression         | ...   | ...   | ...   | ...               | ...                 |
| Ridge Regression          | ...   | ...   | ...   | ...               | ...                 |
| Lasso Regression          | ...   | ...   | ...   | ...               | ...                 |
| Random Forest Regressor   | ...   | ...   | ...   | ...               | ...                 |
| XGBoost Regressor         | ...   | ...   | ...   | ...               | ...                 |
| SVR                       | ...   | ...   | ...   | ...               | ...                 |

*Cuadro 2: Modelo de regresión para el problema de ejercicios de fisioterapia.*

