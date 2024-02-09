# Visualización de Datos de Red Eléctrica

Este proyecto es una aplicación web desarrollada con Streamlit que permite visualizar datos de generación de energía eléctrica proporcionados por la API de Red Eléctrica Española.

### _Aún en desarrollo para ir ampliando el proyecto._

## Funcionalidades

- **Visualización de datos por tipo de generación**: Muestra gráficos de barras y de pastel que representan la generación de energía por tipo (renovable y no renovable).
- **Visualización de datos por mes**: Muestra un gráfico de líneas que representa la generación de energía a lo largo del tiempo, desglosada por tipo.
- **Análisis de porcentajes**: Muestra un gráfico de pastel que representa el porcentaje de generación de energía renovable y no renovable.

## Instalación

1. Clona este repositorio:

_(indicar tu usuario)_
git clone https://github.com/tu_usuario/red-electrica.git

2. Instala las dependencias:
   pip install -r requirements.txt

3. Ejecuta la aplicación:
   streamlit run main.py

## Estructura del Proyecto

**main.py**: Archivo principal que contiene la lógica principal de la aplicación.
**data_utils.py**: Contiene funciones para solicitar y procesar datos de la API de Red Eléctrica.
**visualization_utils.py**: Contiene funciones para generar gráficos utilizando Plotly y Streamlit.

## Contribuciones

Las contribuciones son bienvenidas. Si encuentras algún error o tienes alguna sugerencia de mejora, no dudes en abrir un problema o enviar un pull request.
