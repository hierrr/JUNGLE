from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.dbjungle


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/memo', methods=['POST'])
def post_memo():
    title_receive = request.form['title_give']
    content_receive = request.form['content_give']
    like_receive = request.form['like_give']

    memo = {'title': title_receive, 'content': content_receive, 'like': like_receive}

    db.memos.insert_one(memo)

    return jsonify({'result': 'success'})


@app.route('/memo', methods=['GET'])
def read_memos():
    result = list(db.memos.find({}, {'_id': 0}))
    return jsonify({'result': 'success', 'memos': result})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)