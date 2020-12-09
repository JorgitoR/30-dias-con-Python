import os
import datetime 
import requests
from requests_html import HTML
import sys
import pandas as pd

hoy  = datetime.datetime.now()
year = hoy.year

BASE_DIR = os.path.dirname(__file__)

def url_a_archivo(url, archivo="world.html", save=False):
    r = requests.get(url)
    if r.status_code == 200:
        html_texto = r.text
        if save:
            with open(f"world-{year}.html", 'w') as f:
                f.write(html_texto)
        return html_texto
    
    return ""


#url = "https://www.boxofficemojo.com/year/world/"


def pasar_y_extraer(url, name="peliculas"):
    html_text = url_a_archivo(url)
    r_html = HTML(html=html_text)
    table_class = ".a-section .imdb-scroll-table"
    tabla = r_html.find(table_class)

    table_data = []
    nombres_header = []
    if len(tabla) == 1:
        #print(tabla[0].text)
        r_tabla = tabla[0]
        columnas = r_tabla.find("tr")
        header = columnas[0]
        header_cols = header.find("th")
        nombres_header = [x.text for x in header_cols]

        for row in columnas[1:]:
            #print(row.text)
            cols = row.find("td")
            datos = []
            for i, columna in enumerate(cols):
                #print(i, columna.text, '\n\n')
                datos.append(columna.text)
            table_data.append(datos)
        
        dir = os.path.join(BASE_DIR, 'data')
        os.makedirs(dir, exist_ok=True)
        filepath = os.path.join('data', f'{name}.csv')

        df = pd.DataFrame(table_data, columns=nombres_header)
        df.to_csv(filepath, index=False)
        # df.to_csv('peliculas.csv', index=False)

#print(nombres_header)
#print(table_data)

def run(start_year=None, years_ago=10):
    if start_year == None:
        hoy  = datetime.datetime.now()
        start_year = hoy.year

    assert isinstance(start_year, int)
    assert isinstance(years_ago, int)
    assert len(f"{start_year}") == 4
    for i in range(0, years_ago+1):
        url = f"https://www.boxofficemojo.com/year/world/{start_year}/"
        pasar_y_extraer(url, name=start_year)
        print(f"finished {start_year}")
        start_year -= 1

if __name__ == "__main__":
    try:
        start = int(sys.argv[1])
    except:
        start= None
    try:
        count = int( sys.argv[2])
    except:
        count = 1

    run(start_year=start, years_ago=count)