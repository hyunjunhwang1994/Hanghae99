from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient #패키지 임포트
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('main.html')

@app.route('/mars', methods=['POST'])
def poketmon_post():
    sample_receive = request.form['sample_give']

    return jsonify({'msg':'post연결완료'})

@app.route('/mars',methods=['GET'])
def poketmon_get():

    return jsonify({'msg':'get연결완료!','buyer_list':buyer_list})


if __name__ == '__main__':
    app.run('0.0.0.0',port=5000,debug=True)