import pandas as pd

def inserir_excel_simples():
    # Coletar os nomes em uma única linha
    nomes_input = input("Digite todos os nomes separados por espaço: ")
    nomes = nomes_input.split()

    # Coletar as matrículas em uma única linha
    matriculas_input = input("Digite todas as matrículas, na mesma ordem dos nomes, separadas por espaço: ")
    matriculas_str = matriculas_input.split()

    # Verificar se as quantidades batem
    if len(nomes) != len(matriculas_str):
        print("Erro: a quantidade de nomes e matrículas não é a mesma.")
        return

    # Tentar converter as matrículas para números inteiros
    try:
        matriculas = [int(m) for m in matriculas_str]
    except ValueError:
        print("Erro: todas as matrículas devem ser números.")
        return

    # Criar o DataFrame e salvar
    df = pd.DataFrame({'Nome': nomes, 'Matrícula': matriculas})
    print("\nDados organizados:")
    print(df)

    df.to_excel("arquivo.xlsx", index=False)
    print("\nArquivo 'arquivo.xlsx' salvo com sucesso!")

# Executar
inserir_excel_simples()
