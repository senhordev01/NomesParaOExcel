import pandas as pd
def Inserir_Excel():
    nome = []
    matricula = []
    
    qtd_pessoas = int(input('digite a quantidade de pessoas que serao adicionadas: '))
    for i in range(0, qtd_pessoas):
        inserir_nome = input('digite o nome: ')
        nome.append(inserir_nome)
        print(nome)

    for x in range(0, qtd_pessoas):
        inserir_matricula = int(input('digite a matricula: '))
        matricula.append(inserir_matricula)
        print(matricula)
    
    data = {'Nome': nome,
            'Matricula': matricula}
    
    
    df = pd.DataFrame(data)
    print(df)

    df.to_excel('arquivo.xlsx', index = False)

Inserir_Excel()