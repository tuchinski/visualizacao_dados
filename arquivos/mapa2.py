import json
import requests
from main_primeiro_mapa import metadados, nome_patrulha, remove_zero_esquerda


def main():
    url_dados_coords = "https://data.cityofnewyork.us/resource/2fra-mtpn.json"
    response = requests.get(url_dados_coords)
    dados_coords = json.loads(response.text)

    url_api_dados_crime = "https://data.cityofnewyork.us/resource/bqiq-cu78.json"
    dados_brutos = requests.get(url_api_dados_crime)
    dict_dados_json = json.loads(dados_brutos.text)

    geojson_export = {
        "type": "FeatureCollection",
        "features": []
    }

    for crime in dict_dados_json:
        for crime_coords in dados_coords:
            if crime["law_code_category_description"] == crime_coords["law_cat_cd"]:
                print("1")
                if crime["record_create_date"] == crime_coords["cmplnt_fr_dt"]:
                    print("2")
                    if crime["complaint_precinct_code"] == crime_coords["addr_pct_cd"]:
                        print("3")
                        if crime["offense_description"] == crime_coords["ofns_desc"]:
                            print("4")
                            feature = {
                                "type": "Feature",
                                "properties": {
                                    "name": crime_coords["ofns_desc"],
                                    "pct": crime_coords["addr_pct_cd"],
                                    "county": crime_coords["boro_nm"],
                                    "patrol_borough_name": crime["patrol_borough_name"]
                                },

                            }
                            geojson_export["features"].append(feature)

    with open("mapinha.geojson", "w") as arq:
        arq.write(json.dumps(geojson_export))


if __name__ == '__main__':
    main()
    print("FIM")
