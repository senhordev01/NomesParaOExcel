#para esse sistema rodar, precisa instalar as extensoes: 'pip install pandas', 'pip install openpyxl'
#certifique que tenha um excel em sua maquina
import pandas as pd

data = {'Nome':[],
        'Matrícula': []} #insira os nomes e as matrículas

df = pd.DataFrame(data)
print(df)

df.to_excel('nomes.xlsx', index=False)
