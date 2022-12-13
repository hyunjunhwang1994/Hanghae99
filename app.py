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


@app.route('/users')
def mypage():
    token_receive = request.cookies.get('mytoken')
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        val_ID = db.users.find_one({'id': payload['id']}, {'_id': False})
        return render_template('myPage.html')
    except jwt.ExpiredSignatureError:
        return jsonify({'result': 'fail', 'msg': '로그인 시간이 만료되었습니다.'})
    except jwt.exceptions.DecodeError:
        return jsonify({'result': 'fail', 'msg': '로그인 정보가 존재하지 않습니다.'})


@app.route('/users/info', methods=['GET','POST'])
def getInfo():
    token_receive = request.cookies.get('mytoken')
    if request.method == 'GET':
        try:
            payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
            val_ID = db.users.find_one({'id': payload['id']}, {'_id': False})
            return jsonify({'info':val_ID})
        except jwt.ExpiredSignatureError:
            return jsonify({'result': 'fail', 'msg': '로그인 시간이 만료되었습니다.'})
        except jwt.exceptions.DecodeError:
            return jsonify({'result': 'fail', 'msg': '로그인 정보가 존재하지 않습니다.'})
    if request.method == 'POST':
        nick_receive = request.form['nick_give']
        email_receive = request.form['email_give']
        try:
            payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
            val_ID = db.users.find_one({'id': payload['id']}, {'_id': False})
            id_found = val_ID['id']
            db.users.update_one({'id': id_found}, {'$set': {'nick': nick_receive, 'email': email_receive}})
            print(db.users.find_one({'id': id_found}))
            return '수정 완료'
        except jwt.ExpiredSignatureError:
            return jsonify({'result': 'fail', 'msg': '로그인 시간이 만료되었습니다.'})
        except jwt.exceptions.DecodeError:
            return jsonify({'result': 'fail', 'msg': '로그인 정보가 존재하지 않습니다.'})


@app.route('/users/checkid', methods=["POST"])
def checkid():
    id_receive = request.form['id_give']
    chkID = db.users.find_one({'id':id_receive})
    if chkID == None:
        return '1'
    if chkID != None:
        return '0'


@app.route('/users/join', methods=["POST"])
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


@app.route('/users/login', methods=["POST"])
def login():

    id_receive=request.form['id_give']
    pw_receive = request.form['pw_give']

    pw_hash = hashlib.sha256(pw_receive.encode('utf-8')).hexdigest()
    val = db.users.find_one({'id': id_receive,'pw':pw_hash})

    if val != None:
        payload = {
            'id': id_receive,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=100)
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
        return jsonify({'result': 'success', 'token': token})

    if val == None:
        return jsonify({'result': 'fail', 'msg': "아이디/비밀번호가 일치하지 않습니다."})



