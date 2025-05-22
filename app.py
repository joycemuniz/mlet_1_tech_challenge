from flask import Flask, jsonify, request
from flasgger import Swagger
from auth import auth
from scrapper.exportacao import coletar_dados_exportacao
from scrapper.importacao import coletar_dados_importacao
from scrapper.producao import coletar_dados_producao
from scrapper.comercializacao import coletar_dados_comercializacao
from scrapper.processamento import coletar_dados_processamento

app = Flask(__name__)

app.config['SWAGGER'] = {
    'title': 'API de Dados Vitivinícolas',
    'uiversion': 3
}

swagger = Swagger(app)

@app.route('/')
@auth.login_required
def home():
    """
    Endpoint principal.
    ---
    responses:
      200:
        description: Retorna mensagem de boas-vindas.
    """
    return "Olá, seja bem vindo a API de dados Vitivinícolas!"

@app.route('/producao', methods=['GET'])
@auth.login_required
def get_dados_producao_filtrado():
    """
    Consulta dados de produção. Para melhorar a performance utilize os parâmetros de datas.
    ---
    parameters:
      - name: ano_inicio
        in: query
        type: integer
        required: false
        description: Ano inicial da consulta.
      - name: ano_fim
        in: query
        type: integer
        required: false
        description: Ano final da consulta.
    responses:
      200:
        description: Dados de produção no intervalo de anos.
      400:
        description: Erro de validação de parâmetros.
    """
    try:
        ano_inicio = int(request.args.get('ano_inicio', 1970))
        ano_fim = int(request.args.get('ano_fim', 2024))
        if ano_inicio > ano_fim:
            return jsonify({"erro": "ano_inicio não pode ser maior que ano_fim"}), 400
        data = coletar_dados_producao(ano_inicio, ano_fim)
        return jsonify(data)
    except ValueError:
        return jsonify({"erro": "Parâmetros de ano inválidos. Use inteiros para ano_inicio e ano_fim."}), 400

@app.route('/processamento/<categoria>', methods=['GET'])
@auth.login_required
def get_dados_processamento(categoria):
    """
    Consulta dados de processamento por categoria. Para melhorar a performance utilize também os parâmetros de datas.
    ---
    parameters:
      - name: categoria
        in: path
        type: string
        enum: [viniferas, americanas_hibridas, uvas_mesa, sem_classificacao]
        required: true
        description: Categoria de processamento.
      - name: ano_inicio
        in: query
        type: integer
        required: false
        description: Ano inicial da consulta.
      - name: ano_fim
        in: query
        type: integer
        required: false
        description: Ano final da consulta.
    responses:
      200:
        description: Dados de processamento.
      400:
        description: Categoria inválida ou erro de parâmetros.
    """
    subopcao_map = {
        "viniferas": "subopt_01",
        "americanas_hibridas": "subopt_02",
        "uvas_mesa": "subopt_03",
        "sem_classificacao": "subopt_04"
    }

    subopcao = subopcao_map.get(categoria)
    if not subopcao:
        return jsonify({"erro": "Categoria inválida. Use: viniferas, americanas_hibridas, uvas_mesa ou sem_classificacao"}), 400

    try:
        ano_inicio = int(request.args.get('ano_inicio', 1970))
        ano_fim = int(request.args.get('ano_fim', 2025))
        if ano_inicio > ano_fim:
            return jsonify({"erro": "ano_inicio não pode ser maior que ano_fim"}), 400
    except ValueError:
        return jsonify({"erro": "Parâmetros de ano inválidos. Use inteiros para ano_inicio e ano_fim."}), 400

    data = coletar_dados_processamento(subopcao, ano_inicio, ano_fim)
    return jsonify(data)

