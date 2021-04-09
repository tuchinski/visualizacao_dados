# -*- coding: utf-8 -*
import requests
import json

# categorias = {
#     '50 YEARS OLD OR MORE' :{
#         'traducao': "50+ ANOS",
#         'qtde' = 0,
#         'color' = '#14ebce'
#     } 
#     'ANTI-MULTI RACIAL GROUPS' :{
#         'traducao': "ANTI MULTI GRUPOS RACIAIS",
#         'qtde' = 0,
#         'color' = '#eb0b4c'
#     } 
#     'ANTI-BLACK' :{
#         'traducao': "ANTI-NEGROS",
#         'qtde' = 0,
#         'color' = '#b7450e'
#     } 
#     'ANTI-OTHER ETHNICITY' :{
#         'traducao': "ANTI OUTROS GRUPOS ETINICOS",
#         'qtde' = 0,
#         'color' = '#07c4d3'
#     } 
#     'ANTI-LGBT(MIXED GROUP)' :{
#         'traducao': "ANTI LGBT (GRUPOS MISTOS)",
#         'qtde' = 0,
#         'color' = '#4e8c0a'
#     } 
#     'ANTI-ARAB' :{
#         'traducao': "ANTI-ARÁBICOS",
#         'qtde' = 0,
#         'color' = '#b76ec4'
#     } 
#     'ANTI-OTHER RELIGION' :{
#         'traducao': "ANTI OUTRAS RELIGIÕES",
#         'qtde' = 0,
#         'color' = '#f40325'
#     } 
#     'ANTI-FEMALE' :{
#         'traducao': "DISCRIMINACAO CONTRA MULHER",
#         'qtde' = 0,
#         'color' = '#529803'
#     } 
#     'ANTI-RELIGIOUS PRACTICE GENERALLY' :{
#         'traducao': "ANTI-PRÁTICAS RELIGIOSAS",
#         'qtde' = 0,
#         'color' = '#4bcc24'
#     } 
#     'ANTI-MALE HOMOSEXUAL(GAY)' :{
#         'traducao': "ANTI-HOMOSSEXSUAIS(HOMENS)",
#         'qtde' = 0,
#         'color' = '#50385b'
#     } 
#     'ANTI-JEWISH' :{
#         'traducao': "ANTISSEMITISMO",
#         'qtde' = 0,
#         'color' = '#cbb896'
#     } 
#     'ANTI-ISLAMIC(MUSLIM)' :{
#         'traducao': "ANTI-ISLÂMICOS",
#         'qtde' = 0,
#         'color' = '#c8fe61'
#     } 
#     'ANTI-CATHOLIC' :{
#         'traducao': "ANTI-CATÓLICOS",
#         'qtde' = 0,
#         'color' = '#94265c'
#     } 
#     'ANTI-ASIAN' :{
#         'traducao': "ANTI-ASIÁTICOS",
#         'qtde' = 0,
#         'color' = '#774c67'
#     } 
#     'ANTI-BUDDHIST' :{
#         'traducao': "ANTI-BUDISTAS",
#         'qtde' = 0,
#         'color' = '#b93726'
#     } 
#     'ANTI-HINDU' :{
#         'traducao': "ANTI-HINDUS",
#         'qtde' = 0,
#         'color' = '#8b81f0'
#     } 
#     'ANTI-HISPANIC' :{
#         'traducao': "ANTI-HISPÂNICOS",
#         'qtde' = 0,
#         'color' = '#585048'
#     } 
#     'OTHER' :{
#         'traducao': "OUTROS",
#         'qtde' = 0,
#         'color' = '#c213f2'
#     } 
#     'ANTI-WHITE' :{
#         'traducao': "ANTI-BRANCOS",
#         'qtde' = 0,
#         'color' = '#e5786c'
#     } 
#     'ANTI-TRANSGENDER' :{
#         'traducao': "ANTI-TRANSGÊNEROS",
#         'qtde' = 0,
#         'color' = '#b94d41'
#     } 
#     'ANTI-GENDER NON CONFORMING' :{
#         'traducao': "ANTI-GENERO VARIANTE",
#         'qtde' = 0,
#         'color' = '#eb0dc7'
#     } 
#     'ANTI-JEHOVAS WITNESS' :{
#         'traducao': "ANTI-TESTEMUNHAS DE GEOVÁ",
#         'qtde' = 0,
#         'color' = '#8d9ff7'
#     } 
#     'ANTI-PHYSICAL DISABILITY' :{
#         'traducao': "ANTI-DEFICIENTES",
#         'qtde' = 0,
#         'color' = '#f19237'
#     } 
#     'ANTI-FEMALE HOMOSEXUAL(GAY)' :{
#         'traducao': "ANTI-HOMOSSEXUAIS(MULHER)",
#         'qtde' = 0,
#         'color' = '#b4c92b'
#     } 
# }

