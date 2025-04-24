import pandas as pd
Nome = []
Matricula = []

Inserir = input('digite o nome: ')
Nome.append(Inserir)
print(Nome)

while True:
  pergunta = input('quer adicionar nome ? ')
  if pergunta in ['sim', 'Sim','SIM']:
    add_nome = input('digite o nome: ')
    Nome.append(add_nome)
  elif pergunta in ['nao', 'Nao', 'NAO']:
    break
  else:
    print('Nao consegui entender. Digite novamente')


Inserir_matricula = input('digite a matrícula: ')
Matricula.append(Inserir_matricula)
print(Matricula)

while True:
  pergunta2 = input('quer adicionar matrícula ? ')
  if pergunta2 in ['sim', 'Sim','SIM']:
    add_matricula = input('digite o matrícula: ')
    Matricula.append(add_matricula)
  elif pergunta2 in ['nao', 'Nao', 'NAO']:
    break
  else:
    print('Nao consegui entender. Digite novamente')

data = {'Nome': Nome,
        'Matrícula': Matricula}

df = pd.DataFrame(data)
print(df)

df.to_excel('arquivo.xlsx', index=False)