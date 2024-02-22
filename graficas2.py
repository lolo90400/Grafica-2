import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns  # Importamos seaborn para mejorar la visualización

# Cargar el dataset
data = {
    'id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    'materia': ['Matemáticas', 'Historia', 'Ciencias', 'Lenguaje'] * 5,
    'nota': [80, 65, 90, 75, 95, 70, 85, 60, 78, 82, 93, 68, 73, 88, 77, 50, 92, 63, 85, 79],
    'aprobado': ['Sí', 'No', 'Sí', 'Sí', 'Sí', 'Sí', 'Sí', 'No', 'Sí', 'Sí', 'Sí', 'Sí', 'Sí', 'Sí', 'Sí', 'No', 'Sí', 'No', 'Sí', 'Sí']
}

df = pd.DataFrame(data)

# Graficar la distribución de notas con boxplots separados por materia
plt.figure(figsize=(10, 6))
sns.boxplot(x='materia', y='nota', data=df, palette='Set1')
plt.title('Distribución de Notas')
#plt.xlabel()
plt.ylabel('Nota')
plt.grid(True)
plt.show()

# Graficar la distribución de aprobados con un pie chart
aprobados = df['aprobado'].value_counts()
plt.figure(figsize=(8, 6))
plt.pie(aprobados, labels=['Aprobados', 'No Aprobados'], autopct='%1.1f%%', startangle=90, colors=['lightblue', 'lightcoral'])
plt.title('Distribución Estudiantes')
plt.show()