# -*- coding: utf-8 -*
import requests
import json

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
        try:
            categorias[dado['bias_motive_description']][1] += 1 
        except KeyError:
            categorias['NAO-CLASSIFICADO'][1] += 1
    print(list(categorias.values()))
    


    with open('data_parliament.json','w') as file:
        file.write(json.dumps(list(categorias.values()),indent=4,ensure_ascii=False))


if __name__ == "__main__":
    main()