from django.shortcuts import render
from deep_translator import GoogleTranslator

import requests

def obter_personagens(api_url="https://last-airbender-api.fly.dev/api/v1/characters"):
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Erro na requisição: {e}")
        return None

def traduzir_atributos(personagens):
    translator = GoogleTranslator(source='en', target='pt')
    traducao_personagens = []

    for character in personagens:
        try:
            name_translated = translator.translate(character['name'])
            affiliation_translated = translator.translate(character.get('affiliation', 'Desconhecido'))
            # Tradução de aliados e inimigos
            allies = character.get('allies', [])
            enemies = character.get('enemies', [])

            allies_translated = [translator.translate(ally) for ally in allies] if allies else ['Nenhum']
            enemies_translated = [translator.translate(enemy) for enemy in enemies] if enemies else ['Nenhum']
        except Exception as e:
            print(f"Erro ao traduzir: {e}")
            name_translated = character['name']
            affiliation_translated = character.get('affiliation', 'Desconhecido')
            allies_translated = ['Nenhum']
            enemies_translated = ['Nenhum']
        

        traducao_personagens.append({
            "name": name_translated,
            "affiliation": affiliation_translated,
            "allies": allies_translated,
            "enemies": enemies_translated,
        })

    return traducao_personagens

def exibir_personagens(request):
    personagens = obter_personagens()
    personagens_traduzidos = traduzir_atributos(personagens) if personagens else []
    return render(request, 'personagens.html', {'personagens': personagens_traduzidos})
