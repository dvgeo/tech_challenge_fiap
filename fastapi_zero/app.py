import requests
from bs4 import BeautifulSoup

from http import HTTPStatus
from fastapi import FastAPI
from fastapi.responses import HTMLResponse # seu eu quisesse retornar um html

from fastapi_zero.schemas import Message

app = FastAPI()


def parse_vitibrasil_data_producao(url):
    url = 'http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_02'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Encontra a tabela específica na página
    table = soup.find('table', class_='tb_base tb_dados')

    # Cria um dicionário vazio para armazenar os dados extraídos
    data = {}
    # Define uma variável para armazenar a categoria atual
    # (inicialmente vazia)
    current_category = None

    # Itera por cada linha da tabela
    for row in table.find_all('tr'):
        # Encontra todas as células (<td>) da linha atual
        cells = row.find_all('td')

        # Verifica se a linha possui exatamente duas células
        # (esperado para dados)
        if len(cells) == 2:
            # Verifica se a primeira célula possui a classe "tb_item"
            # (indica categoria principal)
            if cells[0].get('class') == ['tb_item']:
                # Extrai o texto da célula (nome da categoria) e
                # remove espaços em branco
                current_category = cells[0].text.strip()
                # Cria um novo dicionário vazio dentro do dicionário
                # principal para armazenar subcategorias e volumes
                data[current_category] = {}
            # Verifica se a primeira célula possui a classe
            #  "tb_subitem" (indica subcategoria)
            elif cells[0].get('class') == ['tb_subitem']:
                # Extrai o texto da célula (nome da subcategoria)
                # e remove espaços em branco
                subcategory = cells[0].text.strip()
                # Extrai o texto da célula (volume) e remove espaços
                # em branco
                volume = (
                    cells[1].text.strip()
                )  # (Comentário sobre conversão para float removido)
                # Adiciona a subcategoria e seu volume correspondente ao
                # dicionário da categoria atual
                data[current_category][subcategory] = volume

    # Retorna o dicionário final contendo as categorias, subcategorias
    # e volumes
    return data


def parse_vitibrasil_data_processamento1(url):
    url = 'http://vitibrasil.cnpuv.embrapa.br/index.php?subopcao=subopt_01&opcao=opt_03'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Encontra a tabela específica na página
    table = soup.find('table', class_='tb_base tb_dados')

    # Cria um dicionário vazio para armazenar os dados extraídos
    data = {}
    # Define uma variável para armazenar a categoria atual
    # (inicialmente vazia)
    current_category = None

    # Itera por cada linha da tabela
    for row in table.find_all('tr'):
        # Encontra todas as células (<td>) da linha atual
        cells = row.find_all('td')

        # Verifica se a linha possui exatamente duas células
        # (esperado para dados)
        if len(cells) == 2:
            # Verifica se a primeira célula possui a classe
            # "tb_item" (indica categoria principal)
            if cells[0].get('class') == ['tb_item']:
                # Extrai o texto da célula (nome da categoria)
                # e remove espaços em branco
                current_category = cells[0].text.strip()
                # Cria um novo dicionário vazio dentro do dicionário
                # principal para armazenar subcategorias e volumes
                data[current_category] = {}
            # Verifica se a primeira célula possui a classe
            # "tb_subitem" (indica subcategoria)
            elif cells[0].get('class') == ['tb_subitem']:
                # Extrai o texto da célula (nome da subcategoria)
                # e remove espaços em branco
                subcategory = cells[0].text.strip()
                # Extrai o texto da célula (volume) e remove espaços
                #  em branco
                volume = (
                    cells[1].text.strip()
                )  # (Comentário sobre conversão para float removido)
                # Adiciona a subcategoria e seu volume correspondente
                # ao dicionário da categoria atual
                data[current_category][subcategory] = volume

    # Retorna o dicionário final contendo as categorias, subcategorias
    # e volumes
    return data


