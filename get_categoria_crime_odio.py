import requests
import json

categorias = {
    '50 YEARS OLD OR MORE' : "50+ ANOS",
    'ANTI-MULTI RACIAL GROUPS' : "ANTI MULTI GRUPOS RACIAIS",
    'ANTI-BLACK' : "ANTI-NEGROS",
    'ANTI-OTHER ETHNICITY' : "ANTI OUTROS GRUPOS ETINICOS",
    'ANTI-LGBT(MIXED GROUP)' : "ANTI LGBT (GRUPOS MISTOS)",
    'ANTI-ARAB' : "ANTI-ARÁBICOS",
    'ANTI-OTHER RELIGION' : "ANTI OUTRAS RELIGIÕES",
    'ANTI-FEMALE' : "DISCRIMINACAO CONTRA MULHER",
    'ANTI-RELIGIOUS PRACTICE GENERALLY' : "ANTI-PRÁTICAS RELIGIOSAS",
    'ANTI-MALE HOMOSEXUAL(GAY)' : "ANTI-HOMOSSEXSUAIS(HOMENS)",
    'ANTI-JEWISH' : "ANTISSEMITISMO",
    'ANTI-ISLAMIC(MUSLIM)' : "ANTI-ISLÂMICOS",
    'ANTI-CATHOLIC' : "ANTI-CATÓLICOS",
    'ANTI-ASIAN' : "ANTI-ASIÁTICOS",
    'ANTI-BUDDHIST' : "ANTI-BUDISTAS",
    'ANTI-HINDU' : "ANTI-HINDUS",
    'ANTI-HISPANIC' : "ANTI-HISPÂNICOS",
    'OTHER' : "OUTROS",
    'ANTI-WHITE' : "ANTI-BRANCOS",
    'ANTI-TRANSGENDER' : "ANTI-TRANSGÊNEROS",
    'ANTI-GENDER NON CONFORMING' : "ANTI-GENERO VARIANTE",
    'ANTI-JEHOVAS WITNESS' : "ANTI-TESTEMUNHAS DE GEOVÁ",
    'ANTI-PHYSICAL DISABILITY' : "ANTI-DEFICIENTES",
    'ANTI-FEMALE HOMOSEXUAL(GAY)' : "ANTI-HOMOSSEXUAIS(MULHER)",
}

def main():
    json_raw = requests.get('https://data.cityofnewyork.us/resource/bqiq-cu78.json')
    dados_json = json.loads(json_raw.text)
    categorias_crime_odio = [dado['county'] for dado in dados_json if 'county' in dado]
    # print(','.join(categorias_crime_odio))


    with open('categoria_crime_odio2.txt','w') as file:
        # for i in range(0,len(categorias_crime_odio)):
        #     categorias_crime_odio[i] = categorias[categorias_crime_odio[i]]
        file.write(','.join(categorias_crime_odio))
    
    # with open('tipos_categorias.txt','w') as file:
    #     file.write("\n".join(list(set(categorias_crime_odio))))

if __name__ == "__main__":
    main()