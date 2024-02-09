import requests
import streamlit as st
import pandas as pd

def solicitar_data(start_date, end_date, location):
    """
    Solicitar información a la API de Red Eléctrica

    Parámetros:
        location (str): 'peninsular', 'canarias', 'baleares', 'ceuta', 'melilla'
        start_date (str): Fecha de inicio en formato 'YYYY-MM-DDTHH:MM'.
        end_date (str): Fecha de fin en formato 'YYYY-MM-DDTHH:MM'.

    Retorna:
        DataFrame: Datos obtenidos de la API.
    """
    # Construir la URL de la consulta
    url = 'https://apidatos.ree.es/es/datos/generacion/estructura-generacion'
    parametros = {
        'time_trunc': 'month',
        'start_date': start_date,
        'end_date': end_date
    }

    # Verificar si se proporcionó una ubicación y si es una opción válida
    opciones_validas = {'peninsular', 'canarias', 'baleares', 'ceuta', 'melilla'}
    if location in opciones_validas:
        parametros['geo_limit'] = location
    elif location:
        st.error(f"Ubicación no válida. Las opciones válidas son: {opciones_validas}")
        return None

    # Realizar la solicitud GET a la API
    response = requests.get(url, params=parametros)
    
    # Verificar si la solicitud fue bien
    if response.status_code == 200:
        # Convertir la respuesta JSON en un DataFrame
        data = response.json()
        records = []
        for item in data['included']:
            group_type = item['type']  
            renewable = item['attributes']['type']
            for value in item['attributes']['values']:
                record = {
                    'type': group_type,
                    'datetime': value['datetime'],
                    'value': value['value'],
                    'percentage': value['percentage'],
                    'renewable': renewable
                }
                records.append(record)
        df = pd.DataFrame(records)
        return df
    else:
        # Imprimir un mensaje de error si la solicitud falla
        st.error(f'Error al solicitar datos a la API: {response.status_code}')
        return None
