# Control de Gastos Multiusuario
Proyecto final del *Diplomado en Python: Fundamentos y Aplicaciones Prácticas*.

Este proyecto implementa un **dashboard interactivo en Streamlit** para el registro, análisis y visualización de **gastos personales y familiares**, permitiendo comparar múltiples usuarios y obtener información útil para la toma de decisiones.

---

## Objetivo del Proyecto
Desarrollar una solución en Python que:
1. Obtenga y prepare datos.
2. Explore y visualice métricas relevantes.
3. Entregue valor mediante análisis y comparaciones.
4. Presente una interfaz simple e intuitiva para el usuario.

El proyecto simula un sistema de gestión de gastos para dos usuarios: **Eduardo y Lorenza**, con datos distribuidos en dos meses.

---

## Estructura del Repositorio

```
proyecto-gastos/
│── README.md
│── requirements.txt
│── data/
│ └── gastos.csv
│── notebooks/
│ └── EDA.ipynb
│── app/
│ └── Control de Gastos.py
│── docs/
├── informe.pdf
└── slides.pdf
```
---

## Dataset

El archivo `gastos.csv` contiene los gastos registrados por usuario.

### Columnas del dataset:
| Columna     | Tipo     | Descripción |
|-------------|----------|-------------|
| usuario     | string   | Nombre del usuario dueño del gasto |
| fecha       | date     | Fecha del gasto (YYYY-MM-DD) |
| categoria   | string   | Tipo de gasto (comida, transporte, etc.) |
| descripcion | string   | Descripción libre del gasto |
| monto       | int      | Monto en guaraníes |

### Fuente de datos
El dataset fue creado mediante ia solo para proyecto final (no contiene datos personales reales).

---

## Preparación y Limpieza de Datos
La preparación del dataset incluye:
- Conversión de fechas a `datetime`.
- Eliminación de entradas vacías.
- Normalización de nombres de categorías.
- Validación de tipos numéricos para el campo `monto`.

Todo este proceso se encuentra documentado en el notebook:  
📁 `notebooks/EDA.ipynb`

---

## Exploratory Data Analysis (EDA)

En el notebook se responden preguntas como:
- ¿Qué usuario gasta más?
- ¿Cuáles son las categorías más costosas?
- ¿Cómo evolucionan los gastos por día?
- ¿Cuáles son los mayores gastos puntuales?

Incluye gráficos:
- Barras por categoría  
- Barras por usuario  
- Línea temporal  
- Top 5 gastos más altos  
- Distribución del monto  

---

## Aplicación Streamlit

La interfaz está en:  
📁 `app/Control de Gastos.py`

### Funciones principales:
✔ Registrar gastos  
✔ Agregar nuevos usuarios  
✔ Filtrar por usuario  
✔ Filtrar por rango de fechas  
✔ Tabla de gastos filtrados  
✔ Gráfico de gastos por categoría  
✔ Gráfico de evolución diaria  
✔ Comparación entre usuarios  
✔ Comparación por categoría  
✔ Resumen automático (totales, promedios, máximos, mínimos)  
✔ Top 5 gastos más altos  

### Ejecutar la app:
Asegúrese de tener `streamlit` instalado.

```bash
streamlit run "Control de Gastos.py"
```

---

## 📄 requirements.txt
Estas son las dependencias necesarias para ejecutar el proyecto:

```bash
pandas
numpy
matplotlib
streamlit
```

Podés instalarlas con:

```bash
pip install -r requirements.txt
```
## Informe Final

El informe completo del proyecto (máx. 10 páginas) se encuentra en:

📁 docs/informe.pdf

Incluye:

-   Objetivo del proyecto

-   Calidad y análisis de los datos

-   Limpieza y transformaciones

-   EDA con gráficos y hallazgos

-   Resultados del análisis

-   Conclusiones

-   Recomendaciones y próximos pasos

## Presentación

La presentación utilizada para la defensa del proyecto está en:

📁 docs/slides.pdf


Incluye:

- Problema

- Datos

- Análisis

- Resultados

- Demo

- Conclusiones

## Próximos Pasos (Mejoras sugeridas)

Algunas mejoras que pueden implementarse en el futuro:

- Sistema de login con contraseñas hash.

- Exportación de reportes a Excel o PDF.

- Alertas automáticas por sobre-gasto.

- Predicción simple de gastos futuros.

- Gráficos adicionales (tendencias mensuales, proyecciones).



## 👨‍💻 Autor

Proyecto desarrollado por Eduardo Maidana, como trabajo final del
Diplomado en Python: Fundamentos y Aplicaciones Prácticas.
