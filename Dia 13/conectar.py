import requests
import pprint
import pandas as pd

api_key = "ea1bed1eec57a65ce1027342d64688ca"

api_key_token_v4 = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJlYTFiZWQxZWVjNTdhNjVjZTEwMjczNDJkNjQ2ODhjYSIsInN1YiI6IjVmYzY4MzA1M2EzNDBiMDAzZmUwOGU1OCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.WtDUJwnO8CevYlhOlkrrELg4cb_QUYGco1rI3AKB7VM"

# HTTP request METHODS

"""
GET -> grab data
POST -> add/update data

"""

#What is HTTP?

# What is a EndPoint or Url?



"""
GET
/movie/{movie_id}
https://api.themoviedb.org/3/movie/550?api_key=ea1bed1eec57a65ce1027342d64688ca

"""
movie_id = 500
api_version = 3
api_base_url  = f"https://api.themoviedb.org/{api_version}"
endpoint_path = f"/movie/{movie_id}"
endpoints = f"{api_base_url}{endpoint_path}?api_key={api_key}"
#print("URL", endpoints)

r = requests.get(endpoints)
#print(r.text)
#print(r.status_code)

#Usando la version4 
movie_id = 501
api_version = 4
api_base_url  = f"https://api.themoviedb.org/{api_version}"
endpoint_path = f"/movie/{movie_id}"
endpoints = f"{api_base_url}{endpoint_path}?api_key={api_key}"

headers = {

    'Authorization': f"Bearer {api_key_token_v4}",
    'Content-Type': 'application/json;charset=utf-8'

}

r = requests.get(endpoints, headers=headers)
#print(r.text)
#print(r.status_code)



api_base_url  = f"https://api.themoviedb.org/{api_version}"
endpoint_path = f"/search/movie"

buscar_query = "The Matrix"
endpoints = f"{api_base_url}{endpoint_path}?api_key={api_key}&query={buscar_query}"
print(endpoints)
r = requests.get(endpoints)

data = r.json()
resultados = data['results']
#print(type(resultados))

if r.status_code in range(200, 299):
    data = r.json()
    resultados = data['results']
    if len(resultados) > 0:
        #print(resultados[0].keys())
        pelicula_ids = set()
        for resultado in resultados:
            _id = resultado['id']
            print(resultado['title'], _id)
            pelicula_ids.add(_id)
        print(list(pelicula_ids))


salida = "peliculas.csv"
datos_pelicula = []
for movie_id in pelicula_ids:
    api_version=3
    api_base_url  = f"https://api.themoviedb.org/{api_version}"
    endpoint_path = f"/movie/{movie_id}"
    endpoints = f"{api_base_url}{endpoint_path}?api_key={api_key}"
    r = requests.get(endpoints)
    if r.status_code in range(200, 299):
        data = r.json()
        datos_pelicula.append(data)
    print(r.json())

df = pd.DataFrame(datos_pelicula)
print(df.head())
df.to_csv(salida, index=False)

#pprint.pprint(r.json())
