import json

from flask import jsonify

# Assure-toi que le chemin du fichier est correct
pathData = "data/data.json"  # Si le fichier est dans le dossier 'data'

def loadData():
    with open(pathData, "r", encoding="utf-8") as fichier:
        return json.load(fichier)

def getData():
    data = loadData()
    return jsonify(data)

def writeData(data):
    with open(pathData, "w", encoding="utf-8") as fichier:
        json.dump(data, fichier, indent=2)

def get_user_from_json():
    # Le fichier data.json doit se trouver dans le dossier 'data'
    with open(pathData, "r", encoding="utf-8") as fichier:
        return json.load(fichier)["users"]