def parse_vitibrasil_data_processamento2(url):
    url = 'http://vitibrasil.cnpuv.embrapa.br/index.php?subopcao=subopt_02&opcao=opt_03'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Encontra a tabela específica na página
    table = soup.find('table', class_='tb_base tb_dados')

    # Cria um dicionário vazio para armazenar os dados extraídos
    data = {}
    # Define uma variável para armazenar a categoria atual
    # (inicialmente vazia)
    current_category = None

    # Itera por cada linha da tabela
    for row in table.find_all('tr'):
        # Encontra todas as células (<td>) da linha atual
        cells = row.find_all('td')

        # Verifica se a linha possui exatamente duas células
        # (esperado para dados)
        if len(cells) == 2:
            # Verifica se a primeira célula possui a classe "tb_item"
            # (indica categoria principal)
            if cells[0].get('class') == ['tb_item']:
                # Extrai o texto da célula (nome da categoria) e
                # remove espaços em branco
                current_category = cells[0].text.strip()
                # Cria um novo dicionário vazio dentro do dicionário
                # principal para armazenar subcategorias e volumes
                data[current_category] = {}
            # Verifica se a primeira célula possui a classe "tb_subitem"
            # (indica subcategoria)
            elif cells[0].get('class') == ['tb_subitem']:
                # Extrai o texto da célula (nome da subcategoria) e
                # remove espaços em branco
                subcategory = cells[0].text.strip()
                # Extrai o texto da célula (volume) e remove espaços em branco
                volume = (
                    cells[1].text.strip()
                )  # (Comentário sobre conversão para float removido)
                # Adiciona a subcategoria e seu volume correspondente
                # ao dicionário da categoria atual
                data[current_category][subcategory] = volume

    # Retorna o dicionário final contendo as categorias, subcategorias
    # e volumes
    return data


def parse_vitibrasil_data_processamento3(url):
    url = 'http://vitibrasil.cnpuv.embrapa.br/index.php?subopcao=subopt_03&opcao=opt_03'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Encontra a tabela específica na página
    table = soup.find('table', class_='tb_base tb_dados')

    # Cria um dicionário vazio para armazenar os dados extraídos
    data = {}
    # Define uma variável para armazenar a categoria atual
    # (inicialmente vazia)
    current_category = None

    # Itera por cada linha da tabela
    for row in table.find_all('tr'):
        # Encontra todas as células (<td>) da linha atual
        cells = row.find_all('td')

        # Verifica se a linha possui exatamente duas células
        # (esperado para dados)
        if len(cells) == 2:
            # Verifica se a primeira célula possui a classe "tb_item"
            # (indica categoria principal)
            if cells[0].get('class') == ['tb_item']:
                # Extrai o texto da célula (nome da categoria) e
                # remove espaços em branco
                current_category = cells[0].text.strip()
                # Cria um novo dicionário vazio dentro do dicionário
                # principal para armazenar subcategorias e volumes
                data[current_category] = {}
            # Verifica se a primeira célula possui a classe "tb_subitem"
            # (indica subcategoria)
            elif cells[0].get('class') == ['tb_subitem']:
                # Extrai o texto da célula (nome da subcategoria) e
                # remove espaços em branco
                subcategory = cells[0].text.strip()
                # Extrai o texto da célula (volume) e remove espaços
                # em branco
                volume = (
                    cells[1].text.strip()
                )  # (Comentário sobre conversão para float removido)
                # Adiciona a subcategoria e seu volume correspondente
                # ao dicionário da categoria atual
                data[current_category][subcategory] = volume

    # Retorna o dicionário final contendo as categorias, subcategorias
    # e volumes
    return data


