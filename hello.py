from flask import Flask
from flask import request
app = Flask(__name__)

@app.route("/")
def hello():
    import pandas as pd # import package
    import numpy as np
    from pymongo import MongoClient
    import datetime
    import json

    # Create a connection using MongoClient.
    cluster = MongoClient("mongodb+srv://Conor:Password123456789@cluster0.z7i6q3o.mongodb.net/?retryWrites=true&w=majority")

    db = cluster["DatabaseAssignment2"]

    collection = db["Characters"]

    list = []

    #print everything
    for j in collection.find():
       list.append(j)

    return list



@app.route("/route32a")
def route32a():
    return "Hello from the 32A"

@app.route("/route")
def route():
    number=request.args.get('number')
    return "Hello from the {}".format(number)

if __name__ == "__main__":
    app.run(host='0.0.0.0',port='8080')
