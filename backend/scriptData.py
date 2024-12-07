from flask import Flask, jsonify
import json


pathData = "data/data.json"

def loadData():
    with open(pathData, "r", encoding="utf-8") as fichier:
        return json.load(fichier)
    
def getData():
    data = loadData()
    return jsonify(data)

def writeData(data):
    with open(pathData, "w", encoding="utf-8") as fichier:
        json.dump(data, fichier, indent=2)
