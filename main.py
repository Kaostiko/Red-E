import requests
import json

def solicitar_data(start_date='2022-01-01T00:00', end_date='2022-12-31T23:59', location='peninsular'):
    """
    Solicitar información a la API de Red Eléctrica

    Parámetros:
        location (str): 'peninsular', 'canarias', 'baleares', 'ceuta', 'melilla'
        start_date (str): Fecha de inicio en formato 'YYYY-MM-DDTHH:MM'.
        end_date (str): Fecha de fin en formato 'YYYY-MM-DDTHH:MM'.

    Retorna:
        dict: Datos obtenidos de la API.
    """
    # Construir la URL de la consulta
    url = 'https://apidatos.ree.es/es/datos/generacion/evolucion-renovable-no-renovable'
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
        print(f"Ubicación no válida. Las opciones válidas son: {opciones_validas}")
        return None

    # Realizar la solicitud GET a la API
    response = requests.get(url, params=parametros)
    print(response.url)
    
    # Verificar si la solicitud fue exitosa
    if response.status_code == 200:
        # Retornar los datos como un diccionario JSON
        return response.json()
    else:
        # Imprimir un mensaje de error si la solicitud falla
        print(f'Error al solicitar datos a la API: {response.status_code}')
        return None

# Obtener los datos
ubicacion = 'melilla'
data = solicitar_data(start_date='2023-01-01T00:00', end_date='2023-12-31T23:59', location='melilla')


# Verificar si se obtuvieron datos
if data:
    nombre_archivo = f'datos_red_electrica_{ubicacion}.json'
    with open(nombre_archivo, 'w') as archivo:
        json.dump(data, archivo, indent=4)
        print("Datos guardados correctamente")
else:
    print("No se ha podido obtener los datos de la API")