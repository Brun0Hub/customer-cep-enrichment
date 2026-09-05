import requests

def get_cep_data(cep: str):
    cep = ''.join(filter(str.isdigit, str(cep)))

    if len(cep) != 8:
        return None
    
    url = f"https://viacep.com.br/ws/{cep}/json/"
    
    try:
        response = requests.get(url)
        response.raise_for_status()

        data = response.json()

        if "erro" in data:
            return None
        
        return data
    
    except:
        return None