from flask import Flask
from flask import request
import json
import requests
import random


def reverse(word):
    return word[::-1]


app = Flask(__name__)


@app.route('/api/', methods=["POST"])
def func2():
    if request.method == 'POST':
        data = request.json['message']
        payload = {'message': data}
        headers = {'Content-Type': "application/json", 'cache-control': "no-cache"}
        response = requests.post(url='http://ms2-service:6000/api', json= payload, headers=headers)
        output = response.json()
        output['random'] = round(random.random() * 10, 2)
        return output
    # url = "http://10.0.0.27:31401/api"
    # payload = "{\"message\": \"Hello\"}"
    # headers = {'Content-Type': "application/json",'cache-control': "no-cache"}
    # response = requests.request("POST", url, data=payload, headers=headers)
    # return response.text


@app.route("/")
def hello():
    return "Hello World!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=6000)