@app.route('/submainpage')
def go_submainpage():
    token_receive = request.cookies.get('mytoken')



    if token_receive == None:
        print("비공개 유저 접속")
        user_id = "unknown"

    else:
        try:
            payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
            user_id = payload['id']

        except jwt.ExpiredSignatureError:
            print("비공개 유저 접속")
            user_id = "unknown"
        except jwt.exceptions.DecodeError:
            print("비공개 유저 접속")
            user_id = "unknown"

    # all_uesrs_info 친구 추가할 모든 유저들 보여줌.
    # 1. all user 데이터에서 자신 제외하기
    # 2. 해당유저가 이미 친구인 사람은 제외하고 보여주기
    currentUser_receive = user_id
    all_users_info = list(db.users.find({}, {'_id': False, 'pw': False, 'email': False}))
    all_friends = list(db.friends.find(
        {"$or": [{'friends_currentUser': currentUser_receive}, {"friends_targetUser": currentUser_receive}]},
        {'_id': False}))

    # 자신 삭제.
    for user in all_users_info:
        if user['id'] == user_id:
            all_users_info.remove(user)


    # 해당유저의 친구 제외하고 보여주기.
    for friend in all_friends:
        if (friend['friends_currentUser'] == user_id) or (friend['friends_targetUser'] == user_id):
            for user in all_users_info:
                if user['id'] == friend['friends_currentUser'] or user['id'] == friend['friends_targetUser']:
                    all_users_info.remove(user)


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

    skip = (nowPage_receive * 4 + 4 * (nowPage_receive % 10)) - postsLimit


    if (block_last > last_page):
        block_last = last_page

    likes_post = db.likes.find_one({"id": user_id}, {'likes_post': 1, '_id': False})
    if likes_post == None:
        likes_post = {'likes_post': []}

    if likes_post != None:
        for post in all_posts:
            i = post['post_num']
            n = post['post_num']


        likes_array = []
        for x in range(postsLimit):
            testList = likes_post['likes_post']

            if i in testList:
                print("있다.-------=-=" + str(i))
                likes_array.append(i)
                i -= 1

                if i == (skip):
                    break
            else:
                print("없다." + str(i))
                i -= 1


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
        'submainpage.html',
        all_posts=all_posts,
        total_count=total_count,
        postsLimit=postsLimit,
        nowPage_receive=nowPage_receive,
        block_start=block_start,
        block_last=block_last,
        last_page=last_page,
        likes_array=likes_array,
        all_users_info = all_users_info,
        user_id=user_id
    )



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
        db.crud.update_one({'post_num': post_id}, {"$inc": {'likes': 1}})


    # 좋아요를 한적이 없다면 insert로 테이블 구조 생성
    else:
        doc_array1 = {"id":user_id, "likes_post":[post_id]}
        db.likes.insert_one(doc_array1)
        print("데이터 저장완료 : " + str(post_id))
        db.crud.update_one({'post_num': post_id}, {'$inc': {'likes': 1}})
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
        db.crud.update_one({'post_num': post_id}, {'$inc': {'likes': -1}})
    else:
        doc_array1 = {"id":user_id}
        db.likes.delete_one(doc_array1)
        print("테이블삭제")
        db.crud.update_one({'post_num': post_id}, {'$inc': {'likes': -1}})
    return ""




@app.route('/api/pagination')
def pagination():

    token_receive = request.cookies.get('mytoken')

    if token_receive == None:
        print("비공개 유저 접속")
        user_id = "unknown"

    else:
        try:
            payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
            user_id = payload['id']

        except jwt.ExpiredSignatureError:
            print("비공개 유저 접속")
            user_id = "unknown"
        except jwt.exceptions.DecodeError:
            print("비공개 유저 접속")
            user_id = "unknown"


    # all_uesrs_info 친구 추가할 모든 유저들 보여줌.
    # 1. all user 데이터에서 자신 제외하기
    # 2. 해당유저가 이미 친구인 사람은 제외하고 보여주기
    currentUser_receive = user_id
    all_users_info = list(db.users.find({}, {'_id': False, 'pw': False, 'email': False}))
    all_friends = list(db.friends.find({"$or": [{'friends_currentUser': currentUser_receive}, {"friends_targetUser": currentUser_receive}]},{'_id':False}))

    # 자신 삭제.
    for user in all_users_info:
        if user['id'] == user_id:
            all_users_info.remove(user)


    # 해당유저의 친구 제외하고 보여주기.
    for friend in all_friends:
        if (friend['friends_currentUser'] == user_id) or (friend['friends_targetUser'] == user_id):
            for user in all_users_info:
                if user['id'] == friend['friends_currentUser'] or user['id'] == friend['friends_targetUser']:
                    all_users_info.remove(user)

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

    if likes_post == None:
        likes_post = {'likes_post':[]}

    print(likes_post)

    if likes_post != None:
        for post in all_posts:
            i = post['post_num']

            n = post['post_num']

        likes_array = []
        print("i:" + str(i))
        # 아래의 함수 가 한페이지당 표시된 글의 수만큼 돌ㅇ야함.
        for x in range(postsLimit):
            testList = likes_post['likes_post']

            if i in testList:
                print("있다.-------=-=" + str(i))
                likes_array.append(i)
                i -= 1

                if i == (skip):
                    break
            else:
                print("없다." + str(i))
                i -= 1


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
        'submainpage.html',
        all_posts=all_posts,
        total_count=total_count,
        postsLimit=postsLimit,
        nowPage_receive=nowPage_receive,
        block_start=block_start,
        block_last=block_last,
        last_page=last_page,
        likes_array=likes_array,
        all_users_info=all_users_info,
        user_id=user_id
    )



