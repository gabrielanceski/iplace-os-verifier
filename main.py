from requests import get
from bs4 import BeautifulSoup
from win11toast import notify
from dotenv import load_dotenv
import os

load_dotenv()

OS_NUMBER = os.getenv('NUMERO_OS')
DOCUMENT = os.getenv('CPF')

if (OS_NUMBER == None or DOCUMENT == None):
    print('Erro ao obter variáveis de ambiente.')
    exit(1)

INFO_ROW = 4
STATUS_ROW = 3
TABLE_CLASS = 'tabDados'
TABLE_LABEL = 'tabLabel'
URL = f'https://at.lojaiplace.com.br/Detalhes.aspx?ID_OrdemServico={OS_NUMBER}&cpf={DOCUMENT}'

print(URL)

def append_row_data(row_index, rows):
    global result

    if (row_index >= len(rows)):
        result += 'Não foi possível obter informações da OS.\n'
        return

    row = rows[row_index]
    label_cols = row.find_all('td', class_=TABLE_LABEL)
    value_cols = [col.find_next_sibling('td') for col in label_cols]
    
    for index, col in enumerate(label_cols):
        result += col.text + ' ' + value_cols[index].text + '\n'

try:
    response = get(URL)
except Exception as e:
    print('Erro ao obter status da OS.')
    exit(1)

html_soup = BeautifulSoup(response.text, 'html.parser')
table = html_soup.find('table', class_=TABLE_CLASS)

result = ''

rows = table.find_all('tr')
append_row_data(INFO_ROW, rows)
append_row_data(STATUS_ROW, rows)


notify(f'Dados da O.S. nº {OS_NUMBER}', result, on_click=URL)
