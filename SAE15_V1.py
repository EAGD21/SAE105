from md_to_html import convert
import requests

# https://www.openstreetmap.org/api/0.6/node/1996209696

#api_url = "https://www.openstreetmap.org/api/0.6/node/1947604611.json"
#response = requests.get(api_url)
# a = help(response)
# b = response.status_code
# c = response.text
#donnees = response.json()
#element = donnees.get("elements")[0]
#json_data = element.get("tags").get("name"),element.get("lat"),element.get("lon")


def telecharger(l,d):
    g = requests.get(l)
    r = g.text
    with open(d,"w") as doc:
        page = doc.write(r)
    return page

def get_node_name(id):
    api_url = f"https://www.openstreetmap.org/api/0.6/node/{id}.json"
    response = requests.get(api_url)
    donnees = response.json()
    try:
        element = donnees.get("elements")[0]
        json_data = element.get("tags").get("name")
    except:
        json_data = "SANS NOM"
    return json_data

def print_node_attributes(id):
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

def node_to_md(id):
    data = print_node_attributes(id)
    n = len(data)
    txt = ""
    txt += f"# Type: {data[0]}  \n# ID: {data[1]}  \n# Latitude: {data[2]}  \n# Longitude: {data[3]}  \n\n\n"
    for i in range(4,n):
        txt += f" - **{data[i][0]}:** {data[i][1]}  \n\n"
    with open('file.md','w') as f:
        f.write(txt)
    convert()

'''
def arretbus(ville):
    api_url = "https://overpass-api.de/api/interpreter"
    request = f"""
    [out:json][timeout:25];
    area["name"="{ville}"]->.searchArea;
    node["highway"="bus_stop"](area.searchArea);
    out geom;
    """
    response = requests.get( f"https://overpass-api.de/api/interpreter?data={request}") 
    if response.status_code == 200:
        data = response.json()
        return data.get("elements")[0].get("tags").get("total")
    return response.status_code

def arretbustram(ville):
    api_url = "https://overpass-api.de/api/interpreter"
    request = f"""
    [out:json][timeout:25];
    area["name"="{ville}"]->.searchArea;
    node["highway"="bus_stop"](area.searchArea);
    out geom;
    """
    response = requests.get( f"https://overpass-api.de/api/interpreter?data={request}")
    data = response.json() 
    return data.get("elements")[0].get("tags").get("total")
    
    api_url = "https://overpass-api.de/api/interpreter"
    request = f"""
    [out:json][timeout:25];
    area["name"="{ville}"]->.searchArea;
    node["railway="tram_stop"](area.searchArea);
    out geom;
    """
    response = requests.get( f"https://overpass-api.de/api/interpreter?data={request}") 
    data = response.json()
    return data.get("elements")[0].get("tags").get("total")
'''
# print(telecharger('https://www.openstreetmap.org/api/0.6/node/3649697385',"fichier.html"))
#print(get_node_name(1947604611))
print(node_to_md(12534300884))
#print(arretbus("caen"))
'''
https://overpass-api.de/api/interpreter?data=[out:json][timeout:25];
    area["wikipedia"="fr:Caen"]->.searchArea;
    nwr["highway"="bus_stop"](area.searchArea);
    out geom;.json
'''