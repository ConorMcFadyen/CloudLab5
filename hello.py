from flask import Flask
from flask import request
app = Flask(__name__)
from PIL import Image
import requests
from io import BytesIO



@app.route("/")
def hello():
    return "This is the cloud computing lab 5!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
    





@app.route("/route32a")
def route32a():
    return "Hello from the 32A"

@app.route("/route")
def route():
    number=request.args.get('number')
    return "Hello from the {}".format(number)

if __name__ == "__main__":
    app.run(host='0.0.0.0',port='8080')
