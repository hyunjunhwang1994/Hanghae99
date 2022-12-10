from flask import Flask, render_template, jsonify, request, session, redirect, url_for
<<<<<<< Updated upstream
from pymongo import MongoClient
import certifi
import jwt
import datetime
import hashlib
=======
import math
>>>>>>> Stashed changes

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

<<<<<<< Updated upstream
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

=======
    return render_template('index.html')
>>>>>>> Stashed changes





@app.route('/pagination')
def startPagination():

    # 시작시 페이지
    nowPage_receive = int(1)
    postsLimit = 8  # 한 페이지당 포스트 수
    pagesLimit = 5  # 페이지 수

    # 포스트의 모든 데이터
    all_posts = list(db.posts.find({}, {'_id': False}))

    # 포스트 총 갯수
    total_count = len(list(db.posts.find({}, {'_id': False})))

    # 총 페이지 수 == 마지막 페이지
    last_page = math.ceil(total_count / postsLimit)

    # 시작 번호 계산
    block_start = nowPage_receive % pagesLimit

    #
    block_zero = nowPage_receive - (nowPage_receive % pagesLimit) + 1
    block_last = nowPage_receive - (nowPage_receive % 10) + pagesLimit




    if (block_last > last_page):
        block_last = last_page




    print("total_count: " +str(total_count))
    print("nowPage_receive: " + str(nowPage_receive))
    print("block_start: " + str(block_start))
    print("block_last: " + str(block_last))
    print("last_page: " +str(last_page))



    return render_template(
        'pagination.html',
        all_posts=all_posts,
        total_count=total_count,
        postsLimit=postsLimit,
        nowPage_receive=nowPage_receive,
        block_start=block_start,
        block_last=block_last,
        last_page=last_page
    )

@app.route('/api/pagination')
def pagination():



    # 프론트에서 넘어온 사용자의 현재 페이지
    nowPage_receive = request.args.get("nowPage_give", 1, type=int)
    postsLimit = 8  # 한 페이지당 포스트 수
    pagesLimit = 5  # 페이지 수

    # 포스트의 모든 데이터
    all_posts = list(db.posts.find({}, {'_id': False}))

    # 포스트 총 갯수
    total_count = len(list(db.posts.find({}, {'_id': False})))

    # 총 페이지 수 == 마지막 페이지
    last_page = math.ceil(total_count / postsLimit)

    # 시작 번호 계산
    # block_start = nowPage_receive % pagesLimit


    block_start = nowPage_receive - (nowPage_receive % pagesLimit) + 1

    # 5와, 10의 배수 처리.
    if(nowPage_receive % 5 == 0):
        block_start = block_start - pagesLimit


    block_last = block_start + (pagesLimit - 1)
    # block_last = nowPage_receive - (nowPage_receive % 10) + pagesLimit


    if (block_last > last_page):
        block_last = last_page




    print("총 포스팅 수: " +str(total_count))
    print("현재 페이지는: " + str(nowPage_receive))
    print("block_start: " + str(block_start))
    print("block_last: " + str(block_last))
    print("제일 마지막 페이지는: " +str(last_page))



    return render_template(
        'pagination.html',
        all_posts=all_posts,
        total_count=total_count,
        postsLimit=postsLimit,
        nowPage_receive=nowPage_receive,
        block_start=block_start,
        block_last=block_last,
        last_page=last_page
    )



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