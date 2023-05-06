import json
from get_all_json_file_names import get_json_list 
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

def extract_text_from_all_json_files(file_name_list):
    text_list = []
    # loop para percorrer toda a lista de nomes de arquivos
    for file in file_name_list:
        # insere o nome como string para obter o arquivo correspondente
        with open(file) as f:
            data = json.load(f)
        # executa o metodo para extrair os textos de cada um dos arquivos json da lista
        text_elements = extract_text_elements(data)
        # adiciona o texto encontrado em cada arquivo json ao vetor de texto
        for text in text_elements:
            # se não for valor vazio ele adiciona setando somente a propriedade de text
            if text["text"] != "":
                text_list.append(text["text"])
        print(text_list)

extract_text_from_all_json_files(get_json_list('../data'))