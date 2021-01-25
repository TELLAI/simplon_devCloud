import csv
import json
import requests
import pprint

depart = 'stop_area:OCE:SA:87686006'
arrivee = 'stop_area:OCE:SA:87722025'
URL = f"https://api.sncf.com/v1/coverage/sncf/journeys?from={depart}&to={arrivee}"


r = requests.get(URL, auth=('d402691b-69c5-48e6-b658-9f9be6140b8a',''))
data = json.loads(r.text)

def fct_dict(data_1, key):
    for i in data_1.keys():
        if i == key:
            data_2 = data_1[key]
            return (data_2)

def fct_list(data_1):
    for i in data_1:
        data_2 = i
        return (data_2)

list_keys = ["journeys", "sections", "stop_date_times", "stop_point", "label"]
count = 0
def fct_zoom(data_1, list_keys, count):
    while(list_keys[count] != "label"):
        if (type(data_1)) == dict:
            for key, value in data_1.items():
                print(type(data_1))
                if key == list_keys[count]:
                    count += 1
                    fct_zoom(value, list_keys, count)
        elif (type(data_1)) == list:
            for i in data_1:
                fct_zoom(i, list_keys, count)
        else:
            print("Erreur")
            print(type(data_1))
    print(data_1)
    
fct_zoom(data, list_keys, count)

#pprint.pprint(data["journeys"][0]["sections"][1])

#pprint.pprint(data["journeys"][0]["sections"][1]["stop_date_times"][0]["stop_point"]["label"])
"""
data_links = fct_zoom(data, "journeys")
        for i in data_links:
            dict_vrac = i
            for key in dict_vrac.keys():
                if key == "sections":
                    liste_info = dict_vrac[key]
                    for j in liste_info:
                        dict_info = j
                        for k in dict_info.keys():
                            if k == "stop_date_times":
                                list_stop_point = dict_info[k]
                                for y in list_stop_point:
                                    dict_arret = y
                                    for key in dict_arret.keys():
                                        if key == "stop_point":
                                            dict_stop_point = dict_arret[key]
                                            for key in dict_stop_point.keys():
                                                if key == 'label':
                                                    list_arret.append(dict_stop_point[key])

"""