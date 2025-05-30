import aiohttp
import asyncio
from bs4 import BeautifulSoup

BASE_URL = "http://vitibrasil.cnpuv.embrapa.br/index.php?ano={ano}&opcao=opt_02"

# Função que limpa e transforma os valores
def parse_valor(valor_str):
    valor_str = valor_str.strip().replace(".", "").replace(",", "")
    return int(valor_str) if valor_str.isdigit() else None

# Extrai os dados HTML para cada ano
def extrair_dados_html(html, ano):
    soup = BeautifulSoup(html, 'html.parser')
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

# Função assíncrona para buscar HTML
async def fetch(session, ano):
    url = BASE_URL.format(ano=ano)
    async with session.get(url) as response:
        html = await response.text()
        return extrair_dados_html(html, ano)

# Coletor assíncrono de dados
async def coletar_dados_producao_async(ano_inicio=1970, ano_fim=2025):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, ano) for ano in range(ano_inicio, ano_fim + 1)]
        resultados = await asyncio.gather(*tasks)
        return [r for r in resultados if r is not None]

# Interface síncrona para uso no Flask
def coletar_dados_producao(ano_inicio=1970, ano_fim=2025):
    return asyncio.run(coletar_dados_producao_async(ano_inicio, ano_fim))