@app.route('/addfriend')
def goFriend():
    token_receive = request.cookies.get('mytoken')

    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        user_id = payload['id']

    except jwt.ExpiredSignatureError:
        return jsonify({'result': 'fail', 'msg': '로그인 시간이 만료되었습니다.'})
    except jwt.exceptions.DecodeError:
        return jsonify({'result': 'fail', 'msg': '로그인 정보가 존재하지 않습니다.'})

    # 모든 유저 불러와 뿌리기 ?
    all_users_info = list(db.users.find({}, {'_id': False,'pw':False, 'email':False}))

    print(all_users_info)

    return render_template("friendtest.html",
                           all_users_info=all_users_info,
                           user_id=user_id)

@app.route('/api/addfriend', methods=["POST"])
def addFriend():




    token_receive = request.cookies.get('mytoken')

    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        user_id = payload['id']

    except jwt.ExpiredSignatureError:
        return jsonify({'result': 'fail', 'msg': '로그인 시간이 만료되었습니다.'})
    except jwt.exceptions.DecodeError:
        return jsonify({'result': 'fail', 'msg': '로그인 정보가 존재하지 않습니다.'})

    currentUser_receive = user_id  # 유저 세션이나 JWT 확인 (현재 유저)
    targetUser_receive = request.form['targetUser_give']  # 추가할 유저 -> html에서 클릭시 해당유저 id 가지고옴


    doc = {
        'friends_currentUser': currentUser_receive,
        'friends_targetUser': targetUser_receive,
        'friends_isFriend': 0}

    db.friends.insert_one(doc)

    return jsonify({"msg":"success"})

@app.route('/api/showfriend', methods=['POST'])
def showFriend():


    token_receive = request.cookies.get('mytoken')

    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        user_id = payload['id']

    except jwt.ExpiredSignatureError:
        return jsonify({'result': 'fail', 'msg': '로그인 시간이 만료되었습니다.'})
    except jwt.exceptions.DecodeError:
        return jsonify({'result': 'fail', 'msg': '로그인 정보가 존재하지 않습니다.'})

    currentUser_receive = user_id  # 유저 세션이나 JWT 확인 (현재 유저)

    all_friends = list(db.friends.find({"$or": [{'friends_currentUser': currentUser_receive}, {"friends_targetUser": currentUser_receive}]},{'_id':False}))



    print("서버 단 친구 목록보기 " + str(all_friends))

    return jsonify(all_friends)



@app.route('/api/deletefriend', methods=['POST'])
def deleteFriend():

    token_receive = request.cookies.get('mytoken')

    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        user_id = payload['id']

    except jwt.ExpiredSignatureError:
        return jsonify({'result': 'fail', 'msg': '로그인 시간이 만료되었습니다.'})
    except jwt.exceptions.DecodeError:
        return jsonify({'result': 'fail', 'msg': '로그인 정보가 존재하지 않습니다.'})

    currentUser_receive = user_id
    targetUser_receive = request.form['targetUser_give']
    order = request.form["order"]


    print(currentUser_receive)
    print(targetUser_receive)
    print(order)

    if(order == "ab"):
        db.friends.delete_one({'friends_currentUser': currentUser_receive, 'friends_targetUser': targetUser_receive})

    if(order == "ba"):
        db.friends.delete_one({'friends_targetUser': currentUser_receive, 'friends_currentUser':targetUser_receive })

    return jsonify({"msg":"success"})


@app.route('/api/permitfriend', methods=['POST'])
def permitFriend():

    currentUser_receive = request.form['currentUser_give']
    targetUser_receive = request.form['targetUser_give']



    db.friends.update_one({'friends_currentUser': currentUser_receive ,'friends_targetUser': targetUser_receive }, {'$set': {'friends_isFriend': 1}})



    return jsonify({"msg":"success"})




@app.route('/test')
def test():

    return render_template('test.html')


@app.route('/content/write')
def write():
    token_receive = request.cookies.get('mytoken')

    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])

        # userinfo = db.users.find_one({'id': payload['id']}, {'_id': 0})
        return render_template('write.html')
    except jwt.ExpiredSignatureError:
        # 위를 실행했는데 만료시간이 지났으면 에러가 납니다.
        return jsonify({'result': 'fail', 'msg': '로그인 시간이 만료되었습니다.'})
    except jwt.exceptions.DecodeError:
        return jsonify({'result': 'fail', 'msg': '로그인 정보가 존재하지 않습니다.'})


