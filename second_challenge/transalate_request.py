import json
import requests

from googletrans import Translator

def obter_personagens(api_url="https://last-airbender-api.fly.dev/api/v1/characters"):
     """
    Faz uma requisição GET para a API de Avatar e retorna os dados dos personagens.
    
    Parameters:
        api_url (str): URL da API para obter informações dos personagens.
    
    Returns:
        list: Lista de personagens em JSON, ou None em caso de falha.
    """
     try:
          response = requests.get(api_url)
          response.raise_for_status() # verifica se houve algum erro na requisição
          return response.json()
     except requests.exceptions.RequestException as e:
         print(f"Erro na requisição: {e}")
         return None

def exibir_personagens(personagens):
    """
    Exibe os personagens no console de forma formatada.
    
    Parameters:
        personagens (list): Lista de personagens em JSON.
    """
    if personagens:
        print(json.dumps(personagens, indent=4, ensure_ascii=False))
    else:
        print("Nenhum personagem encontrado.")
        
def main():
    personagens = obter_personagens()
    exibir_personagens(personagens)

if __name__ == "__main__":
    main()

def traduzir_atributos(personagens):
    translator = Translator()
    for character in personagens:
        name_translated = translator.translate(character['name'], src='en', dest='pt').text
        affiliation_translated = translator.translate(character.get('affiliation', 'Desconhecido'), src='en', dest='pt').text
        print(f"Nome: {name_translated}, Afiliação: {affiliation_translated}")

def main():
    personagens = obter_personagens()  # Chama a função que obtém os personagens
    if personagens:
        traduzir_atributos(personagens)  # Traduz e imprime os dados

if __name__ == "__main__":
    main()
