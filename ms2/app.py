from flask import Flask
from flask import request
import json
import requests


def reverse(word):
    return word[::-1]


app = Flask(__name__)


@app.route('/api', methods=["POST"])
def func1():
    # word = request.args.get('message')
    # print(type(word))
    if request.method == "POST":
        data = request.json['message']
        output_message = dict()
        output_message['message'] = reverse(data)
        return output_message


@app.route("/")
def hello():
    return "Hello World!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)


