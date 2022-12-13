import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import seaborn as sns

Employees = ('Employees.csv')
# Incluí el dataframe completo, ya que los incisos 13 a 17 no indican
# trabajar con la función caché
emplo = pd.read_csv(Employees)
emplo.dropna(inplace=True)
@st.cache
def load_data(nrows):
    employees_data = pd.read_csv(Employees, nrows=nrows)
    lowercase = lambda x : str(x).lower() 
    employees_data.rename(lowercase,axis='columns', inplace=True)
    return employees_data

def filter_ID(employeeid):
    filtered_ID = employees_data[employees_data['employee_id'] == 
                  employeeid]
    return filtered_ID


def filter_hometown(hometown):
    filtered_hometown = employees_data[employees_data['hometown'] == 
                        hometown]
    return filtered_hometown


def filter_unit(unit):
    filtered_unit = employees_data[employees_data['unit'] == 
                    unit]
    return filtered_unit

def filter_education(education):                                           
    filtered_education = employees_data[employees_data['education_level'] == 
                         education]
    return filtered_education

# Título de la app
st.title("Employees App")
st.header('Dataset Overview')
st.write('''This app is useful to analyze the behavior of a set of 
            employees''')
data_load_state = st.text('Loading data...')
employees_data = load_data(500)
data_load_state.text("Done! using st.cache")
sidebar=st.sidebar
sidebar.title('Statistics')

if sidebar.checkbox('Show dataframe'):
    st.dataframe(employees_data)

IDemp = st.sidebar.text_input('Employee ID')
btnBuscar = st.sidebar.button('Search employee ID')
if (btnBuscar):
   data_ID = filter_ID(IDemp.upper())
   count_row = data_ID.shape[0]  # Gives number of rows
   st.write(f"Number of employees : {count_row}")
   st.write(data_ID)

homemp = st.sidebar.text_input('Hometown')
btnBuscarhometown = st.sidebar.button('Search employee hometown')
if (btnBuscarhometown):
   data_hometown = filter_hometown(homemp)
   count_rowb = data_hometown.shape[0]  # Gives number of rows
   st.write(f"Number of employees with the hometown : {count_rowb}")
   st.write(data_hometown)

unitemp = st.sidebar.text_input('Unit')
btnBuscarunit = st.sidebar.button('Search employee unit')
if (btnBuscarunit):
   data_unit = filter_unit(unitemp)
   count_rowc = data_unit.shape[0]  # Gives number of rows
   st.write(f"Number of employees in the unit: {count_rowc}")
   st.write(data_unit)

sidebar.markdown("___")

selected_education = sidebar.selectbox("Select education level", 
                     employees_data['education_level'].unique())
if(selected_education):
   data_education = filter_education(selected_education)
   count_rowd = data_education.shape[0]
   if sidebar.checkbox('''Show dataframe associated to education 
                         level filter'''):
       st.write(f'''Selected Option: {selected_education!r}. Total 
                    employees with the selected level:   {count_rowd}''')
       st.write(data_education)

selected_hometown = sidebar.selectbox("Select a Hometown", 
                    employees_data['hometown'].unique())

# Agregué un checkbox para que fuera más estético el despliegue
# de los datos
if (selected_hometown):
   if sidebar.checkbox('Show dataframe associated to hometown filter'):
       data_hometown = filter_hometown(selected_hometown)
       count_rowb = data_hometown.shape[0]  # Gives number of rows
       st.write(f'''Number of employees from
                    {selected_hometown} : {count_rowb}''')
       st.write(data_hometown)

selected_unit = sidebar.selectbox("Select a Hometown", 
                employees_data['unit'].unique())
if (selected_unit):
   if sidebar.checkbox('Show dataframe associated to unit filter'):
       data_unit = filter_unit(selected_unit)
       count_rowc = data_unit.shape[0] 
       st.write(f'''Number of employees working in the {selected_unit}
                    unit  : {count_rowc}''')
       st.write(data_unit)
fig, ax=plt.subplots()
ax.hist(emplo.Age)
st.header('Age histogram')
plt.xlabel('Age')   
st.pyplot(fig)

fig2 = plt.figure(figsize=(10, 4))
sns.countplot(x="Unit", data=emplo)
plt.xticks(rotation=90)
st.header('Countplot')
st.pyplot(fig2)
mean = pd.DataFrame(emplo).groupby('Hometown').mean()
st.header('Attrition rate by hometown')
st.write('''I have calculated the average attrition rate by hometown
            in order to determine the hometown with the the highest
            attrition rate ''')
if st.checkbox('Show average attrition rate by hometown plot'):
    fig3 = plt.figure(figsize=(10, 4))
    mean["Attrition_rate"].plot()
    plt.xlabel('Hometown') 
    plt.ylabel('Attrition rate') 
# displaying the title
    plt.title("Mean Attrition rate by hometown")
    st.pyplot(fig3)

st.header('Attrition rate and age')
st.write('''In order to explore the relationship between the age of the
            employees and attrition rate, there was performed a 
            2d-histogram which contains such information ''')
if st.checkbox('Show 2-D histogram'):
    fig4 = plt.figure(figsize=(10, 4))
    plt.hist2d(emplo['Attrition_rate'], emplo['Age'], 
               range=[[0, 0.9959],[0, 65]])
    plt.colorbar()
    plt.xlabel('Attrition rate') 
    plt.ylabel('Age') 
    plt.title("Relationship between Age and Attrition rate")
    st.pyplot(fig4)
st.write('''We are observing that the relationship between age and
            attrition rate is not significant, cause the highest
            value is not observed for a particular age''')

st.header('Attrition rate and time of service ')
st.write('''In order to explore the relationship between the time of
            service of the employees  and attrition rate, a 
            2d-histogram which contains such information was 
            performed ''')
if st.checkbox('Show 2-D histogram for the time of service'):
     fig5 = plt.figure(figsize=(10, 4))
     plt.hist2d(emplo['Attrition_rate'], emplo['Time_of_service'], 
                range=[[0, 0.9959],[0, 43]])
     plt.xlabel('Attrition rate') 
     plt.ylabel('Time of service') 
     plt.title("Relationship between Time of service and Attrition rate")
     plt.colorbar()
     st.pyplot(fig5)
st.write('''We are observing that the relationship between time of service
            and attrition rate is not significant, cause the highest value
            is not observed for a particular time of service''')    