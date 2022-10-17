from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('mongodb://test:test@3.39.189.247', 27017)
db = client.dbjungle


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/like', methods=['POST'])
def like_memo():
    date_receive = request.form['date_give']
    memo = db.memos.find_one({'date': date_receive})
    new_like = str(int(memo['like']) + 1)
    db.memos.update_one({'date': date_receive}, {'$set': {'like': new_like}})
    return jsonify({'result': 'success'})


@app.route('/del', methods=['POST'])
def delete_memo():
    date_receive = request.form['date_give']
    db.memos.delete_one({'date': date_receive})
    return jsonify({'result': 'success'})


@app.route('/update', methods=['POST'])
def update_memo():
    date_receive = request.form['date_give']
    title_mod = request.form['title_mod']
    content_mod = request.form['content_mod']
    db.memos.update_one({'date': date_receive}, {'$set': {'title': title_mod}})
    db.memos.update_one({'date': date_receive}, {'$set': {'content': content_mod}})
    return jsonify({'result': 'success'})


@app.route('/memo', methods=['POST'])
def post_memo():
    title_receive = request.form['title_give']
    content_receive = request.form['content_give']
    like_receive = request.form['like_give']
    date_recieve = request.form['date_give']
    memo = {'title': title_receive, 'content': content_receive, 'like': like_receive, 'date': date_recieve}
    db.memos.insert_one(memo)
    return jsonify({'result': 'success'})


@app.route('/memo', methods=['GET'])
def read_memos():
    result = list(db.memos.find({}, {'_id': 0}).sort('like', -1))
    return jsonify({'result': 'success', 'memos': result})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)