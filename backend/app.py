from flask import Flask, request
import flask
import json
from flask_cors import CORS
from readFlim import read
from addFilm import insert
from updateFilm import update
from deleteFlim import delete

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route('/users', methods=["GET"])
def users():
    print("users endpoint reached...")
    with open("users.json", "r") as f:
        data = json.load(f)
        data.append({
            "username": "user4",
            "pets": ["hamster"]
        })
        return flask.jsonify(data)
    
@app.route('/films', methods=["GET","POST","PUT","DELETE"])
def films():
    print("films endpoint reached...")
    if request.method == "GET":
        #read from db
        return flask.jsonify(read())

    if request.method == "POST":
        received_data = request.get_json()
        print(f"received data: {received_data}")
        insert(received_data)
        return_data = {
            "status": "success",
            "message": f"received: {received_data}"
        }
        return flask.Response(response=json.dumps(return_data), status=201)
    
    if request.method == "PUT":
        received_data = request.get_json()
        print(f"received data: {received_data}")
        update(received_data)
        return_data = {
            "status": "success",
            "message": f"received: {received_data}"
        }
        return flask.Response(response=json.dumps(return_data), status=201)
    
    if request.method == "DELETE":
        received_data = request.get_json()
        print(f"received data: {received_data}")
        delete(received_data)
        return_data = {
            "status": "success",
            "message": f"received: {received_data}"
        }
        return flask.Response(response=json.dumps(return_data), status=201)
    



if __name__ == "__main__":
    app.run("localhost", 6969)