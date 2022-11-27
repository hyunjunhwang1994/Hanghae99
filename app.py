from flask import Flask, render_template, jsonify, request, make_response
from pymongo import MongoClient  # 패키지 임포트

# client = MongoClient("mongodb+srv://test:sparta@cluster0.jmcjmfs.mongodb.net/?retryWrites=true&w=majority")
# db = client.dbsparta.study

client = MongoClient('mongodb+srv://test:sparta@cluster0.jftxkcu.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta



app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

#로그인
@app.route('/login')
def login():
    return render_template('login.html')
@app.route('/login', methods=['POST'])
def login_post():
    id_receive = request.form['id_give']
    pwd_receive = request.form['pwd_give']
    users_list = list(db.users.find({},{'_id':False,'name':False}))
    for id_pwd in users_list:
        if id_receive == id_pwd['id'] and pwd_receive == id_pwd['pwd']:
            user_id = request.form["id_give"]
            res = make_response(jsonify({'msg':"로그인성공"}))
            res.set_cookie("user_id", user_id)
            return res
    return jsonify({'msg':'아이디나 비밀번호가틀립니다'})

@app.route('/getcookie')
def getcookie():
    user_id = request.cookies.get("user_id")
    return user_id

@app.route('/delcookie',methods=['GET'])
def delCookie():
    res = make_response(jsonify({'msg':"로그아웃성공"}))
    res.delete_cookie('user_id')
    return res

#회원가입
@app.route('/signup')
def signup():
    return render_template('signup.html')
@app.route('/signup', methods=['POST'])
def signup_post():
    name_receive = request.form['name_give']
    id_receive = request.form['id_give']
    pwd_receive = request.form['pwd_give']
    doc = {
            "name":name_receive,
            "id":id_receive,
            "pwd":pwd_receive
    }
    db.users.insert_one(doc)
    return jsonify({'msg':'회원가입완료'})
@app.route('/idcheck', methods=['GET'])
def id_check_get():
    id_list = list(db.users.find({},{'_id':False,'pwd':False,'name':False}))
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
    count_receive = int(request.form['count_give'])
    username_receive = request.form['username_give']
    date_receive = request.form['date_give']

    doc = {
        'name': name_receive,
        'store': store_receive,
        'username': username_receive,
        'date': date_receive,
        'count': count_receive
    }

    poketmon = db.poketmons.find({'name': name_receive, 'store': store_receive}, {'stock': True})
    poketmon = list(poketmon)
    stock = int(poketmon[0]['stock'])

    if count_receive > stock:
        return jsonify({'msg': '예약 가능 수량을 초과하였습니다'})
    else:
        db.reservation.insert_one(doc)
        db.poketmons.update_one({'name': name_receive, 'store':store_receive}, {'$set': {'stock': stock-count_receive}})
        return jsonify({'msg': '예약완료'})



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
def enter_ask():
    return render_template('ask.html')
@app.route("/input_ask", methods=["POST"])
def input_ask():
    name_receive = request.form['name_give']
    store_receive = request.form['store_give']
    count_receive = int(request.form['count_give'])
    username_receive = request.form['username_give']
    date_receive = request.form['date_give']

    doc = {
        'name': name_receive,
        'store': store_receive,
        'username': username_receive,
        'date': date_receive,
        'count': count_receive
    }





    poketmon_list = list(db.poketmons.find({"store"}, {'_id': False}))
    return jsonify({'poketmons': poketmon_list})
@app.route("/show_ask", methods=["POST"])
def show_ask():
    id_receive = request.form['login_id']

    ask_list = list(db.ask.find({"id": id_receive}, {'_id': False}))
    return jsonify({'ask_list': ask_list})

@app.route("/show_option", methods=["GET"])
def show_option():

    option_list = list(db.poketmons.find({}, {'_id': False}))
    return jsonify({'option_list': option_list})



if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
