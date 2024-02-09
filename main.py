import streamlit as st
from data_utils import solicitar_data
from visualization_utils import graficar_datos

def main():
    st.title("Visualización de Datos de Red Eléctrica")
    
    # Formulario para ingresar la ubicación y el año
    ubicacion = st.selectbox("Selecciona la ubicación:", ['peninsular', 'canarias', 'baleares', 'ceuta', 'melilla'])
    anio_opcion = st.selectbox("Selecciona el año:", ['2018', '2019', '2020', '2021', '2022', '2023', 'Desde 2018 al 2023'])
    
    # Determinar el rango de años para la consulta
    if anio_opcion == 'Desde 2018 al 2023':
        start_year = 2018
        end_year = 2024
    else:
        start_year = int(anio_opcion)
        end_year = int(anio_opcion)
    
    # Botón para solicitar los datos
    if st.button("Obtener datos"):
        for year in range(start_year, end_year + 1):
            # Solicitar los datos a la API
            start_date = f"{year}-01-01T00:00"
            end_date = f"{year}-12-31T23:59"
            data = solicitar_data(start_date, end_date, ubicacion)
            
            # Verificar si se obtuvieron datos
            if data is not None:
                # Mostrar los datos en formato tabla desplegable
                with st.expander(f"Datos obtenidos para el año {year}"):
                    st.write(data)
                
                # Graficar los datos
                graficar_datos(data)
            else:
                st.error("No se ha podido obtener los datos de la API")

if __name__ == "__main__":
    main()
