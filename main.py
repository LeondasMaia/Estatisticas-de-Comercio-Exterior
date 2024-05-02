from plotly.subplots import make_subplots
import plotly.express as px
import pandas as pd
import os

#ALterando para o diretorio de utilização
novo_diretorio = r"C:\Users\leond\OneDrive\Área de Trabalho\Seu_Bone\PS\Arquivos"

#Alterar o diretório atual para o novo diretório
os.chdir(novo_diretorio)


#Importando as tabelas para o código

#Tabela de importações 2020
import20 = pd.read_csv('IMP_2020.csv', sep = ';')

#Tabela de importações 2021
import21 = pd.read_csv('IMP_2021.csv', sep = ';')

#Tabela de exportações 2020
export20 = pd.read_csv('EXP_2020.csv', sep = ';')

#Tabela de exportações 2021
export21 = pd.read_csv('EXP_2021.csv', sep = ';')



#Fazendo a união das duas tabelas, a de 2020 e depois a de 2021, gerando a tabela de importação / exportação total (2020+2021):
import_total = pd.concat([import20, import21], ignore_index=True)

export_total = pd.concat([export20, export21], ignore_index=True)


#Codigos para realizar a limpeza da base de dados
#import_total.info()
#import_total.isnull().sum()
#import_total.duplicated().sum()

#export_total.info()
#export_total.isnull().sum()
#export_total.duplicated().sum() 


#Separamos os produtos por estados
mais_importados = import_total.groupby(['SG_UF_NCM', 'CO_NCM', 'CO_ANO'], as_index=False).sum()

#Colocamos a tabela na ordem da Quantidade de "Kg Estatística", em ordem decrescente, separado por estados e apenas os três primeiros
mais_importados = mais_importados.sort_values(by='QT_ESTAT', ascending=False).groupby('SG_UF_NCM').head(3)

#Apenas Retiramos a ordem (chamada de Index) listada anterior
mais_importados = mais_importados.reset_index(drop=True)




#Separamos os produtos por estados
mais_exportados = export_total.groupby(['SG_UF_NCM', 'CO_NCM', 'CO_ANO'], as_index=False).sum()

#Colocamos a tabela na ordem da Quantidade de "Kg Estatística", em ordem decrescente, separado por estados e apenas os três primeiros
mais_exportados = mais_exportados.sort_values(by='QT_ESTAT', ascending=False).groupby('SG_UF_NCM').head(3)

#Apenas Retiramos a ordem listada anterior
mais_exportados = mais_exportados.reset_index(drop=True)


#Renomeando as colunas de acordo com o site de referência para melhor entendimento
mais_importados.rename(columns={

    'CO_ANO'        :   'Ano' ,
    'CO_MES'        :   'Mes',
    'CO_NCM'        :   'Cod. NCM',
    'CO_UNID'       :   'Cod. Unid. Estatistica',
    'CO_PAIS'       :   'Cod. pais destino/origem',
    'SG_UF_NCM'     :   'Cod. UF origem/destino',
    'CO_VIA'        :   'Cod. via transporte',
    'CO_URF'        :   'Cod. URF embarque/desembarque',
    'QT_ESTAT'      :   'Kg estatistica',
    'KG_LIQUIDO'    :   'Kg liquido',
    'VL_FOB'        :   'Valor FOB (US$)',
    'VL_FRETE'      :   'Valor Frete',
    'VL_SEGURO'     :   'Valor Seguro'

}, inplace= True)

mais_exportados.rename(columns={

    'CO_ANO'        :   'Ano' ,
    'CO_MES'        :   'Mes',
    'CO_NCM'        :   'Cod. NCM',
    'CO_UNID'       :   'Cod. Unid. Estatistica',
    'CO_PAIS'       :   'Cod. pais destino/origem',
    'SG_UF_NCM'     :   'Cod. UF origem/destino',
    'CO_VIA'        :   'Cod. via transporte',
    'CO_URF'        :   'Cod. URF embarque/desembarque',
    'QT_ESTAT'      :   'Kg estatistica',
    'KG_LIQUIDO'    :   'Kg liquido',
    'VL_FOB'        :   'Valor FOB (US$)',
    'VL_FRETE'      :   'Valor Frete',
    'VL_SEGURO'     :   'Valor Seguro'

}, inplace= True)


# Gráfico de barras para os top 3 produtos mais importados por estado nos anos de 2020 e 2021
fig_importacao = px.bar(mais_importados, x='Cod. UF origem/destino', y='Cod. NCM', color = 'Kg estatistica', title='Top 3 Produtos Mais Importados por Estado')

# Gráfico de barras para os top 3 produtos mais exportados por estado nos anos de 2020 e 2021
fig_exportacao = px.bar(mais_exportados, x='Cod. UF origem/destino', y='Cod. NCM', color = 'Kg estatistica', title='Top 3 Produtos Mais Exportados por Estado')


#Iremos utilizar a tabela de exportações de 2021 para a realização desta parte
#Criei uma nova variávelp com o a tabela de exportações de 2021 por organização e facilitar o entendimento
expMes = pd.read_csv('EXP_2021.csv', sep = ';')

#Subdividindo a tabela de acordo com o estado, o mês e o cód. do produto
expMes = expMes.groupby(['SG_UF_NCM', 'CO_MES',  'CO_NCM' ], as_index=False).sum()

expMes = expMes.sort_values(by=['QT_ESTAT', 'CO_MES' ], ascending=False).groupby('SG_UF_NCM').head(3)

expMes = expMes.reset_index(drop=True)


#Renomeando as colunas de acordo com o site de referência para melhor entendimento
expMes.rename(columns={

    'CO_ANO'        :   'Ano' ,
    'CO_MES'        :   'Mes',
    'CO_NCM'        :   'Cod. NCM',
    'CO_UNID'       :   'Cod. Unid. Estatistica',
    'CO_PAIS'       :   'Cod. pais destino/origem',
    'SG_UF_NCM'     :   'Cod. UF origem/destino',
    'CO_VIA'        :   'Cod. via transporte',
    'CO_URF'        :   'Cod. URF embarque/desembarque',
    'QT_ESTAT'      :   'Kg estatistica',
    'KG_LIQUIDO'    :   'Kg liquido',
    'VL_FOB'        :   'Valor FOB (US$)',
    'VL_FRETE'      :   'Valor Frete',
    'VL_SEGURO'     :   'Valor Seguro'

}, inplace= True)


# Gráfico de barras para os top 3 produtos mais importados por estado nos anos de 2020 e 2021
fig_expMes = px.bar(expMes, x='Cod. UF origem/destino', y='Cod. NCM', color = 'Kg estatistica', title='Top 3 Produtos Mais Exportados por mês de 2021 por Estado')


#Unindo os três gráficos
fig = make_subplots(rows=3, cols=1, subplot_titles=('Exportações 2020/2021', 'Importações 2020/2021', 'Exportações 2020 por mês'))

# Adicionar as figuras aos subplots
for i, fig_px in enumerate([fig_exportacao, fig_importacao, fig_expMes], start=1):
    for trace in fig_px.data:
        fig.add_trace(trace, row=i, col=1)

# Atualizar título do layout
fig.update_layout(title_text="Dashboard")

# Mostrar o painel
fig.show()
