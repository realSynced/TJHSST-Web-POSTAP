from flask import Flask, render_template, session


app = Flask(__name__)
app.secret_key = '12345678'



@app.route('/')
def index():

    this_user_visits = 1
    selected_hero    = "Archibald"

    # EXTRACT FROM COOKIE (IF EXISTS)
    if 'this_user_visits' in session:
        this_user_visits = session['this_user_visits'] + 1

    if 'selected_hero' in session:
        selected_hero = session['selected_hero']


    session['this_user_visits'] = this_user_visits
    session['selected_hero']    = selected_hero

    return render_template('index.html',
    	visit_no=this_user_visits,
    	hero=selected_hero
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)