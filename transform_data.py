import pandas as pd 
import json

# Definir el nombre del lugar y el año
nombre_lugar = 'peninsular'
anio = '2022'

# Cargar los datos desde el archivo JSON
with open(f'datos_red_electrica_{nombre_lugar}.json', 'r') as file:
    data = json.load(file)

# Extraer los datos relevantes y añadir la información del grupo
records = []
for item in data['included']:
    group_type = item['type']  
    # Obtener el tipo de grupo (Renovable o No Renovable)
    for value in item['attributes']['values']:
        record = {
            'type': group_type,
            'datetime': value['datetime'],
            'value': value['value'],
            'percentage': value['percentage']
        }
        records.append(record)

# Convertir los datos en un DataFrame de pandas
df_lugar_anio = pd.DataFrame(records)

# Mostrar el DataFrame
print('data cruda', df_lugar_anio)

# Convertir la columna 'datetime' en cadena de texto
df_lugar_anio['datetime'] = df_lugar_anio['datetime'].astype(str)

# Separar las fechas en día, mes y año
df_lugar_anio[['date', 'time']] = df_lugar_anio['datetime'].str.split('T', expand=True)
df_lugar_anio[['year', 'month', 'day']] = df_lugar_anio['date'].str.split('-', expand=True)

# Incorporar el dato 'type' a cada registro como una nueva columna
df_lugar_anio['group_type'] = df_lugar_anio['type']

# Eliminar columnas que no sirven
nuevo_df_lugar_anio = df_lugar_anio.drop(columns=['datetime', 'day', 'date', 'time'])

print('############################## DATA TRATADA ##########################', nuevo_df_lugar_anio)

# Guardar el DataFrame en un archivo de Excel con el nombre del lugar y el año
nuevo_df_lugar_anio.to_excel(f'datos_red_electrica_{nombre_lugar}_{anio}.xlsx', index=False)
