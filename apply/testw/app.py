from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
dbjungle = client.dbjungle

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/memo', methods=['POST'])
def post_memo():
    title_receive = request.form['title_give']
    content_receive = request.form['content_give']
    like_receive = (int)(request.form['like_give'])
    memo = {'title': title_receive, 'content': content_receive, 'like': like_receive}
    dbjungle.memos.insert_one(memo)
    return jsonify({'result':'success'})

@app.route('/list', methods=['GET'])
def show_memo():
    memos = list(dbjungle.memos.find({}, {'_id': False}).sort('like', -1))
    return (jsonify({'result':'success', 'memo_list' : memos}))


@app.route('/update', methods=['POST'])
def update_memo():
    title_receive = request.form['title_give']
    content_receive = request.form['content_give']
    new_title = request.form['new_title']
    new_content = request.form['new_content']

    dbjungle.memos.update_one ({'title': title_receive}, {'$set': {'title': new_title}})
    dbjungle.memos.update_one ({'content': content_receive}, {'$set': {'content': new_content}})
    return jsonify({'result' : 'success'})

@app.route('/delete', methods=['POST'])
def delete_memo():
    title_receive = request.form['title_give']
    dbjungle.memos.delete_one({'title': title_receive})
    return jsonify({'result' : 'success'})


@app.route('/like', methods=['POST'])
def like_memo():
    title_receive = request.form['title_give']
    title = dbjungle.memos.find_one({'title':title_receive})
    new_like = title['like'] + 1
    dbjungle.memos.update_one({'title':title_receive}, {'$set': {'like':new_like}})
    return jsonify({'result':'success'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)