# Importe os pacotes necessários
import pandas as pd
import seaborn as sns

# Ler o arquivo csv
data = pd.read_csv('gasolina.csv')

# crie o gráfico 
with sns.axes_style('darkgrid'):
  grafico_gasolina = sns.lineplot(
      x = 'dia',
      y = 'venda',
      data = data
  )

  grafico_gasolina.set(
      title = 'Preço médio de venda da gasolina na cidade de São Paulo nos 10 primeiros dias de Julho de 2021',
      xlabel = 'Dia',
      ylabel = 'Preço (R$)'
  )