categorias = {
    '50 YEARS OLD OR MORE' :[
        "50+ ANOS",
        0,
        '#14ebce',
        "50+ ANOS",
    ], 
    'ANTI-MULTI RACIAL GROUPS' :[
        "MULTI GRUPOS RACIAIS",
        0,
        '#eb0b4c',
        "MULTI GRUPOS RACIAIS",
    ], 
    'ANTI-BLACK' :[
        "NEGROS",
        0,
        '#b7450e',
        "NEGROS",
    ], 
    'ANTI-OTHER ETHNICITY' :[
        "OUTROS GRUPOS ETINICOS",
        0,
        '#07c4d3',
        "OUTROS GRUPOS ETINICOS",
    ], 
    'ANTI-LGBT(MIXED GROUP)' :[
        "LGBT (GRUPOS MISTOS)",
        0,
        '#4e8c0a',
        "LGBT (GRUPOS MISTOS)",
    ], 
    'ANTI-ARAB' :[
        "ARÁBICOS",
        0,
        '#b76ec4',
        "ARÁBICOS",
    ], 
    'ANTI-OTHER RELIGION' :[
        "OUTRAS RELIGIÕES",
        0,
        '#f40325',
        "OUTRAS RELIGIÕES",
    ], 
    'ANTI-FEMALE' :[
        "DISCRIMINACAO CONTRA MULHER",
        0,
        '#529803',
        "DISCRIMINACAO CONTRA MULHER",
    ], 
    'ANTI-RELIGIOUS PRACTICE GENERALLY' :[
        "PRÁTICAS RELIGIOSAS",
        0,
        '#4bcc24',
        "PRÁTICAS RELIGIOSAS",
    ], 
    'ANTI-MALE HOMOSEXUAL(GAY)' :[
        "HOMOSSEXSUAIS(HOMENS)",
        0,
        '#50385b',
        "HOMOSSEXSUAIS(HOMENS)",
    ], 
    'ANTI-JEWISH' :[
        "ANTISSEMITISMO",
        0,
        '#cbb896',
        "ANTISSEMITISMO",
    ], 
    'ANTI-ISLAMIC(MUSLIM)' :[
        "ISLÂMICOS",
        0,
        '#c8fe61',
        "ISLÂMICOS",
    ], 
    'ANTI-CATHOLIC' :[
        "CATÓLICOS",
        0,
        '#94265c',
        "CATÓLICOS",
    ], 
    'ANTI-ASIAN' :[
        "ASIÁTICOS",
        0,
        '#774c67',
        "ASIÁTICOS",
    ], 
    'ANTI-BUDDHIST' :[
        "BUDISTAS",
        0,
        '#b93726',
        "BUDISTAS",
    ], 
    'ANTI-HINDU' :[
        "HINDUS",
        0,
        '#8b81f0',
        "HINDUS",
    ], 
    'ANTI-HISPANIC' :[
        "HISPÂNICOS",
        0,
        '#585048',
        "HISPÂNICOS",
    ], 
    'OTHER' :[
        "OUTROS",
        0,
        '#c213f2',
        "OUTROS",
    ], 
    'ANTI-WHITE' :[
        "BRANCOS",
        0,
        '#e5786c',
        "BRANCOS",
    ], 
    'ANTI-TRANSGENDER' :[
        "TRANSGÊNEROS",
        0,
        '#b94d41',
        "TRANSGÊNEROS",
    ], 
    'ANTI-GENDER NON CONFORMING' :[
        "GENERO VARIANTE",
        0,
        '#eb0dc7',
        "GENERO VARIANTE",
    ], 
    'ANTI-JEHOVAS WITNESS' :[
        "TESTEMUNHAS DE GEOVÁ",
        0,
        '#8d9ff7',
        "TESTEMUNHAS DE GEOVÁ",
    ], 
    'ANTI-PHYSICAL DISABILITY' :[
        "DEFICIENTES",
        0,
        '#f19237',
        "DEFICIENTES",
    ], 
    'ANTI-FEMALE HOMOSEXUAL(GAY)' :[
        "HOMOSSEXUAIS(MULHER)",
        0,
        '#b4c92b',
        "HOMOSSEXUAIS(MULHER)",
    ],
    'NAO-CLASSIFICADO': [
        "NÃO CLASSIFICADO",
        0,
        '#06a3e3'
        "NÃO CLASSIFICADO",
    ]
}

def main():
    json_raw = requests.get('https://data.cityofnewyork.us/resource/bqiq-cu78.json')
    dados_json = json.loads(json_raw.text)

    for dado in dados_json:
        # print(json.dumps(dado,indent=4))
        try:
            categorias[dado['bias_motive_description']][1] += 1 
        except KeyError:
            categorias['NAO-CLASSIFICADO'][1] += 1
    # print(json.dumps(categorias,ensure_ascii=False))
    print(list(categorias.values()))
    

    # categorias_crime_odio = [dado['county'] for dado in dados_json if 'county' in dado]
    # print(','.join(categorias_crime_odio))


    with open('data_parliament.json','w') as file:
        # file.write(json.dumps(categorias,indent=4,ensure_ascii=False))
        file.write(json.dumps(list(categorias.values()),indent=4,ensure_ascii=False))
        # file.write()

        # for i in range(0,len(categorias_crime_odio)):
        #     categorias_crime_odio[i] = categorias[categorias_crime_odio[i]]
        # file.write(','.join(categorias_crime_odio))
    
    # with open('tipos_categorias.txt','w') as file:
    #     file.write("\n".join(list(set(categorias_crime_odio))))

if __name__ == "__main__":
    main()