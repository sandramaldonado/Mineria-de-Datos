import pandas as pd 
from textblob import TextBlob
import seaborn as sns

xlsx=pd.read_excel("Encuesta de Satisfacción con las Reposiciones (respuestas).xlsx","Respuestas de formulario 1")
datos1=xlsx['Porqué?'].values.tolist()
datos2=xlsx['Porqué?1'].values.tolist()
print(datos1)
print(datos2)
t=""
array= []


    
for x in range(len(datos1)):
    t=TextBlob(datos1[x])
    traduccion=t.translate(to="en")
    print(traduccion)
    print(traduccion.sentiment,"\n")
    array.append(str(traduccion))
nuevos_datos = pd.DataFrame(array, columns=['porque?'])
nuevos_datos.to_excel("Ejemplito2.xlsx", sheet_name='example')
print(array)

dato_en = pd.read_excel("Ejemplito2.xlsx","example")
dato_en ['polaridad']=dato_en['porque?'].apply(lambda x: TextBlob(x).sentiment.polarity)
dato_en ['subobj']=dato_en['porque?'].apply(lambda x: TextBlob(x).sentiment.subjectivity)

print("Polaridad")
print("Maximo Valor", dato_en['polaridad'].max())

print("Minimo Valor", dato_en['polaridad'].min())

print("Valor Medio", dato_en['polaridad'].mean())

sns.distplot(dato_en['polaridad'])
sns.distplot(dato_en['subobj'])
n=0
while n<4:
    dato_en['P'+ str(n)]=dato_en['porque?'].apply(lambda x: TextBlob(x).sentiment.polarity)
    dato_en['S'+ str(n)]= dato_en['porque?'].apply(lambda x: TextBlob(x).sentiment.subjectivity)
    n=n+1
dato_en.to_excel('Resultados.xlsx')
