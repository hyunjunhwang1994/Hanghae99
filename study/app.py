from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient
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
    id_receive = request.form['sample_give']
    return jsonify({'msg':'post연결완료'})
@app.route('/login',methods=['GET'])
def login_get():
    return jsonify({'msg':'get연결완료!'})

#회원가입
@app.route('/signup')
def signup():
    return render_template('signup.html')
@app.route('/signup', methods=['POST'])
def signup_post():
    sample_receive = request.form['sample_give']
    return jsonify({'msg':'post연결완료'})
@app.route('/signup',methods=['GET'])
def signup_get():
    return jsonify({'msg':'get연결완료!'})



if __name__ == '__main__':
    app.run('0.0.0.0',port=5000,debug=True)