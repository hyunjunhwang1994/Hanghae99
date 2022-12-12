import pymongo
from flask import Flask, render_template, jsonify, request, session, redirect, url_for
from pymongo import MongoClient
import certifi
import jwt
import datetime
import hashlib

import math


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


@app.route('/members/checkid', methods=["POST"])
def checkid():
    id_receive = request.form['id_give']
    chkID = db.users.find_one({'id':id_receive})
    if chkID == None:
        return '1'
    if chkID != None:
        return '0'


@app.route('/members/join', methods=["POST"])
def join():
    id_receive = request.form['id_give']
    pw_receive = request.form['pw_give']
    nick_receive = request.form['nick_give']
    email_receive = request.form['email_give']

    user_list = list(db.users.find({}, {'_id': False}))

    uid = len(user_list) + 1

    pw_hash = hashlib.sha256(pw_receive.encode('utf-8')).hexdigest()


    doc = {
        'id': id_receive,
        'pw': pw_hash,
        'nick': nick_receive,
        'email': email_receive,
        'uid' : uid
    }

    db.users.insert_one(doc)

    return '등록 완료'


@app.route('/members/login', methods=["POST"])
def login():

    id_receive=request.form['id_give']
    pw_receive = request.form['pw_give']

    pw_hash = hashlib.sha256(pw_receive.encode('utf-8')).hexdigest()

    val = db.users.find_one({'id': id_receive,'pw':pw_hash})

    if val != None:
        payload = {
            'id': id_receive,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=5)
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
        return jsonify({'result': 'success', 'token': token})

    if val == None:
        return jsonify({'result': 'fail', 'msg': '아이디/비밀번호가 일치하지 않습니다.'})




@app.route('/pagination')
def startPagination():

    # 시작시 페이지
    nowPage_receive = int(1)
    postsLimit = 8  # 한 페이지당 포스트 수
    pagesLimit = 5  # 페이지 수

    # 포스트의 모든 데이터
    all_posts = list(db.posts.find().sort('_id', pymongo.ASCENDING).limit(postsLimit))
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

    # doc = {
    #     "title":"zflqf",
    #     "name":"zz",
    #     "view": 555
    # }
    # db.posts.insert_one(doc)

    # 프론트에서 넘어온 사용자의 현재 페이지
    nowPage_receive = request.args.get("nowPage_give", 1, type=int)
    postsLimit = 8  # 한 페이지당 포스트 수
    pagesLimit = 5  # 페이지 수

    # nowPage -> skip()
    #   1         0
    #   2         8
    #   3         16
    #   4         24  <--|
    skip = (nowPage_receive * 4 + 4 * (nowPage_receive % 10)) - postsLimit

    all_posts = list(db.posts.find().sort('_id', pymongo.ASCENDING).skip(skip).limit(postsLimit))

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



@app.route('/addfriend')
def goFriend():
    return render_template("friendtest.html")

@app.route('/api/addfriend', methods=["POST"])
def addFriend():
    # userA_receive = request.form['userA'] # 유저 세션이나 JWT 확인 (현재 유저)
    # userB_receive = request.form['userB'] # 추가할 유저 -> html에서 클릭시 해당유저 id 가지고옴
    # test
    currentUser_receive = "qfqfqf"
    targetUser_receive = "userA"


    doc = {
        'friends_currentUser': currentUser_receive,
        'friends_targetUser': targetUser_receive,
        'friends_isFriend': 0}

    db.friends.insert_one(doc)

    return render_template('index.html')

@app.route('/api/showfriend', methods=['POST'])
def showFriend():
    # userA_receive = request.form['userA'] # 유저 세션이나 JWT 확인 (현재 유저)

    # 나중에 JWT로 사용자 ID넣기
    currentUser_receive = "userA"

    # 접속한 userA의 경우 표현할 것
    # friend_a가 userA / isFriend: 0   친구 신청 중
    # friend_a가 userA / isFriend: 1   내 친구

    # friend_b가 userA / isFriend: 0   친구 수락하기 전
    # friend_b가 userA / isFriend: 1   내 친구
    all_friends = list(db.friends.find({"$or": [{'friends_currentUser': currentUser_receive}, {"friends_targetUser": currentUser_receive}]},{'_id':False}))

    print("서버 단 친구 목록보기 " + str(all_friends))

    return jsonify(all_friends)



