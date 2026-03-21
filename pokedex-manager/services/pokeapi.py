import requests

BASE_URL = "https://pokeapi.co/api/v2/"

def buscar_pokemon(nome_ou_id):
    try:
        url = f"{BASE_URL}/pokemon/{str(nome_ou_id).lower()}"
        response = requests.get(url)
        if response.status_code == 404:
            return None
        response.raise_for_status()
        data = response.json()
        
        return {
            'id': data['id'],
            'nome': data['name'],
            'tipo': data['types'] [0] ['type']['name'],
            'imagem_url': data['sprites']['front_default'],
            'altura': data['height'],
            'peso': data['weight'],
        }
    except requests.RequestException as e:
        print(f"Erro ao buscar Pokémon: {e}")
        return None