def parse_vitibrasil_data_processamento4(url):
    url = 'http://vitibrasil.cnpuv.embrapa.br/index.php?subopcao=subopt_04&opcao=opt_03'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Encontra a tabela específica na página
    table = soup.find('table', class_='tb_base tb_dados')

    # Cria um dicionário vazio para armazenar os dados extraídos
    data = {}
    # Define uma variável para armazenar a categoria atual
    # (inicialmente vazia)
    current_category = None

    # Itera por cada linha da tabela
    for row in table.find_all('tr'):
        # Encontra todas as células (<td>) da linha atual
        cells = row.find_all('td')

        # Verifica se a linha possui exatamente duas células
        # (esperado para dados)
        if len(cells) == 2:
            # Verifica se a primeira célula possui a classe "tb_item"
            # (indica categoria principal)
            if cells[0].get('class') == ['tb_item']:
                # Extrai o texto da célula (nome da categoria) e
                # remove espaços em branco
                current_category = cells[0].text.strip()
                # Cria um novo dicionário vazio dentro do dicionário
                # principal para armazenar subcategorias e volumes
                data[current_category] = {}
            # Verifica se a primeira célula possui a classe "tb_subitem"
            # (indica subcategoria)
            elif cells[0].get('class') == ['tb_subitem']:
                # Extrai o texto da célula (nome da subcategoria) e
                # remove espaços em branco
                subcategory = cells[0].text.strip()
                # Extrai o texto da célula (volume) e remove espaços
                # em branco
                volume = (
                    cells[1].text.strip()
                )  # (Comentário sobre conversão para float removido)
                # Adiciona a subcategoria e seu volume correspondente
                # ao dicionário da categoria atual
                data[current_category][subcategory] = volume

    # Retorna o dicionário final contendo as categorias, subcategorias e
    # volumes
    return data


def parse_vitibrasil_data_comercializacao(url):
    url = 'http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_04'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Encontra a tabela específica na página
    table = soup.find('table', class_='tb_base tb_dados')

    # Cria um dicionário vazio para armazenar os dados extraídos
    data = {}
    # Define uma variável para armazenar a categoria atual
    # (inicialmente vazia)
    current_category = None

    # Itera por cada linha da tabela
    for row in table.find_all('tr'):
        # Encontra todas as células (<td>) da linha atual
        cells = row.find_all('td')

        # Verifica se a linha possui exatamente duas células
        # (esperado para dados)
        if len(cells) == 2:
            # Verifica se a primeira célula possui a classe "tb_item"
            # (indica categoria principal)
            if cells[0].get('class') == ['tb_item']:
                # Extrai o texto da célula (nome da categoria) e
                # remove espaços em branco
                current_category = cells[0].text.strip()
                # Cria um novo dicionário vazio dentro do
                # dicionário principal para armazenar subcategorias e volumes
                data[current_category] = {}
            # Verifica se a primeira célula possui a classe
            # "tb_subitem" (indica subcategoria)
            elif cells[0].get('class') == ['tb_subitem']:
                # Extrai o texto da célula (nome da subcategoria) e
                # remove espaços em branco
                subcategory = cells[0].text.strip()
                # Extrai o texto da célula (volume) e remove espaços em branco
                volume = (
                    cells[1].text.strip()
                )  # (Comentário sobre conversão para float removido)
                # Adiciona a subcategoria e seu volume correspondente
                # ao dicionário da categoria atual
                data[current_category][subcategory] = volume

    # Retorna o dicionário final contendo as categorias, subcategorias e
    # volumes
    return data


