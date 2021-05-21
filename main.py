import json
import requests

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

nome_patrulha = {
    "PBBN": {
        "nome": "PATROL BORO BKLYN NORTH",
        "county": "Kings"
    },
    "PBBS": {
        "nome": "PATROL BORO BKLYN SOUTH",
        "county": "Kings"
    },
    "PBBX": {
        "nome": "PATROL BORO BRONX",
        "county": "Bronx"
    },
    "PBMN": {
        "nome": "PATROL MAN NORTH",
        "county": "New York"
    },
    "PBMS": {
        "nome": "PATROL BORO MAN SOUTH",
        "county": "New York"
    },
    "PBQN": {
        "nome": "PATROL BORO QUEENS NORTH",
        "county": "Queens"
    },
    "PBQS": {
        "nome": "PATROL BORO QUEENS SOUTH",
        "county": "Queens"
    },
    "PBSI": {
        "nome": "PATROL BORO STATEN ISLAND",
        "county": "Richmond"
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


def main():
    url_api_dados_crime = "https://data.cityofnewyork.us/resource/bqiq-cu78.json"
    dados_brutos = requests.get(url_api_dados_crime)

    dados_tratados = {}

    dict_dados_json = json.loads(dados_brutos.text)

    for crime in dict_dados_json:
        try:
            dados_tratados[crime["complaint_precinct_code"]][crime["law_code_category_description"]] += 1
        except KeyError:
            if crime['complaint_precinct_code'] not in dados_tratados.keys():
                dados_tratados[crime["complaint_precinct_code"]] = {}

            dados_tratados[crime["complaint_precinct_code"]][crime["law_code_category_description"]] = 1

    # print(json.dumps(dados_tratados,indent=4))

    dados_mapa = "https://data.cityofnewyork.us/resource/5rqd-h5ci.json"

    dados_mapa_bruto = requests.get(dados_mapa)
    dados_mapa_json = json.loads(dados_mapa_bruto.text)

    geojson_export = {
        "type": "FeatureCollection",
        "features": []
    }

    for local in dados_mapa_json:
        maior_crime, maior_qtde = encontra_maior_crime(dados_tratados, local["pct"])

        feature = {
            "type": "Feature",
            "properties": {
                "name": "Precinct {}".format(local['pct']),
                "pct": local["pct"],
                "sector": local["sector"],
                "maior_crime": maior_crime,
                "fill": metadados[maior_crime]["color"],
                "qtde": maior_qtde,
                "county": nome_patrulha[local["patrol_bor"]]["county"],
                "patrol_borough_name": nome_patrulha[local["patrol_bor"]]["nome"]
            },
            "geometry": local["the_geom"]
        }
        geojson_export["features"].append(feature)

    with open("new_geojson.geojson", "w") as arq:
        arq.write(json.dumps(geojson_export))

    print("THE END")


if __name__ == '__main__':
    main()
