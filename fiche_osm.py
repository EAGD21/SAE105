from md_to_html import convert
import requests
from math import *

def get_node(id: int) -> list:
    api_url = f"https://www.openstreetmap.org/api/0.6/node/{id}.json"
    response = requests.get(api_url)
    donnees = response.json()
    try:
        element = donnees.get("elements")[0].get("tags")
        data = []
        data.append(donnees.get("elements")[0].get("type"))
        data.append(donnees.get("elements")[0].get("id"))
        data.append(donnees.get("elements")[0].get("lat"))
        data.append(donnees.get("elements")[0].get("lon"))
        for json_data in element.items():
            data.append(json_data)
    except:
        json_data = "SANS NOM"
        pass
    return data

def node_to_md(id: int) -> None:

    #headers = {"User-Agent": "CityDataScript/1.0 (contact@example.org)"}
    #wp_res = requests.get(f"https://tile.openstreetmap.org/{data[2]}/{data[3]}/15.png")

    n = len(data)
    data = get_node(id)
    txt = ""
    txt += f"# Type: {data[0]}  \n# ID: {data[1]}  \n# Latitude: {data[2]}  \n# Longitude: {data[3]}  \n\n\n"
    txt += f"![map](https://tile.openstreetmap.org/{data[2]}/{data[3]}/15.png) \n\n"
    for i in range(4,n):
        txt += f" - **{data[i][0]}:** {data[i][1]}  \n\n"
    with open('file.md','w') as f:
        f.write(txt)

def generate_map(lat,lon): # difficulté dans l'ajout et l'utilisation de la map
    x = (lon + 180) / 360 * 256 * 2**15
    y = (1 - ( (lat * 3.141592653589793 / 180).tan() + (1 / (lat * 3.141592653589793 / 180).cos()).ln() ) / 3.141592653589793) / 2 * 256 * 2**15
    tile_x = int(x // 256)
    tile_y = int(y // 256)
    return f"https://tile.openstreetmap.org/15/{tile_x}/{tile_y}.png"

def fiche_osm(id):
    node_to_md(id)
    convert()