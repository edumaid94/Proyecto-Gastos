import streamlit as st
import pandas as pd
import os
from datetime import date

CSV_FILE = "gastos.csv"

# ---------------------- Cargar o crear CSV ----------------------
def load_data():
    if os.path.exists(CSV_FILE):
        return pd.read_csv(CSV_FILE)
    else:
        df = pd.DataFrame(columns=["usuario", "fecha", "categoria", "descripcion", "monto"])
        df.to_csv(CSV_FILE, index=False)
        return df

def save_data(df):
    df.to_csv(CSV_FILE, index=False)

# ---------------------- App ----------------------
st.title("💰 Control de Gastos Multiusuario")

df = load_data()

st.sidebar.header("Menú")
opcion = st.sidebar.selectbox("Opciones", ["Registrar gasto", "Ver reportes"])

# ---------------------- Registrar gasto ----------------------
if opcion == "Registrar gasto":
    st.header("Registrar gasto")

    usuarios_existentes = sorted(df["usuario"].dropna().unique().tolist())
    usuario = st.selectbox("Usuario", usuarios_existentes + ["Agregar nuevo"])

    # Agregar nuevo usuario
    if usuario == "Agregar nuevo":
        nuevo_usuario = st.text_input("Nombre del nuevo usuario")
        if st.button("Guardar usuario"):
            if nuevo_usuario.strip() != "":
                df.loc[len(df)] = [nuevo_usuario, "", "", "", ""]
                save_data(df)
                st.success(f"Usuario '{nuevo_usuario}' agregado. Selecciónalo ahora para cargar un gasto.")
            else:
                st.warning("Debe ingresar un nombre válido.")
        st.stop()

    fecha = st.date_input("Fecha", value=date.today())
    categoria = st.selectbox("Categoría", ["Comida", "Transporte", "Super", "Ocio", "Combustible", "Otros"])
    descripcion = st.text_input("Descripción")
    monto = st.number_input("Monto (Gs.)", min_value=0)

    if st.button("Guardar gasto"):
        nueva_fila = {
            "usuario": usuario,
            "fecha": fecha,
            "categoria": categoria,
            "descripcion": descripcion,
            "monto": monto
        }
        df = pd.concat([df, pd.DataFrame([nueva_fila])], ignore_index=True)
        save_data(df)
        st.success("Gasto registrado correctamente.")

# ---------------------- Reportes ----------------------
elif opcion == "Ver reportes":
    st.header("Reportes de gastos")

    df["fecha"] = pd.to_datetime(df["fecha"], errors="coerce")

    st.subheader("Filtros")

    # Filtro por usuario
    usuario_filtro = st.selectbox(
        "Filtrar por usuario",
        ["Todos"] + sorted(df["usuario"].dropna().unique().tolist())
    )

    # Filtro por fechas
    col1, col2 = st.columns(2)
    fecha_min = df["fecha"].min()
    fecha_max = df["fecha"].max()

    fecha_inicio = col1.date_input("Fecha inicio", fecha_min)
    fecha_fin = col2.date_input("Fecha fin", fecha_max)

    # Aplicar filtros
    df_filtrado = df.copy()

    if usuario_filtro != "Todos":
        df_filtrado = df_filtrado[df_filtrado["usuario"] == usuario_filtro]

    df_filtrado = df_filtrado[
        (df_filtrado["fecha"] >= pd.to_datetime(fecha_inicio)) &
        (df_filtrado["fecha"] <= pd.to_datetime(fecha_fin))
    ]

    # Tabla
    st.subheader("Tabla de gastos filtrados")
    st.dataframe(df_filtrado)

    # Gráfico total por categoría
    st.subheader("Total por categoría")
    tot_cat = df_filtrado.groupby("categoria")["monto"].sum()
    st.bar_chart(tot_cat)

    # Total por día
    st.subheader("Total por día")
    tot_dia = df_filtrado.groupby("fecha")["monto"].sum()
    st.line_chart(tot_dia)

    # Comparación entre usuarios
    st.subheader("Comparación entre usuarios")
    total_por_usuario = df_filtrado.groupby("usuario")["monto"].sum()
    st.bar_chart(total_por_usuario)

    # Comparación por categoría entre usuarios
    st.subheader("Comparación por categoría entre usuarios")
    total_cat_usuario = df_filtrado.pivot_table(
        index="categoria",
        columns="usuario",
        values="monto",
        aggfunc="sum",
        fill_value=0
    )
    st.bar_chart(total_cat_usuario)

    # ---------------------- RESUMEN AUTOMÁTICO ----------------------
    st.subheader("Resumen automático")

    total_gastado = df_filtrado["monto"].sum()
    promedio_gasto = df_filtrado["monto"].mean()
    gasto_min = df_filtrado["monto"].min()
    gasto_max = df_filtrado["monto"].max()
    cantidad_gastos = df_filtrado.shape[0]

    promedio_diario = df_filtrado.groupby("fecha")["monto"].sum().mean()

    st.write(f"**Total gastado:** {total_gastado:,.0f} Gs.")
    st.write(f"**Promedio por gasto:** {promedio_gasto:,.0f} Gs.")
    st.write(f"**Gasto mínimo:** {gasto_min:,.0f} Gs.")
    st.write(f"**Gasto máximo:** {gasto_max:,.0f} Gs.")
    st.write(f"**Cantidad de gastos registrados:** {cantidad_gastos}")
    st.write(f"**Promedio diario gastado:** {promedio_diario:,.0f} Gs.")

    # ---------------------- TOP 5 GASTOS MÁS ALTOS ----------------------
    st.subheader("Top 5 gastos más altos")

    if not df_filtrado.empty:
        top5 = df_filtrado.nlargest(5, "monto")
        st.table(top5[["fecha", "usuario", "categoria", "descripcion", "monto"]])
    else:
        st.info("No hay datos para mostrar en el top 5.")
