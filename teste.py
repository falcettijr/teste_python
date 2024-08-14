import pandas as pd

# Defina os caminhos dos arquivos Excel
planilhas = ['planilha_1.xlsx', 'planilha_2.xlsx']

# Mapeamento de colunas com nomes diferentes, mas que contêm os mesmos dados
colunas_mapeadas = {
    'Nome': 'Nome',
    'Nome Completo': 'Nome',
    'Telefone': 'Telefone',
    'Celular': 'Telefone',
    'cpf': 'CPF',
    'CPF': 'CPF'
}

# Lista para armazenar os dataframes
dataframes = []

# Carregar e renomear as colunas das planilhas
for planilha in planilhas:
    df = pd.read_excel(planilha)
    
    # Renomear as colunas de acordo com o mapeamento
    df = df.rename(columns=colunas_mapeadas)
    
    # Selecionar apenas as colunas de interesse
    df = df[['Nome', 'Telefone', 'CPF']]
    
    dataframes.append(df)

# Unificar todas as planilhas em um único dataframe
df_unificado = pd.concat(dataframes, ignore_index=True)

# Remover duplicatas, caso existam
df_unificado = df_unificado.drop_duplicates()

# Exportar para um novo arquivo Excel
df_unificado.to_excel('clientes_unificados.xlsx', index=False)

print("Unificação concluída! O arquivo 'clientes_unificados.xlsx' foi criado.")