@app.route('/comercializacao', methods=['GET'])
@auth.login_required
def get_dados_comercializacao_2():
    """
    Consulta de dados de comercialização. Para melhorar a performance utilize os parâmetros de datas.
    ---
    parameters:
      - name: ano_inicio
        in: query
        type: integer
        required: false
        description: Ano inicial da consulta.
      - name: ano_fim
        in: query
        type: integer
        required: false
        description: Ano final da consulta.
    responses:
      200:
        description: Dados de comercialização no intervalo.
      400:
        description: Erro de validação de parâmetros.
    """
    try:
        ano_inicio = int(request.args.get('ano_inicio', 1970))
        ano_fim = int(request.args.get('ano_fim', 2024))
        if ano_inicio > ano_fim:
            return jsonify({"erro": "ano_inicio não pode ser maior que ano_fim"}), 400
        data = coletar_dados_comercializacao(ano_inicio, ano_fim)
        return jsonify(data)
    except ValueError:
        return jsonify({"erro": "Parâmetros de ano inválidos. Use inteiros para ano_inicio e ano_fim."}), 400

@app.route('/importacao/<categoria>', methods=['GET'])
@auth.login_required
def get_dados_importacao(categoria):
    """
    Consulta dados de importação por categoria. Para melhorar a performance utilize também os parâmetros de datas.
    ---
    parameters:
      - name: categoria
        in: path
        type: string
        enum: [vinhos_mesa, espumantes, uvas_frescas, uvas_passas, sucos]
        required: true
        description: Categoria de importação.
      - name: ano_inicio
        in: query
        type: integer
        required: false
        description: Ano inicial da consulta.
      - name: ano_fim
        in: query
        type: integer
        required: false
        description: Ano final da consulta.
    responses:
      200:
        description: Dados de importação.
      400:
        description: Categoria inválida ou erro de parâmetros.
    """
    subopcao_map = {
        "vinhos_mesa": "subopt_01",
        "espumantes": "subopt_02",
        "uvas_frescas": "subopt_03",
        "uvas_passas": "subopt_04",
        "sucos": "subopt_05"
    }

    subopcao = subopcao_map.get(categoria)
    if not subopcao:
        return jsonify({"erro": "Categoria inválida. Use: vinhos_mesa, espumantes, uvas_frescas, uvas_passas ou sucos"}), 400

    try:
        ano_inicio = int(request.args.get('ano_inicio', 1970))
        ano_fim = int(request.args.get('ano_fim', 2025))
        if ano_inicio > ano_fim:
            return jsonify({"erro": "ano_inicio não pode ser maior que ano_fim"}), 400
    except ValueError:
        return jsonify({"erro": "Parâmetros de ano inválidos. Use inteiros para ano_inicio e ano_fim."}), 400

    data = coletar_dados_importacao(subopcao, ano_inicio, ano_fim)
    return jsonify(data)

@app.route('/exportacao/<categoria>', methods=['GET'])
@auth.login_required
def get_dados_exportacao(categoria):
    """
    Consulta dados de exportação por categoria. Para melhorar a performance utilize também os parâmetros de datas.
    ---
    parameters:
      - name: categoria
        in: path
        type: string
        enum: [vinhos_mesa, espumantes, uvas_frescas, sucos]
        required: true
        description: Categoria de exportação.
      - name: ano_inicio
        in: query
        type: integer
        required: false
        description: Ano inicial da consulta.
      - name: ano_fim
        in: query
        type: integer
        required: false
        description: Ano final da consulta.
    responses:
      200:
        description: Dados de exportação.
      400:
        description: Categoria inválida ou erro de parâmetros.
    """
    subopcao_map = {
        "vinhos_mesa": "subopt_01",
        "espumantes": "subopt_02",
        "uvas_frescas": "subopt_03",
        "sucos": "subopt_04"
    }

    subopcao = subopcao_map.get(categoria)
    if not subopcao:
        return jsonify({"erro": "Categoria inválida. Use: vinhos_mesa, espumantes, uvas_frescas ou sucos"}), 400

    try:
        ano_inicio = int(request.args.get('ano_inicio', 1970))
        ano_fim = int(request.args.get('ano_fim', 2025))
        if ano_inicio > ano_fim:
            return jsonify({"erro": "ano_inicio não pode ser maior que ano_fim"}), 400
    except ValueError:
        return jsonify({"erro": "Parâmetros de ano inválidos. Use inteiros para ano_inicio e ano_fim."}), 400

    data = coletar_dados_exportacao(subopcao, ano_inicio, ano_fim)
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)

