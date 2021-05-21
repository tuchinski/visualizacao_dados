import json
import requests

categoria_ofensa = {
    "Age": {
        "color": "orange",
        "Qtd": [0,0,0,0,0,0,0,0,0,0,0,0]
    },
    "Disability": {
        "color": "red",
        "Qtd": [0,0,0,0,0,0,0,0,0,0,0,0]
    },
    "Ethnicity/National Origin/Ancestry": {
        "color": "blue",
        "Qtd": [0,0,0,0,0,0,0,0,0,0,0,0]
    },
    "Gender": {
        "color": "purple",
        "Qtd": [0,0,0,0,0,0,0,0,0,0,0,0]
    },
    "Race/Color": {
        "color": "red",
        "Qtd": [0,0,0,0,0,0,0,0,0,0,0,0]
    },
    "Religion/Religious Practice": {
        "color": "pink",
        "Qtd": [0,0,0,0,0,0,0,0,0,0,0,0]
    },
    "Sexual Orientation": {
        "color": "yellow",
        "Qtd": [0,0,0,0,0,0,0,0,0,0,0,0]
    },
    "NO_CRIMES":{
        "color": "white"
    }
}


def remove_zero_esquerda(pct):
    while pct[0] == "0":
        pct = pct[1:]
    return pct


def encontra_maior_crime(dict_dados_json, pct):
    pct = remove_zero_esquerda(pct)
    # if pct[0] == "0":
    #     pct = pct[1:]
    if pct not in dict_dados_json.keys():
        return ("NO_CRIMES", 0)
    dado_atual = dict_dados_json[pct]
    maior_nome = None
    maior_qtde = -1

    for crime in dado_atual:
        if dado_atual[crime] > maior_qtde:
            maior_qtde = dado_atual[crime]
            maior_nome = crime

    return maior_nome, maior_qtde

url_api = "https://data.cityofnewyork.us/resource/bqiq-cu78.json"
response = requests.get(url_api)
dados_crimes = json.loads(response.text)

dados_tratados = {}

for crime in dados_crimes:
    teste = "offense_category"
    try:
        dados_tratados[crime["complaint_precinct_code"]][crime[teste]] += 1
    except KeyError:
        if crime['complaint_precinct_code'] not in dados_tratados.keys():
            dados_tratados[crime["complaint_precinct_code"]] = {}

        dados_tratados[crime["complaint_precinct_code"]][crime[teste]] = 1

dados_mapa = "https://data.cityofnewyork.us/resource/kmub-vria.json"

dados_mapa_bruto = requests.get(dados_mapa)
dados_mapa_json = json.loads(dados_mapa_bruto.text)

geojson_export = {
    "type": "FeatureCollection",
    "features": []
}

for local in dados_mapa_json:
    maior_crime, maior_qtde = encontra_maior_crime(dados_tratados, local["precinct"])
    maior_crime = maior_crime
    feature = {
            "type": "Feature",
            "properties": {
                "name": "Precinct {}".format(local['precinct']),
                "precinct": local["precinct"],
                "maior_crime": maior_crime,
                "fill": categoria_ofensa[maior_crime]["color"],
                "qtde": maior_qtde
            },
            "geometry": local["the_geom"]
        }
    geojson_export["features"].append(feature)

with open("mapa2.geojson", "w") as arq:
        arq.write(json.dumps(geojson_export))

print("acabou")