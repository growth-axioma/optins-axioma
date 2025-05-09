import streamlit as st
import pandas as pd
from io import BytesIO

st.title("CSV a Excel con columnas filtradas")

columnas_deseadas = [
    "Name", "Email", "EmpresaUser", "Cargo", "Actividaddelaempresa", 
    "PaisUser", "CelularUser", "CiudadUser"
]

archivo_csv = st.file_uploader("Sube tu archivo CSV", type="csv")

if archivo_csv is not None:
    try:
        df = pd.read_csv(archivo_csv)
        columnas_presentes = [col for col in columnas_deseadas if col in df.columns]
        df_filtrado = df[columnas_presentes]

        output = BytesIO()
        df_filtrado.to_excel(output, index=False, engine='openpyxl')
        output.seek(0)

        nombre_excel = archivo_csv.name.replace(".csv", ".xlsx")

        st.success("Archivo procesado con éxito.")
        st.download_button(
            label="Descargar Excel",
            data=output,
            file_name=nombre_excel,
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
    except Exception as e:
        st.error(f"Error al procesar el archivo: {e}")