@app.route('/api/deletefriend', methods=['POST'])
def deleteFriend():

    currentUser_receive = request.form['currentUser_give'] ## 나
    targetUser_receive = request.form['targetUser_give']
    order = request.form["order"]

    # 삭제의 경우 내가 userB (상대방이 친구추가 한 경우)이여도 삭제가 가능해야 한다.
    # -> 삭제할 아이디와 내 아이디가 일치하는 경우에만 삭제 ( friends_a, friends_b 순서상관없이 )

    # 경우의 수
    # a = 나 b = 유저  (삭제)
    # a = 유저 b = 나  (삭제)
    print(currentUser_receive)
    print(targetUser_receive)
    print(order)

    if(order == "ab"):
        db.friends.delete_one({'friends_currentUser': currentUser_receive, 'friends_targetUser': targetUser_receive})

    if(order == "ba"):
        db.friends.delete_one({'friends_targetUser': currentUser_receive, 'friends_currentUser':targetUser_receive })

    return render_template('index.html')

@app.route('/api/permitfriend', methods=['POST'])
def permitFriend():

    currentUser_receive = request.form['currentUser_give']
    targetUser_receive = request.form['targetUser_give']



    db.friends.update_one({'friends_currentUser': currentUser_receive ,'friends_targetUser': targetUser_receive }, {'$set': {'friends_isFriend': 1}})



    return render_template('index.html')


@app.route('/test')
def test():

    return render_template('test.html')

@app.route('/write')
def write():
    return render_template('write.html')



@app.route('/write/content', methods=["POST"])
def write_content():
    crud_title_receive = request.form['crud_title_give']
    write_receive = request.form['write_give']
    # print(write_receive)
    write_list = list(db.crud.find({}, {'_id': False}))
    post_num = len(write_list) + 1  # len() = ~의 리스트 수

    doc = {
        # ID 추가해야함
        'crudtitle': crud_title_receive,
        'post_num': post_num,
        'write': write_receive,
        'editable': 1  #수정가능하면 editable 1
    }

    db.crud.insert_one(doc)

    return jsonify({'msg': '저장 완료!'})
@app.route('/written')
def written():
    return render_template('written.html')


@app.route("/written/content/<int:post_num>", methods=["GET"])
def written_get(post_num):
    user = db.crud.find_one({'post_num':post_num})
    # print(user)
    post_num = user["post_num"]
    crudtitle = user["crudtitle"]
    write = user["write"]
    write_url2 = write.replace('<figure class="media"><oembed url=', '<iframe width="560" height="315" src=')
    write_url1 = write_url2.replace('></oembed></figure>',' title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>')
    # write_url2 = write.replace('<figure class="media"><oembed url="https://youtu.be', '<iframe width="560" height="315" src="https://www.youtube.com/embed')
    # write_url1 = write_url2.replace('></oembed></figure>',' title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>')

    write_url = write_url1.repalce('youtu.be','www.youtube.com/embed')

    # print(write_url)

    print(write_url1)
    print(write_url2)
    print(write)
    editable = user["editable"]

    # < figure class ="media" > < oembed url="https://youtu.be/jqNrkhMx1Ow" > < / oembed > < / figure >

    return render_template('written.html',
                           post_num=post_num,
                           crudtitle=crudtitle,
                           write=write,
                           write_url = write_url,
                           editable=editable)
# edit 쪽에 보내야 할 듯.d

@app.route('/write/content/edit', methods=["POST"])
def edit_content():
    crud_title_receive = request.form['crud_title_give']
    write_receive = request.form['write_give']
    # print(write_receive)
    write_list = list(db.crud.find({}, {'_id': False}))
    post_num = len(write_list) + 1  # len() = ~의 리스트 수

    doc = {
        # ID 추가해야함
        'crudtitle': crud_title_receive,
        'post_num': post_num,
        'write': write_receive,
        'editable': 1  #수정가능하면 editable 1
    }

@app.route("/written/content/edit/<int:post_num>", methods=["GET"])
def edit_get(post_num):
    user = db.crud.find_one({'post_num': post_num})
    # print(user)
    post_num = user["post_num"]
    crudtitle = user["crudtitle"]
    write = user["write"]
    write_url2 = write.replace('<figure class="media"><oembed url=', '<iframe width="560" height="315" src=')
    write_url1 = write_url2.replace('></oembed></figure>',
                                    ' title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>')
    # write_url2 = write.replace('<figure class="media"><oembed url="https://youtu.be', '<iframe width="560" height="315" src="https://www.youtube.com/embed')
    # write_url1 = write_url2.replace('></oembed></figure>',' title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>')

    write_url = write_url1.repalce('youtu.be', 'www.youtube.com/embed')

    print(write)
    editable = user["editable"]

    # < figure class ="media" > < oembed url="https://youtu.be/jqNrkhMx1Ow" > < / oembed > < / figure >

    return render_template('written.html',
                           post_num=post_num,
                           crudtitle=crudtitle,
                           write=write,
                           write_url=write_url,
                           editable=editable)


    #수정해야함

    return jsonify({'msg': '수정 완료!'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)