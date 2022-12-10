from flask import Flask, render_template, jsonify, request, session, redirect, url_for
from pymongo import MongoClient
import certifi
import jwt
import datetime
import hashlib

app = Flask(__name__)

ca=certifi.where()




client = MongoClient("mongodb+srv://test:sparta@cluster0.vnmg85w.mongodb.net/?retryWrites=true&w=majority")
db = client.dbsparta

SECRET_KEY = 'SPARTA'




@app.route('/')
def home():
    return render_template('main.html')


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/member/join', methods=["POST"])
def join():
    id_receive = request.form['id_give']
    pw_receive = request.form['pw_give']
    nick_receive = request.form['nick_give']
    email_receive = request.form['email_give']

    pw_hash = hashlib.sha256(pw_receive.encode('utf-8')).hexdigest()

    doc = {
        'id': id_receive,
        'pw': pw_hash,
        'nick': nick_receive,
        'email': email_receive
    }

    db.users.insert_one(doc)

    return '0'


@app.route('/member/login', methods=["POST"])
def login():
    id_receive=
    return None



@app.route('/test')
def test():

    return render_template('test.html')

@app.route('/crud')
def crud():
    return render_template('crud.html')



@app.route('/crud/write', methods=["POST"])
def write():
    write_receive = request.form['write_give']
    print(write_receive)
    write_list = list(db.crud.find({}, {'_id': False}))
    count = len(write_list) + 1  # len() = ~의 리스트 수

    doc = {
        # ID 추가해야함
        'num': count,
        'write': write_receive,
        'done': 1
    }

    db.crud.insert_one(doc)

    return jsonify({'msg': '저장 완료!'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)