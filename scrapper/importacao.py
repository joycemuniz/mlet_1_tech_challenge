import requests
from bs4 import BeautifulSoup
import time

# URL base com o parâmetro de ano e subopcao
BASE_URL = "http://vitibrasil.cnpuv.embrapa.br/index.php?ano={ano}&subopcao={subopcao}&opcao=opt_05"

# Função que limpa e transforma os valores
def parse_valor(valor_str):
    valor_str = valor_str.strip().replace(".", "").replace(",", "")
    if valor_str == "-" or valor_str == "":
        return None
    return int(valor_str)

# Função principal de raspagem para cada ano
def raspar_dados_por_ano(ano, subopcao):
    url = BASE_URL.format(ano=ano, subopcao=subopcao)
    response = requests.get(url)
    response.encoding = "utf-8"
    soup = BeautifulSoup(response.content, 'html.parser')

    tabela = soup.find("table", class_="tb_base tb_dados")
    if not tabela:
        return None

    linhas = tabela.find("tbody").find_all("tr")
    dados = []

    for linha in linhas:
        colunas = linha.find_all("td")
        if len(colunas) != 3:
            continue

        pais = colunas[0].get_text(strip=True)
        quantidade = parse_valor(colunas[1].get_text())
        valor = parse_valor(colunas[2].get_text())

        dados.append({
            "pais": pais,
            "quantidade_kg": quantidade,
            "valor_usd": valor
        })

    return {
        "ano": ano,
        "dados": dados
    }

# Função para coletar dados em um intervalo de anos
def coletar_dados_importacao(subopcao, ano_inicio=1970, ano_fim=2025):
    dados_importacao_json = []
    for ano in range(ano_inicio, ano_fim + 1):
        dados_ano = raspar_dados_por_ano(ano, subopcao)
        if dados_ano:
            dados_importacao_json.append(dados_ano)
        time.sleep(0.005)
    return dados_importacao_json