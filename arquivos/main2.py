import json
import requests
from requests.models import Response

metadados = {
    "MISDEMEANOR": {
        "traducao": "CRIME DE MENOR GRAVIDADE",
        "color": "orange"
    },
    "FELONY": {
        "traducao": "CRIME DE MENOR GRAVIDADE",
        "color": "red"
    },
    "VIOLATION": {
        "traducao": "VIOLAÇÃO",
        "color": "blue"
    },
    "INVESTIGATION": {
        "traducao": "INVESTIGAÇÃO",
        "color": "purple"
    },
    "NO_CRIMES": {
        "traducao": "SEM CRIMES",
        "color": "green"
    }

}

categoria_ofensa = {
    "Age": {
        "Qtd": [0,0,0,0,0,0,0,0,0,0,0,0]        
    },
    "Disability": {
        "Qtd": [0,0,0,0,0,0,0,0,0,0,0,0] 
    },
    "Ethnicity/National Origin/Ancestry": {
        "Qtd": [0,0,0,0,0,0,0,0,0,0,0,0] 
    },
    "Gender": {
        "Qtd": [0,0,0,0,0,0,0,0,0,0,0,0] 
    },
    "Race/Color": {
        "Qtd": [0,0,0,0,0,0,0,0,0,0,0,0] 
    },
    "Religion/Religious Practice": {
        "Qtd": [0,0,0,0,0,0,0,0,0,0,0,0] 
    },
    "Sexual Orientation": {
        "Qtd": [0,0,0,0,0,0,0,0,0,0,0,0] 
    }
}

mes = {
    '1': {
        'Nome': "janeiro"
    },
    '2': {
        'Nome': "fevereiro"
    },
    '3': {
        'Nome': "março"
    },
    '4': {
        'Nome': "abril"
    },
    '5': {
        'Nome': "maio"
    },
    '6': {
        'Nome': "junho"
    },
    '7': {
        'Nome': "julho"
    },
    '8': {
        'Nome': "agosto"
    },
    '9': {
        'Nome': "setembro"
    },
    '10': {
        'Nome': "outubro"
    },
    '11': {
        'Nome': "novembro"
    },
    '12': {
        'Nome': "dezembro"
    }
}


def busca_crime():
    url_api = "https://data.cityofnewyork.us/resource/bqiq-cu78.json"
    response = requests.get(url_api)
    dados_crimes = json.loads(response.text)

    for crime in dados_crimes:
        categoria_ofensa[crime["offense_category"]]["Qtd"][(int(crime["month_number"]))-1] += 1

    retorno = []
    for cat_crime in categoria_ofensa:
        crime_atual = {
            "name": cat_crime,
            "data": categoria_ofensa[cat_crime]["Qtd"]
        }
        retorno.append(crime_atual)
    print(json.dumps(retorno, indent=4))


if __name__ == '__main__':
    #main()
    busca_crime()