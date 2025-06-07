from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/start')
def hello_world():
    return render_template('start.html')

@app.route('/whoareyou')
def who_are_you():
    name = request.args.get('name', '')
    return render_template('whoareyou.html', name=name)

@app.route('/what')
def what_next():
    name = request.args.get('name', '')
    return render_template('what.html', name=name)

@app.route('/escape')
def escape_room():
    name = request.args.get('name', '')
    return render_template('escape.html', name=name)

@app.route('/whichroom')
def which_room():
    name = request.args.get('name', '')
    return render_template('whichroom.html', name=name)

@app.route('/truth')
def truth_path():
    name = request.args.get('name', '')
    return render_template('truth.html', name=name)

@app.route('/illusion')
def illusion_path():
    name = request.args.get('name', '')
    return render_template('illusion.html', name=name)

@app.route('/freedom')
def freedom():
    name = request.args.get('name', '')
    return render_template('freedom.html', name=name)

@app.route('/truth_riddle')
def truth_riddle():
    name = request.args.get('name', '')
    return render_template('truth_riddle.html', name=name)

@app.route('/illusion_riddle')
def illusion_riddle():
    name = request.args.get('name', '')
    return render_template('illusion_riddle.html', name=name)

@app.route('/')
def index():
    return render_template('start.html')

app.debug=True
if __name__ == '__main__':
    app.run()