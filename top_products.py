import requests
from bs4 import BeautifulSoup
import pandas as pd

SITE_URL = "https://lista.mercadolivre.com.br/placa-wifi#D[A:placa%20wifi]"
FINAL_PRODUCTS = {
  "Nome": [],
  "Preço": [],
}

site_content = requests.get(SITE_URL).text
soup = BeautifulSoup(site_content, "html.parser")
div_produtos = soup.select(".ui-search-layout.ui-search-layout--grid li")

for p in div_produtos:
  try:
    product_name = p.select_one(".ui-search-item__title").text
    product_price = float(p.select_one(".andes-money-amount__fraction").text)

    FINAL_PRODUCTS["Nome"].append(product_name)
    FINAL_PRODUCTS["Preço"].append(product_price)
  except:
    continue

print(FINAL_PRODUCTS)

df = pd.DataFrame(FINAL_PRODUCTS).sort_values(by="Preço", ascending=False)

# Escrever o DataFrame em um arquivo Excel
caminho_arquivo = 'produtos.xlsx'
with pd.ExcelWriter(caminho_arquivo, engine='xlsxwriter') as writer:
    df.to_excel(writer, index=False, sheet_name='Produtos')
    workbook  = writer.book
    worksheet = writer.sheets['Produtos']

    # Ajustar a largura das colunas para o tamanho do texto
    for i, col in enumerate(df.columns):
        column_len = max(df[col].astype(str).apply(len).max(), len(col) + 2)
        worksheet.set_column(i, i, column_len)

    currency_format = workbook.add_format({'num_format': 'R$ #,##0.00'})
    worksheet.set_column(df.columns.get_loc('Preço'), df.columns.get_loc('Preço'), None, currency_format)