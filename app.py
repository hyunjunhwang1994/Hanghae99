from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient  # 패키지 임포트

# client = MongoClient("mongodb+srv://test:sparta@cluster0.jmcjmfs.mongodb.net/?retryWrites=true&w=majority")
# db = client.dbsparta.study

client = MongoClient('mongodb+srv://test:sparta@cluster0.jftxkcu.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta



app = Flask(__name__)

@app.route('/')
def home():
    # return render_template('main.html')
    return render_template('index.html')

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
    id_receive = request.form['id_give']
    pw_receive = request.form['pw_give']
    doc = {
            "name":name_receive,
            "id":id_receive,
            "pw":pw_receive
    }
    db.users.insert_one(doc)
    return jsonify({'msg':'회원가입완료'})
@app.route('/signup', methods=['GET'])
def signup_get():
    return jsonify({'msg':'get연결완료'})
@app.route('/idcheck', methods=['POST'])
def id_check_post():
    id_list = list(db.users.find({},{'_id':False,'pw':False,'name':False}))
    return jsonify({'id_list':id_list})


# 포켓몬 전체조회 (이혜민)
@app.route('/index')
def index():
    return render_template('index.html')

@app.route("/poketmon", methods=["GET"])
def poketmon_list():
    poketmon_list = list(db.poketmons.find({}, {'_id': False}))
    return jsonify({'poketmons': poketmon_list})

# 검색 (이혜민)
@app.route("/search", methods=["GET"])
def poketmon_search():
    poketmon_list = list(db.poketmons.find({}, {'_id': False}))
    return jsonify({'poketmon_list': poketmon_list})

# 예약하기(이혜민)
@app.route('/reservation')
def reservation():
    return render_template('reservation.html')

@app.route("/reservation", methods=["GET"])
def reservation_get():
    print('확인해봐')
    poketmons_list = list(db.poketmons.find({}, {'_id': False}))
    print(poketmon_list)
    return jsonify({'poketmons_list': poketmons_list})

# 예약확정,DB저장 (이혜민)
@app.route("/reservation", methods=["POST"])
def reservation_post():
    name_receive = request.form['name_give']
    store_receive = request.form['store_give']
    count_receive = request.form['count_give']
    username_receive = request.form['username_give']
    date_receive = request.form['date_give']

    doc = {
        'name': name_receive,
        'store': store_receive,
        'username': username_receive,
        'date': date_receive,
        'count': count_receive
    }
    db.reservation.insert_one(doc)

    return jsonify({'msg':'저장완료'})

# 예약내역보기 (황현준)
@app.route('/reservation-list')
def reservation_list():
    return render_template('reservation-list.html')

@app.route("/show_reservation", methods=["POST"])
def show_reservation():

    name_receive = request.form['name_give']

    reservation_list = list(db.reservation.find({"username": name_receive}, {'_id': False}))

    return jsonify({'reservation_list': reservation_list})

# 문의하기 (황현준)
@app.route('/ask')
def show_ask():
    return render_template('ask.html')
@app.route("/ask", methods=["POST"])
def do_ask():
    return 0;


if __name__ == '__main__':
    app.run('0.0.0.0',port=5000,debug=True)
