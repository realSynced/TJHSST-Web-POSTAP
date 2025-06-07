from flask import Flask, render_template, session

app = Flask(__name__)
app.secret_key = '12345678'



@app.route('/')
def index():

    this_user_visits = None

    this_user_visits = session.get('this_user_visits', 0) + 1
    session['this_user_visits'] = this_user_visits

    return render_template('index.html', visit_no=this_user_visits)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)