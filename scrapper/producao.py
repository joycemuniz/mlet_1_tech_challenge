import requests
from bs4 import BeautifulSoup
import json
import time

# URL base com o parâmetro de ano e opção
BASE_URL = "http://vitibrasil.cnpuv.embrapa.br/index.php?ano={ano}&opcao=opt_02"

# Função que limpa e transforma os valores
def parse_valor(valor_str):
    valor_str = valor_str.strip().replace(".", "").replace(",", "")
    return int(valor_str) if valor_str.isdigit() else None

# Função principal de raspagem para cada ano
def raspar_dados_por_ano(ano):
    url = BASE_URL.format(ano=ano)
    response = requests.get(url)
    response.encoding = "utf-8"
    soup = BeautifulSoup(response.content, 'html.parser')
    
    tabela = soup.find("table", class_="tb_base tb_dados")
    if not tabela:
        return None 
    
    dados_por_item = {}
    linhas = tabela.find_all("tr")
    
    item_atual = None
    for linha in linhas:
        colunas = linha.find_all("td")
        if len(colunas) != 2:
            continue

        nome = colunas[0].get_text(strip=True)
        valor = parse_valor(colunas[1].get_text())

        # Detecta se é um novo item
        if "tb_item" in colunas[0].get("class", []):
            item_atual = nome
            if item_atual not in dados_por_item:
                dados_por_item[item_atual] = []
        else:
            if item_atual:
                dados_por_item[item_atual].append({
                    "sub-item": nome,
                    "quantidade_litros": valor
                })

    # Monta estrutura do json separado por ano e item
    return {
        "ano": ano,
        "itens": [
            {
                "item": item,
                "sub-itens": subitens
            }
            for item, subitens in dados_por_item.items()
        ]
    }
#Fazendo a raspagem dos dados no periodo escolhido ou default 1970 a 2025


def coletar_dados_producao(ano_inicio=1970,ano_fim=2025):
    dados_producao_json = []
    for ano in range(ano_inicio, ano_fim + 1):
        dados_ano = raspar_dados_por_ano(ano)
        if dados_ano:
            dados_producao_json.append(dados_ano)
        time.sleep(1)
    return dados_producao_json