def parse_vitibrasil_importacao_vinhos(url):
    """
    Extracts country data from the Vitibrasil website table.

    Args:
        url (str): URL of the Vitibrasil webpage containing the table.

    Returns:
        list: List of dictionaries containing country data
        (name, quantity, value).
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    table = soup.find('table', class_='tb_base tb_dados')
    data = {}

    for row in table.find_all('tr')[1:]:  # Skip header row
        cells = row.find_all('td')
        country = cells[0].text.strip()
        quantity = cells[
            1
        ].text.strip()  # .replace('.', '')) if cells[1].text else None
        value = cells[
            2
        ].text.strip()  # .replace('.', '')) if cells[2].text else None
        data[country] = {'quantidade': quantity, 'valor': value}

    return data


def parse_vitibrasil_importacao_espumantes(url):
    """
    Extracts country data from the Vitibrasil website table.

    Args:
        url (str): URL of the Vitibrasil webpage containing the table.

    Returns:
        list: List of dictionaries containing country data 
        (name, quantity, value).
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    table = soup.find('table', class_='tb_base tb_dados')
    data = {}

    for row in table.find_all('tr')[1:]:  # Skip header row
        cells = row.find_all('td')
        country = cells[0].text.strip()
        quantity = cells[
            1
        ].text.strip()  # .replace('.', '')) if cells[1].text else None
        value = cells[
            2
        ].text.strip()  # .replace('.', '')) if cells[2].text else None
        data[country] = {'quantidade': quantity, 'valor': value}

    return data


def parse_vitibrasil_importacao_uvas_frescas(url):
    """
    Extracts country data from the Vitibrasil website table.

    Args:
        url (str): URL of the Vitibrasil webpage containing the table.

    Returns:
        list: List of dictionaries containing country data 
        (name, quantity, value).
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    table = soup.find('table', class_='tb_base tb_dados')
    data = {}

    for row in table.find_all('tr')[1:]:  # Skip header row
        cells = row.find_all('td')
        country = cells[0].text.strip()
        quantity = cells[
            1
        ].text.strip()  # .replace('.', '')) if cells[1].text else None
        value = cells[
            2
        ].text.strip()  # .replace('.', '')) if cells[2].text else None
        data[country] = {'quantidade': quantity, 'valor': value}

    return data


def parse_vitibrasil_importacao_uvas_passas(url):
    """
    Extracts country data from the Vitibrasil website table.

    Args:
        url (str): URL of the Vitibrasil webpage containing the table.

    Returns:
        list: List of dictionaries containing country data 
        (name, quantity, value).
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    table = soup.find('table', class_='tb_base tb_dados')
    data = {}

    for row in table.find_all('tr')[1:]:  # Skip header row
        cells = row.find_all('td')
        country = cells[0].text.strip()
        quantity = cells[
            1
        ].text.strip()  # .replace('.', '')) if cells[1].text else None
        value = cells[
            2
        ].text.strip()  # .replace('.', '')) if cells[2].text else None
        data[country] = {'quantidade': quantity, 'valor': value}

    return data


def parse_vitibrasil_importacao_suco_uva(url):
    """
    Extracts country data from the Vitibrasil website table.

    Args:
        url (str): URL of the Vitibrasil webpage containing the table.

    Returns:
        list: List of dictionaries containing country data 
        (name, quantity, value).
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    table = soup.find('table', class_='tb_base tb_dados')
    data = {}

    for row in table.find_all('tr')[1:]:  # Skip header row
        cells = row.find_all('td')
        country = cells[0].text.strip()
        quantity = cells[
            1
        ].text.strip()  # .replace('.', '')) if cells[1].text else None
        value = cells[
            2
        ].text.strip()  # .replace('.', '')) if cells[2].text else None
        data[country] = {'quantidade': quantity, 'valor': value}

    return data


def parse_vitibrasil_exportacao_vinhos(url):
    """
    Extracts country data from the Vitibrasil website table.

    Args:
        url (str): URL of the Vitibrasil webpage containing the table.

    Returns:
        list: List of dictionaries containing country data 
        (name, quantity, value).
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    table = soup.find('table', class_='tb_base tb_dados')
    data = {}

    for row in table.find_all('tr')[1:]:  # Skip header row
        cells = row.find_all('td')
        country = cells[0].text.strip()
        quantity = cells[
            1
        ].text.strip()  # .replace('.', '')) if cells[1].text else None
        value = cells[
            2
        ].text.strip()  # .replace('.', '')) if cells[2].text else None
        data[country] = {'quantidade': quantity, 'valor': value}

    return data


