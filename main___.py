import streamlit as st

st.title('**Proyecto 8 - Arbol de Decisión**')
st.subheader('**Introducción**')

st.write("""
En este proyecto se va a desarrollar una exploración y limpieza de datos de una tabla que contiene variables\
 sobre clientes de un banco, después se desarrollara un modelo que busca clasificar a los individuos por \
la categorización dada por la variable “Atrition_Flag” la cual indica si un usuario tiene una cuenta activa \
(Existing Customer) o una desactivada (Attrited Customer).

El link del notebook donde se desarolla la exploración y analisis de datos es el siguiente:

En este appweb podra inteactuar con los resultados del modelo""")

st.subheader('**Descipcion de las variables**')

st.write("""

**Variable Onjetivo:** Attrition_Flag

La variable Attrition_Flag es una variable cateogiruca que hac referencias al tipo de cuenta de un determinado usuario de un banco. \
Esta tomo el valor 1 para referirse a la categoria "Existing Customer" (cuentas activas) y 0 para "Attrited Customer (cuentas inactivas)"

**Cusstomer Age:**

La variable Customer_Age hace referencia a la edad del cliente.

**Gender:**

La Variable Gender hace referencia al genero del cliente. Tomas el valor de 0 si el cliente es de genero masculino, por el contrario toma el valor de \
0 si es de genero femenino

**Dependent_Count:**

La variable Depebdebt_Count hacereferencia

""")