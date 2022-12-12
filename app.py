import pymongo
from flask import Flask, render_template, jsonify, request, session, redirect, url_for
from jinja2 import Environment
from pymongo import MongoClient
import certifi
import jwt
import datetime
import hashlib
import math


app = Flask(__name__)
app.jinja_env.add_extension('jinja2.ext.loopcontrols')

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










@app.route('/api/clicklike', methods=['POST'])
def click_likes():

    token_receive = request.cookies.get('mytoken')

    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        user_id = payload['id']

    except jwt.ExpiredSignatureError:
        return jsonify({'result': 'fail', 'msg': '로그인 시간이 만료되었습니다.'})
    except jwt.exceptions.DecodeError:
        return jsonify({'result': 'fail', 'msg': '로그인 정보가 존재하지 않습니다.'})

    click_receive = request.form["click_give"]
    print("좋아요 한 글 번호" + str(click_receive))

    post_id = int(click_receive)

    find_user = db.likes.find_one({'id': user_id})


    # 해당 유저가 좋아요 를 1번이라도 했다면 push
    if(find_user != None):
        query = {"id": user_id}
        new_values = {
            "$push": {"likes_post": post_id}
        }
        db.likes.update_one(query, new_values)
        print("데이터 저장완료 : " + str(post_id))
    # 좋아요를 한적이 없다면 insert로 테이블 구조 생성
    else:
        doc_array1 = {"id":user_id, "likes_post":[post_id]}
        db.likes.insert_one(doc_array1)
        print("데이터 저장완료 : " + str(post_id))
    return ""
@app.route('/api/cancellike', methods=["POST"])
def cancel_likes():


    token_receive = request.cookies.get('mytoken')

    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        user_id = payload['id']

    except jwt.ExpiredSignatureError:
        return jsonify({'result': 'fail', 'msg': '로그인 시간이 만료되었습니다.'})
    except jwt.exceptions.DecodeError:
        return jsonify({'result': 'fail', 'msg': '로그인 정보가 존재하지 않습니다.'})

    click_receive = request.form["click_give"]

    post_id = int(click_receive)
    find_user = db.likes.find_one({"$and": [{'id':user_id},{"likes_post":{"$size":1}}]})

    if(find_user == None):
        query = {"id": user_id}
        new_values = {
            "$pull": {"likes_post": post_id}
        }
        db.likes.update_one(query, new_values)
        print("데이터삭제")
    else:
        doc_array1 = {"id":user_id}
        db.likes.delete_one(doc_array1)
        print("테이블삭제")
    return ""

@app.route('/pagination')
def startPagination():

    token_receive = request.cookies.get('mytoken')

    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        user_id = payload['id']

    except jwt.ExpiredSignatureError:
        return jsonify({'result': 'fail', 'msg': '로그인 시간이 만료되었습니다.'})
    except jwt.exceptions.DecodeError:
        return jsonify({'result': 'fail', 'msg': '로그인 정보가 존재하지 않습니다.'})

    # 시작시 페이지
    nowPage_receive = int(1)
    postsLimit = 8  # 한 페이지당 포스트 수
    pagesLimit = 5  # 페이지 수

    # 포스트의 모든 데이터
    all_posts = list(db.crud.find().sort('_id', pymongo.ASCENDING).limit(postsLimit))
    # 포스트 총 갯수
    total_count = len(list(db.crud.find({}, {'_id': False})))
    # 총 페이지 수 == 마지막 페이지
    last_page = math.ceil(total_count / postsLimit)
    # 해당 글의 글번호 ( 8개씩 잘라서 )


    # 블록 계산
    block_start = nowPage_receive % pagesLimit
    block_zero = nowPage_receive - (nowPage_receive % pagesLimit) + 1
    block_last = nowPage_receive - (nowPage_receive % 10) + pagesLimit



    if (block_last > last_page):
        block_last = last_page

    likes_post = db.likes.find_one({"id": user_id},{'likes_post':1,'_id':False})

    if likes_post != None:
        array = likes_post['likes_post']
        array.sort()
        print("정렬하기전 likes_post : " + str(array))
        likes_array = array[0:8]
        print("정렬 후 likes_post :" + str(likes_array))
    else:
        likes_array = [0,0,0,0,0,0,0,0]
        return render_template(
            'pagination.html',
            all_posts=all_posts,
            total_count=total_count,
            postsLimit=postsLimit,
            nowPage_receive=nowPage_receive,
            block_start=block_start,
            block_last=block_last,
            last_page=last_page,
            likes_array=likes_array
        )


    for post in all_posts:
        i = post['post_num']


    for post in likes_array[:]:
        if i < post:
            likes_array.remove(post)


    # 빈값이 있는경우 +  0으로 값넣기
    for x in range(postsLimit - len(likes_array)):
        likes_array.append(0)

    likes_array.sort(reverse=True)
    print(likes_array)


    # print("total_count: " +str(total_count))
    # print("nowPage_receive: " + str(nowPage_receive))
    # print("block_start: " + str(block_start))
    # print("block_last: " + str(block_last))
    # print("last_page: " +str(last_page))



    return render_template(
        'pagination.html',
        all_posts=all_posts,
        total_count=total_count,
        postsLimit=postsLimit,
        nowPage_receive=nowPage_receive,
        block_start=block_start,
        block_last=block_last,
        last_page=last_page,
        likes_array=likes_array
    )

