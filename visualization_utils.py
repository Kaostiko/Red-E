import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

def graficar_datos(df):
    """
    Graficar los datos por tipo de generación utilizando Plotly.
    
    Parámetros:
        df (DataFrame): DataFrame que contiene los datos.
    """
    # Filtrar los datos para excluir la categoría 'Generación total'
    df_filtrado = df[df['type'] != 'Generación total']
    
    # Gráficos:
    fig_bar = px.bar(df_filtrado, x='type', y='value', color='type',
                     labels={'type': 'Tipo de Generación', 'value': 'Valor Total'},
                     title='Generación de Energía por Tipo')
    
    fig_pie = px.pie(df_filtrado, values='percentage', names='type',
                     labels={'type': 'Tipo de Generación', 'percentage': 'Porcentaje (%)'},
                     title='Porcentaje de Generación de Energía por Tipo')
    
    # Calcular el porcentaje de energía renovable y no renovable
    df_renewable = df_filtrado[df_filtrado['renewable'] == 'Renovable']
    total_renovable = df_renewable['value'].sum()
    total_no_renovable = df_filtrado['value'].sum() - total_renovable
    total_generacion = df_filtrado['value'].sum()
    porcentaje_renovable = (total_renovable / total_generacion) * 100
    porcentaje_no_renovable = (total_no_renovable / total_generacion) * 100
    
    # Crear un gráfico de barras con barras de diferentes colores / valor total renovable-no renovable
    fig_valor_total = go.Figure(data=[
        go.Bar(
            x=['Renovable'],
            y=[total_renovable],
            name='Renovable',
            marker_color='#0068C9',
            text=[f'{total_renovable:.2f} MWh'],
            textposition='auto',
            showlegend=False
        ),
        go.Bar(
            x=['No Renovable'],
            y=[total_no_renovable],
            name='No Renovable',
            marker_color='#83C9FF',
            text=[f'{total_no_renovable:.2f} MWh'],
            textposition='auto',
            showlegend=False
        )
    ])

    # Actualizar el diseño del gráfico
    fig_valor_total.update_layout(title='Valor Total de Generación de Energía Renovable y No Renovable',
                                xaxis_title='Tipo de Generación',
                                yaxis_title='Valor Total (MWh)',
                                bargap=0.2)

    df_porcentaje = pd.DataFrame({'Tipo de Generación': ['Renovable', 'No Renovable'],
                                  'Porcentaje': [porcentaje_renovable, porcentaje_no_renovable]})
    
    fig_porcentaje = px.pie(df_porcentaje, values='Porcentaje', names='Tipo de Generación',
                             labels={'Porcentaje': 'Porcentaje de Generación (%)'},
                             title='Porcentaje de Generación de Energía Renovable y No Renovable')
    
    fig_mes = px.line(df_filtrado, x='datetime', y='value', color='type',
                      labels={'value': 'Valor Total', 'datetime': 'Mes'},
                      title='Generación de Energía por Mes')
    
    fig_mes_percentage_pie = px.pie(df_filtrado, values='percentage', names='type',
                                    labels={'percentage': 'Porcentaje (%)', 'type': 'Tipo de Generación'},
                                    title='Porcentaje de Generación de Energía por Mes')

    # Mostrar los gráficos
    st.plotly_chart(fig_bar)
    st.plotly_chart(fig_pie)
    st.plotly_chart(fig_mes)
    st.plotly_chart(fig_mes_percentage_pie)
    st.plotly_chart(fig_valor_total)
    st.plotly_chart(fig_porcentaje)
