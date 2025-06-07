from flask import Flask, render_template, jsonify

votes = {
    'upvote': 0,
    'downvote': 0
}

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html', votes=votes)

@app.route('/upvote', methods=['GET', 'POST'])
def upvote():
    votes['upvote'] += 1
    return jsonify(votes)

@app.route('/downvote', methods=['GET', 'POST'])
def downvote():
    votes['downvote'] += 1
    return jsonify(votes)

app.debug=True
if __name__ == '__main__':
    app.run()