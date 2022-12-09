from flask import Flask, render_template, jsonify, request, session, redirect, url_for

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient("mongodb+srv://test:sparta@cluster0.vnmg85w.mongodb.net/?retryWrites=true&w=majority")
db = client.dbsparta





@app.route('/')
def home():

    doc = {'name': 'bobby', 'age': 21}
    db.test.insert_one(doc)

    return render_template('index.html')


@app.route('/test')
def test():

    return render_template('test.html')


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)