def parse_vitibrasil_exportacao_espumantes(url):
    """
    Extracts country data from the Vitibrasil website table.

    Args:
        url (str): URL of the Vitibrasil webpage containing the table.

    Returns:
        list: List of dictionaries containing country data 
        (name, quantity, value).
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    table = soup.find('table', class_='tb_base tb_dados')
    data = {}

    for row in table.find_all('tr')[1:]:  # Skip header row
        cells = row.find_all('td')
        country = cells[0].text.strip()
        quantity = cells[
            1
        ].text.strip()  # .replace('.', '')) if cells[1].text else None
        value = cells[
            2
        ].text.strip()  # .replace('.', '')) if cells[2].text else None
        data[country] = {'quantidade': quantity, 'valor': value}

    return data


def parse_vitibrasil_exportacao_uvas_frescas(url):
    """
    Extracts country data from the Vitibrasil website table.

    Args:
        url (str): URL of the Vitibrasil webpage containing the table.

    Returns:
        list: List of dictionaries containing country data 
        (name, quantity, value).
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    table = soup.find('table', class_='tb_base tb_dados')
    data = {}

    for row in table.find_all('tr')[1:]:  # Skip header row
        cells = row.find_all('td')
        country = cells[0].text.strip()
        quantity = cells[
            1
        ].text.strip()  # .replace('.', '')) if cells[1].text else None
        value = cells[
            2
        ].text.strip()  # .replace('.', '')) if cells[2].text else None
        data[country] = {'quantidade': quantity, 'valor': value}

    return data


