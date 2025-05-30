import aiohttp
import asyncio
from bs4 import BeautifulSoup

BASE_URL = "http://vitibrasil.cnpuv.embrapa.br/index.php?ano={ano}&subopcao={subopcao}&opcao=opt_05"

# Limpa e transforma os valores
def parse_valor(valor_str):
    valor_str = valor_str.strip().replace(".", "").replace(",", "")
    if valor_str == "-" or valor_str == "":
        return None
    return int(valor_str)

# Função que extrai dados da tabela HTML
def extrair_dados_html(html, ano):
    soup = BeautifulSoup(html, 'html.parser')
    tabela = soup.find("table", class_="tb_base tb_dados")
    if not tabela or not tabela.find("tbody"):
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

async def fetch(session, ano, subopcao):
    url = BASE_URL.format(ano=ano, subopcao=subopcao)
    async with session.get(url) as response:
        html = await response.text()
        return extrair_dados_html(html, ano)

async def coletar_dados_importacao_async(subopcao, ano_inicio=1970, ano_fim=2025):
    async with aiohttp.ClientSession() as session:
        tarefas = [fetch(session, ano, subopcao) for ano in range(ano_inicio, ano_fim + 1)]()