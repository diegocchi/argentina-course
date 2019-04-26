from flask import Flask, request, jsonify
from flask_cors import CORS
from random import randint

app = Flask(__name__)
CORS(app)

@app.route('/api/course/raffle', methods=['GET'])
def raffle():
    number = randint(0,100)
    return jsonify(number)

@app.route('/api/course/raffle', methods=['POST'])
def save():
    number = request.json['number']
    number = number.replace('\n', '')
    file = open('banco.db', 'a+')
    file.write(number)
    file.write('\r')
    file.close()
    return jsonify('Save successfully')

app.run()