def parse_vitibrasil_exportacao_suco_uva(url):
    """
    Extracts country data from the Vitibrasil website table.

    Args:
        url (str): URL of the Vitibrasil webpage containing the table.

    Returns:
        list: List of dictionaries containing country data 
        (name, quantity, value).
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    table = soup.find('table', class_='tb_base tb_dados')
    data = {}

    for row in table.find_all('tr')[1:]:  # Skip header row
        cells = row.find_all('td')
        country = cells[0].text.strip()
        quantity = cells[
            1
        ].text.strip()  # .replace('.', '')) if cells[1].text else None
        value = cells[
            2
        ].text.strip()  # .replace('.', '')) if cells[2].text else None
        data[country] = {'quantidade': quantity, 'valor': value}

    return data


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Olá mundo'}
    '''return """
    <html>
        <head>
            <title> Nosso olá mundo!</title>
        </head>
        <body>
            <h1>Olá Mundo</h1>
        </body>  
    </html>"""'''

# print(read_root())
@app.get('/producao')
async def obter_producao():
    url = 'http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_02'
    data = parse_vitibrasil_data_producao(url)
    return data


@app.get('/processamento/viniferas')
async def obter_processamento_vinifera():
    url = 'http://vitibrasil.cnpuv.embrapa.br/index.php?subopcao=subopt_01&opcao=opt_03'
    data = parse_vitibrasil_data_processamento1(url)
    return data


@app.get('/processamento/americanas_hibridas')
async def obter_processamento_americanas_hibridas():
    url = 'http://vitibrasil.cnpuv.embrapa.br/index.php?subopcao=subopt_02&opcao=opt_03'
    data = parse_vitibrasil_data_processamento2(url)
    return data


@app.get('/processamento/uvas')
async def obter_processamento_uvas():
    """
    Busca dados do país na tabela de processamento de uvas 
    do Vitibrasil e retorna como JSON.
    """
    url = 'http://vitibrasil.cnpuv.embrapa.br/index.php?subopcao=subopt_03&opcao=opt_03'
    data = parse_vitibrasil_data_processamento3(url)
    return data


@app.get('/processamento/sem_classificacao')
async def obter_processamento_sem_classificacao():
    url = 'http://vitibrasil.cnpuv.embrapa.br/index.php?subopcao=subopt_04&opcao=opt_03'
    data = parse_vitibrasil_data_processamento4(url)
    return data


@app.get('/comercializacao')
async def obter_comercializacao():
    url = 'http://vitibrasil.cnpuv.embrapa.br/index.php?subopcao=subopt_04&opcao=opt_03'
    data = parse_vitibrasil_data_comercializacao(url)
    return data


@app.get('/importacao/vinhos')
async def obter_importacao_vinhos():
    """
    Busca dados do país na tabela de importação de vinhos 
    do Vitibrasil e retorna como JSON.
    """
    url = 'http://vitibrasil.cnpuv.embrapa.br/index.php?subopcao=subopt_01&opcao=opt_05'
    data = parse_vitibrasil_importacao_vinhos(url)
    return data


@app.get('/importacao/espumantes')
async def obter_importacao_espumantes():
    """
    Busca dados do país na tabela de importação de espumantes 
    do Vitibrasil e retorna como JSON.
    """
    url = 'http://vitibrasil.cnpuv.embrapa.br/index.php?subopcao=subopt_02&opcao=opt_05'
    data = parse_vitibrasil_importacao_espumantes(url)
    return data


@app.get('/importacao/uvas_frescas')
async def obter_importacao_uvas_frescas():
    """
    Busca dados do país na tabela de importação de uvas frescas 
    do Vitibrasil e retorna como JSON.
    """
    url = 'http://vitibrasil.cnpuv.embrapa.br/index.php?subopcao=subopt_03&opcao=opt_05'
    data = parse_vitibrasil_importacao_uvas_frescas(url)
    return data


@app.get('/importacao/uvas_passas')
async def obter_importacao_uvas_passas():
    """
    Busca dados do país na tabela de importação de uvas passas 
    do Vitibrasil e retorna como JSON.
    """
    url = 'http://vitibrasil.cnpuv.embrapa.br/index.php?subopcao=subopt_04&opcao=opt_05'
    data = parse_vitibrasil_importacao_uvas_passas(url)
    return data


@app.get('/importacao/suco_uva')
async def obter_importacao_suco_uva():
    """
    Busca dados do país na tabela de importação de suco de uva 
    do Vitibrasil e retorna como JSON.
    """
    url = 'http://vitibrasil.cnpuv.embrapa.br/index.php?subopcao=subopt_05&opcao=opt_05'
    data = parse_vitibrasil_importacao_uvas_frescas(url)
    return data


@app.get('/exportacao/vinhos')
async def obter_exportacao_vinhos():
    """
    Busca dados do país na tabela de exportação de vinhos 
    do Vitibrasil e retorna como JSON.
    """
    url = 'http://vitibrasil.cnpuv.embrapa.br/index.php?subopcao=subopt_01&opcao=opt_06'
    data = parse_vitibrasil_exportacao_vinhos(url)
    return data


@app.get('/exportacao/espumantes')
async def obter_exportacao_espumantes():
    """
    Busca dados do país na tabela de exportação de espumantes 
    do Vitibrasil e retorna como JSON.
    """
    url = 'http://vitibrasil.cnpuv.embrapa.br/index.php?subopcao=subopt_02&opcao=opt_06'
    data = parse_vitibrasil_exportacao_espumantes(url)
    return data


@app.get('/exportacao/uvas_frescas')
async def obter_exportacao_uvas_frescas():
    """
    Busca dados do país na tabela de exportação de uvas frescas 
    do Vitibrasil e retorna como JSON.
    """
    url = 'http://vitibrasil.cnpuv.embrapa.br/index.php?subopcao=subopt_03&opcao=opt_06'
    data = parse_vitibrasil_exportacao_uvas_frescas(url)
    return data


@app.get('/exportacao/suco_uva')
async def obter_exportacao_suco_uva():
    """
    Busca dados do país na tabela de exportação de suco de uva 
    do Vitibrasil e retorna como JSON.
    """
    url = 'http://vitibrasil.cnpuv.embrapa.br/index.php?subopcao=subopt_04&opcao=opt_06'
    data = parse_vitibrasil_exportacao_suco_uva(url)
    return data
