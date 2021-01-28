import json
import requests
import csv
import pprint

url = "https://api.sncf.com/v1/coverage/sncf/stop_areas"
headers = {"Authorization": "e3f2b3a6-caa9-47d7-98ee-1f67379e654b"}

def read_json(): # read and saves json

    response = requests.get(url, headers=headers) #pop up for password
        # raw_data = json.loads(response.text) #dict
    with open('stop_areas_maria.json', mode="w") as file:
        json.dump(response.text, file)
# returns nothing, saves json

def read_links():

    with open('stop_areas_maria.json') as json_stop_areas_file:
        data = json.load(json_stop_areas_file)

    links = data['links'] # 11 dict with 1 href in each

    list_hrefs = []

    for loop_link in links:

        if type(loop_link) == dict:
            if "href" in loop_link.keys():
                local_href = loop_link["href"]
                list_hrefs.append(local_href)
            else:
                print("Missing key id")
        else:
            print(f"Unexpected format {type(loop_link)}") 

    return list_hrefs

def save_csv(filepath, list): 
    with open(filepath, mode="w", newline='') as f:
        csv_writer = csv.writer(f, delimiter=';')
    if type(data_rows) == list:
        for row in data_rows:
                # écriture du contenu du row dans la nouvelle ligne du fichier csv
            csv_writer.writerow(row)
    else: 
        print("Unexpected input")

def save_links(): 

    read_json()
    my_list = read_links()
    save_csv('my_stop_areas.csv', my_list)