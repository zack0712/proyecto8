import streamlit as st 
import pickle as pkl
import numpy as np 
from sklearn.tree import DecisionTreeClassifier
from PIL import Image

image1 = Image.open('Heatmap_.png')

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
0 si es de genero femenino.

**Dependent_Count:**

La variable Depebdebt_Count hacereferencia al numero de personas que dependen del cliente.


**Education_level**

La vaiable Education_Level hace referencia a los años de educacion del cliente.

**Marital_Status**

La variable Marital_Status hace refencia a si la personas tiene pareja o no. Esta toma el valor de 1 si la personas tiene pareja y por el contrario 0 si no es el caso.

**Months_on_book**	

La variable Months_on_book hace referncia a los meses consecutivos los cuales el individuo se ha mantenido como cliente del banco.

**Total_Relationship_Count**

La variable Total_Relationship_Count hace referencia al numero de productos que el cliente tiene con el banco.

**Months_Inactive_12_mon**

La varriable Months_Inactive_12_mon hace referencia al numero de meses que el cliente ha estado inactivo en los ultimos 12 meses.

**Contacts_Count_12_mon**

La varaible Contacts_Count_12_mon hace referencia al numero de contactos que se ha tenido con el cliente en los ultimos 12 meses.

**Credit_Limit**

La variable Credit_Limit hace referencia al limite de credito que tiene el cliente en la tarjeta de credito con el banco.

**Total_Revolving_Bal**	

La varaible Total_Revolving_Bal hace referencia al saldo ratarorio disponible en la tarjeta de credito del cliente.

**Avg_Open_To_Buy**	

La variable Avg_Open_To_Buy al promedio de la linea de credito diponible para usar la tatjeta en los ultimos 12 meses.

**Total_Amt_Chng_Q4_Q1**

La variable Total_Amt_Chng_Q4_Q1 hace referencia en el cambio en el monto de la cuenta del cliente del primer trimestre a el cuarto trimestre.

**Total_Trans_Amt**	

La variable Total_Trans_Amt hace referencia al monto total de todas las transferencias ralizadas por el cliente.

**Total_Trans_Ct**	

La variable Total_Trans_Ct hace referencia al numero total de transacciones realizadas por el cliente.

**Total_Ct_Chng_Q4_Q1**	

La varaible Total_Ct_Chng_Q4_Q1 hace referencia al cambio en el numero de transacciones realizadas por el clientre entre el primer y el cuarto trimestre.

**Avg_Utilization_Ratio**

La variable Avg_Utilization_Ratio hace referencia a el ratio de uso medio de la tarjeta.

""")

st.subheader('**Heatmap Correlación Variables del Modelo**')
st.image(image1)



st.subheader('**Interactuar con el Modelo**')
st.write(F'##### Link notebook entrenamiento del modelo: https://github.com/zack0712/Clase-Machine-Learning/blob/main/proyecto8.ipynb')

col1,col2=st.columns(2)
with col1:
    edad = st.number_input('Edad:',min_value=(0))
    genero = st.selectbox('Genero:',('Masculino','Femenino'))
    dependientes = st.number_input('Numero de Dependientes',min_value=(0))
    años_educ = st.number_input('Años de Educación',min_value=(0))
    pareja = st.selectbox('Estado Civil:',('Casado','Soltero'))
    meses_fidelidad = st.number_input('Meses con el banco:',min_value=(0))
    productos = st.number_input('Numero de productos con el banco:',min_value=(0))
    meses_inactivo = st.number_input('Numero de Meses Inactivos:',min_value=(0))
    contactos = st.number_input('Numero de contactos:',min_value=(0))

with col2: 
    limite_credito = st.number_input('Limite de Credito:',min_value=(0))
    saldo_rotatorio = st.number_input('Saldo Rotaroio en tarjeta:',min_value=(0))
    linea_cred_mean = st.number_input('Linea de Credito Promedio: (Ultimos 12 meses)',min_value=(0))
    cambio_monto = st.number_input('Cambio en el monto de la transacción (Q4 sobre Q1)')
    monto_trans = st.number_input('Monto Total de Transacciones (Ultimos 12 meses)',min_value=(0))
    numero_trans = st.number_input('Numero de Transacciones (Ultimos 12 meses)',min_value=(0))
    cambio_trans = st.number_input('Cambio en el recuento de transacciones (Q4 sobre Q1)')
    ratio_uso = st.number_input('Ratio de uso medio de la tarjeta')

clf_pickle = open('clf_tree.pickle','rb')
clf = pkl.load(clf_pickle)
clf_pickle.close()

genero = 1 if genero == 'Maculino' else 0
pareja = 1 if pareja == 'Casado' else 0

variables = [edad, genero, dependientes, años_educ, pareja, meses_fidelidad, productos, meses_inactivo, contactos,\
    limite_credito, saldo_rotatorio, linea_cred_mean, cambio_monto, monto_trans, numero_trans, cambio_trans, ratio_uso]

prediccion = clf.predict([np.array(variables).reshape(1,-1)][0])[0]
proba =  clf.predict_proba([np.array(variables).reshape(1,-1)][0])[0][1]


st.subheader('**Resultados de Prediccion**')
resultado = 'Existing customer 'if prediccion ==1 else 'Attrited Customer'

st.markdown(f"""
#### Se clasifica al cliente en el grupo ---> {resultado} 
""")
