from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient #패키지 임포트
client = MongoClient("mongodb+srv://test:sparta@cluster0.jmcjmfs.mongodb.net/?retryWrites=true&w=majority")
db = client.dbsparta.study

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('main.html')

#로그인
@app.route('/login')
def login():
    return render_template('login.html')
@app.route('/login', methods=['POST'])
def login_post():
    name_receive = request.form['name_give']
    return jsonify({'msg':'post연결완료'})
@app.route('/login', methods=['GET'])
def login_get():
    return jsonify({'msg':'get연결완료'})

#회원가입
@app.route('/signup')
def signup():
    return render_template('signup.html')
@app.route('/signup', methods=['POST'])
def signup_post():
    name_receive = request.form['name_give']
    id_receive = request.form['name_give']
    pw_receive = request.form['name_give']
    doc = {
            "name":name_receive,
            "id":id_receive,
            "pw":pw_receive
    }
    db.insert_one(doc)

    return jsonify({'msg':'회원가입완료'})
@app.route('/signup', methods=['GET'])
def signup_get():
    return jsonify({'msg':'get연결완료'})



if __name__ == '__main__':
    app.run('0.0.0.0',port=5000,debug=True)