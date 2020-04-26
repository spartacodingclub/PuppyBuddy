from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient

client=MongoClient('localhost', 27017)
db = client.dbsparta

puppybuddy = Flask(__name__)

@puppybuddy.route('/')
def home():
    return render_template('puppybuddy.html')

@puppybuddy.route('/enroll', methods=['POST'])
def enroll_info():
    name_r = request.form['name_give']
    age_r = request.form['age_give']
    breed_r = request.form['breed_give']
    charm_r = request.form['charm_give']
    location_r = request.form['location_give']
    start_r = request.form['start_give']
    finish_r = request.form['finish_give']

    puppy_info = {
        '이름' : name_r,
        '나이' : age_r,
        '견종' : breed_r,
        '특징' : charm_r,
        '산책장소' : location_r,
        '산책시작' : start_r,
        '산책종료' : finish_r


    }

    db.buddy.insert_one(puppy_info)
    return jsonify({'result': 'success', 'msg': '성공적으로 등록되었습니다'})


@puppybuddy.route('/enroll', methods=['GET'])
def read_list():
    info = list(db.buddy.find({}, {'_id': False}))
    return jsonify({'result':'success', 'buddy': info})

if __name__ =='__main__':
    puppybuddy.run('127.0.0.1', port=5007, debug=True)