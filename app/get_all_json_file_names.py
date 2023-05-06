import os
import json
def get_json_files(path):
    directory_path = path

    # define extensão
    json_ext = ".json"

    # Lista para adicionar nomes dos arquivos json
    file_names = []

    # Loop para buscar por todos os nomes dos files .json do diretorio
    for filename in os.listdir(directory_path):
        # Obtem cada um dos arquivos
        _, ext = os.path.splitext(filename)
        # Se a extensão for json adiciona na lista todos os arquivos
        if ext == json_ext:
            file_names.append(filename)

    file_paths = []

    for name in file_names:
         # Associa nome do arquivo com o path dele
        file_path = os.path.join(directory_path, name)
        # adiciona na lista somente o path
        file_paths.append(file_path)
    
    # Retorna a lista com o paths dos arquivos json
    return file_paths

#print(get_json_files('../data'))
        

def extract_text_elements(data):
    """
    Função que extrai elementos de texto e seus bounds de um arquivo JSON
    :param data: Dicionário contendo a hierarquia de elementos do arquivo JSON
    :return: Lista de dicionários contendo as propriedades de "text" e "bounds" dos elementos de texto
    """
    text_elements = []
    
    # Verifica se a hierarquia de elementos é uma lista
    if isinstance(data, list):
        for item in data:
            text_elements += extract_text_elements(item)
            
    # Verifica se a hierarquia de elementos é um dicionário
    elif isinstance(data, dict):
        # Verifica se o elemento é de texto
        if 'text' in data:
            # Adiciona as propriedades de "text" e "bounds" a lista de resultados
            text_element = {'text': data.get('text', ''), 'bounds': data.get('bounds', []),'visible': data.get('visible-to-user','')}
            if text_element["visible"]:
              text_elements.append(text_element)
        
        # Chama a função recursivamente para continuar a busca por elementos de texto na hierarquia
        for key, value in data.items():
            text_elements += extract_text_elements(value)
    
    return text_elements

def extract_text_from_all_json_files(file_path_list):
    text_list = []
    # loop para percorrer toda a lista de nomes de arquivos
    for path in file_path_list:
        # insere o nome como string para obter o arquivo correspondente
        with open(path) as f:
            data = json.load(f)
        # executa o metodo para extrair os textos de cada um dos arquivos json da lista
        text_elements = extract_text_elements(data)
        # adiciona o texto encontrado em cada arquivo json ao vetor de texto
        for text in text_elements:
            # se não for valor vazio ele adiciona setando somente a propriedade de text
            if text["text"] != "":
                text_list.append(text["text"])
        print(text_list)

extract_text_from_all_json_files(get_json_files('../data'))
