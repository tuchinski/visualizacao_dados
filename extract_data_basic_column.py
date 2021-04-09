import requests
import json


def get_data_api(url):
    """
        Busca os dados na API, e transforma o JSON pra um dict de Python
    """
    json_raw = requests.get(url)
    return json.loads(json_raw.text)

def main():
    """
        Nesse a gente vai extrair os dados da categoria da ofensa, pra mostrar
        num grafico de barras
    """
    dados_json = get_data_api('https://data.cityofnewyork.us/resource/bqiq-cu78.json')

    # Os condados de NY
    counties = {}
    categoria_ofensa = []

    for dado in dados_json:

        # add as categorias num array, pq todos os bairros tem que ter todas
        # as categorias, msm que não tenha nenhum crime daquela categoria
        cat_ofensa_atual = dado['offense_category']
        if cat_ofensa_atual not in categoria_ofensa:
            categoria_ofensa.append(cat_ofensa_atual)

        # Caso ainda não tenha aparecido o condado
        if dado['county'] not in counties:
            counties[dado['county']] = {}
            counties[dado['county']][dado['offense_category']] = 1    

        # Caso o condado já tenha aparecido, mas ainda não apareceu um crime desta categoria
        elif dado['offense_category'] not in counties[dado['county']]:
            counties[dado['county']][dado['offense_category']] = 1    

        counties[dado['county']][dado['offense_category']] += 1 
    
    finalera = []

    for categoria in categoria_ofensa:
        data = []
        for bairro in counties:
            if categoria not in counties[bairro]:
                counties[bairro][categoria] = 0
            data.append(counties[bairro][categoria])
        finalera.append({
            'name': categoria,
            'data': data
        })
    print (finalera)

    # ! esse comentado inverte o gráfico

    # for bairro in counties:
    #     data = []
    #     # Coloca todas as categorias que n tem naquele bairro com o valor 
    #     for categoria in categoria_ofensa:
    #         if categoria not in counties[bairro]:
    #             counties[bairro][categoria] = 0
    #         # data.append(counties[bairro][categoria])

    #     finalera.append({
    #         'name': categoria,
    #         'data': data
    #     })
    # print(json.dumps(finalera,indent=4))
    
    json_retorno = {
        "chart": {
            "type": 'column'
        },
        "title": {
            "text": 'Crimes de ódio em NYC'
        },
        "subtitle": {
            "text": 'Categoria da Ofensa por bairro'
        },
        "series": finalera,
        "xAxis": {
            'categories': list(counties.keys())
        },
        'yAxis': {
            'min': 0,
            'title': {
                "text": 'Quantidade crimes'
            }
        },
        'tooltip': {
        'headerFormat': '<span style="font-size:10px">{point.key}</span><table>',
        'pointFormat': '<tr><td style="color:{series.color};padding:0">{series.name}: </td>' +
            '<td style="padding:0"><b>{point.y} mm</b></td></tr>',
        'footerFormat': '</table>',
        'shared': True,
        'useHTML': True
        },
        'plotOptions': {
            'column': {
                'pointPadding': 0.2,
                'borderWidth': 0
            }
        },
    }
    
    
    # print(categoria_ofensa)

    with open('basic_column.json','w') as file:
        # file.write(json.dumps(finalera,indent=4))
        file.write(json.dumps(json_retorno,indent=4))






if __name__ == "__main__" :
    main()