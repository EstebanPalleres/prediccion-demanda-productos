# Predicción de Demanda de Productos

Este proyecto tiene como objetivo predecir la demanda de productos utilizando varias técnicas de machine learning.

## Descripción

He desarrollado un modelo que predice la demanda de productos utilizando varias técnicas de machine learning como regresión lineal, árboles de decisión y random forest. Implementé el modelo con una API Flask y creé un tablero interactivo para predicciones en tiempo real.

## Pasos del Proyecto

1. **Recolección de Datos:** Datos históricos de demanda de productos.
2. **Preprocesamiento de Datos:** Limpieza y transformación de los datos.
3. **Desarrollo de Modelos:** Implementación de varios modelos de machine learning.
4. **Evaluación de Modelos:** Comparación de modelos usando métricas como MAE y RMSE.
5. **Implementación:** Creación de una API Flask y un tablero interactivo.

## Resultados

- Todos los modelos (regresión lineal, árboles de decisión y random forest) entregaron resultados similares:
  - MAE: 0.13
  - RMSE: 0.18
- El modelo LSTM logró un loss de 0.0320.

## Conclusión Ejecutiva

El modelo desarrollado puede predecir la demanda de productos con una precisión razonable. Las predicciones ayudan a optimizar el inventario y mejorar la planificación de la cadena de suministro, tomando decisiones más informadas basadas en datos.

## Cómo Ejecutar el Proyecto

1. Clona este repositorio.
2. Instala las dependencias necesarias.
3. Ejecuta el archivo `app.py` para iniciar la API Flask.
4. Accede al tablero interactivo para visualizar las predicciones en tiempo real.

## Archivos Importantes

- `prediccion-demanda-productos.ipynb`: Jupyter Notebook con todo el código del proyecto.
- `app.py`: Código de la API Flask.
- `dashboard.py`: Código del tablero interactivo.