@app.route('/api/pagination')
def pagination():

    token_receive = request.cookies.get('mytoken')

    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        user_id = payload['id']

    except jwt.ExpiredSignatureError:
        return jsonify({'result': 'fail', 'msg': '로그인 시간이 만료되었습니다.'})
    except jwt.exceptions.DecodeError:
        return jsonify({'result': 'fail', 'msg': '로그인 정보가 존재하지 않습니다.'})


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

    all_posts = list(db.crud.find().sort('_id', pymongo.ASCENDING).skip(skip).limit(postsLimit))

    # 포스트 총 갯수
    total_count = len(list(db.crud.find({}, {'_id': False})))

    # 총 페이지 수 == 마지막 페이지
    last_page = math.ceil(total_count / postsLimit)

    block_start = nowPage_receive - (nowPage_receive % pagesLimit) + 1

    # 5와, 10의 배수 처리.
    if(nowPage_receive % 5 == 0):
        block_start = block_start - pagesLimit
    block_last = block_start + (pagesLimit - 1)

    if (block_last > last_page):
        block_last = last_page


    likes_post = db.likes.find_one({"id": user_id},{'likes_post':1,'_id':False})

    if likes_post != None:
        for post in all_posts:
            i = post['post_num']
            n = post['post_num']

        likes_array = []
        for x in range(len(likes_post['likes_post']) + 1):
            testList = likes_post['likes_post']

            # 2페이지라 가정
            # 16 ~ 9 까지의 데이터만 있으면됨.
            if i in testList:
                print("있다.-------=-=" + str(i))
                likes_array.append(i)
                i -= 1

                if i == (n - (postsLimit + 1)):
                    break
            else:
                print("없다." + str(i))
                i -= 1
    else:
        likes_array = [0,0,0,0,0,0,0,0]
        return render_template(
            'pagination.html',
            all_posts=all_posts,
            total_count=total_count,
            postsLimit=postsLimit,
            nowPage_receive=nowPage_receive,
            block_start=block_start,
            block_last=block_last,
            last_page=last_page,
            likes_array=likes_array
        )


    i = 0
    for post in all_posts:
        i = post['post_num']

    # 포스팅 하는 post_num의 최댓값 보다 큰경우 삭제
    for post in likes_array[:]:
        if i < post:
            likes_array.remove(post)


    # 빈값이 있는경우 +  0으로 값넣기
    for x in range(postsLimit - len(likes_array)):
        likes_array.append(0)

    likes_array.sort(reverse=True)
    print("페이지에 적용될 Likes: " + str(likes_array))




    return render_template(
        'pagination.html',
        all_posts=all_posts,
        total_count=total_count,
        postsLimit=postsLimit,
        nowPage_receive=nowPage_receive,
        block_start=block_start,
        block_last=block_last,
        last_page=last_page,
        likes_array=likes_array
    )



@app.route('/addfriend')
def goFriend():

    # 모든 유저 불러와 뿌리기 ?
    all_users_info = list(db.users.find({}, {'_id': False,'pw':False, 'email':False}))

    print(all_users_info)

    return render_template("friendtest.html",
                           all_users_info=all_users_info)

@app.route('/api/addfriend', methods=["POST"])
def addFriend():
    # userA_receive = request.form['userA'] # 유저 세션이나 JWT 확인 (현재 유저)
    # userB_receive = request.form['userB'] # 추가할 유저 -> html에서 클릭시 해당유저 id 가지고옴
    # test

    token_receive = request.cookies.get('mytoken')

    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        user_id = payload['id']

    except jwt.ExpiredSignatureError:
        return jsonify({'result': 'fail', 'msg': '로그인 시간이 만료되었습니다.'})
    except jwt.exceptions.DecodeError:
        return jsonify({'result': 'fail', 'msg': '로그인 정보가 존재하지 않습니다.'})


    currentUser_receive = user_id
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
    print(write_receive)
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

    write_list = list(db.crud.find({}, {'_id': False}))

    return jsonify({'msg': '전송 완료!'})
# edit 쪽에 보내야 할 듯.d

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)