@app.route('/content/write', methods=["POST"])
def write_content():
    token_receive = request.cookies.get('mytoken')
    crud_title_receive = request.form['crud_title_give']
    write_receive = request.form['write_give']
    payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
    userinfo = db.users.find_one({'id': payload['id']}, {'_id': 0})
    id=userinfo["id"]
    # print(write_receive)
    write_list = list(db.crud.find({}, {'_id': False}))
    # print(write_list)
    post_num = len(write_list) + 1  # len() = ~의 리스트 수

    doc = {
        'likes' : 0,
        'id' : id,
        'crudtitle': crud_title_receive,
        'post_num': post_num,
        'write': write_receive,
    }

    db.crud.insert_one(doc)

    return jsonify({'msg': '저장 완료!'})


@app.route('/content/written', methods=["GET"])
def written():

    return render_template('written.html')


@app.route("/content/written/<int:post_num>", methods=["GET"])
def written_get(post_num):
    token_receive = request.cookies.get('mytoken')

    user = db.crud.find_one({'post_num': post_num})
    # print(user)
    id = user["id"]
    # print(id)
    post_num = user["post_num"]
    crudtitle = user["crudtitle"]
    write = user["write"]
    write_url2 = write.replace('<figure class="media"><oembed url=', '<iframe width="560" height="315" src=')
    write_url1 = write_url2.replace('></oembed></figure>', ' title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>')
    write_url = write_url1.replace('youtu.be', 'www.youtube.com/embed')
    comment_list = list(db.crudcomment.find({'post_num': post_num}, {'_id': False}))
    comments=comment_list
    print(comments)


    try :
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        user_id = payload["id"]
        return render_template('written.html',
                               comments=comments,
                               user_id=user_id,
                               id=id,
                               post_num=post_num,
                               crudtitle=crudtitle,
                               write=write,
                               write_url=write_url
                               )
    except:
        return render_template('written.html',
                               comments=comments,
                               id=id,
                               post_num=post_num,
                               crudtitle=crudtitle,
                               write=write,
                               write_url=write_url,
                           )

@app.route('/content/edit', methods=["POST"])
def edit_content():
    crud_title_receive = request.form['crud_title_edit']
    write_receive = request.form['write_edit']
    # print(write_receive)
    # print(crud_title_receive)

    num_receive = request.form['num_give']
    num_receive=int(num_receive)
    # print(num_receive)
    # print(type(num_receive))

    db.crud.update_one({'post_num': num_receive}, {'$set': {'write': write_receive}})
    db.crud.update_one({'post_num': num_receive}, {'$set': {'crudtitle': crud_title_receive}})

    return jsonify({'msg': '수정 완료!'})


@app.route("/content/edit/<int:post_num>", methods=["GET"])
def edit_get(post_num):
    user = db.crud.find_one({'post_num': post_num})
    # print(user)
    id = user["id"]
    post_num = user["post_num"]
    crudtitle = user["crudtitle"]
    write = user["write"]
    write_url2 = write.replace('<figure class="media"><oembed url=', '<iframe width="560" height="315" src=')
    write_url1 = write_url2.replace('></oembed></figure>', ' title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>')
    write_url = write_url1.replace('youtu.be', 'www.youtube.com/embed')
    token_receive = request.cookies.get('mytoken')

    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        user_id = payload["id"]
        if (user_id == id): return render_template('edit.html',
                                                   user_id=user_id,
                                                   id=id,
                                                   post_num=post_num,
                                                   crudtitle=crudtitle,
                                                   write=write,
                                                   write_url=write_url
                                                   )
    except jwt.ExpiredSignatureError:
        return jsonify({'result': 'fail', 'msg': '로그인 시간이 만료되었습니다.'})
    except jwt.exceptions.DecodeError:
        return jsonify({'result': 'fail', 'msg': '로그인 정보가 존재하지 않습니다.'})


@app.route("/content/comment", methods=["POST"])
def add_comment():
    token_receive = request.cookies.get('mytoken')
    payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
    userinfo = db.users.find_one({'id': payload['id']}, {'_id': 0})
    nick = userinfo["nick"]
    id = userinfo["id"]
    num_receive = request.form['num_give']
    num_receive= int(num_receive)
    comment_receive = request.form['comment_give']

    doc = {
        'id': id,
        'nick': nick,
        'post_num': num_receive,
        'comment': comment_receive
    }
    db.crudcomment.insert_one(doc)

    return jsonify({'msg': '작성 완료!'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)