from flask import Flask, session, render_template

app = Flask(__name__)
app.secret_key = 'dtfyghubjn234567dfgh'


def create_or_retrieve():
    if 'user_state' not in session:
        init_user_state()
    return session['user_state']

def init_user_state():
    session['user_state'] = {
        'visits': 0,
        'hero_name': "",
        'authenticated_user': False,
        'visited_locations': {
            'palace': False,
            'market': False,
            'forest': False,
            'mountain': False
        }
    }


@app.route('/')
def default_page():

    user_state = create_or_retrieve()

    return render_template('index.html',
        user_data=user_state
    )


@app.route('/hero/<hero>')
def set_hero(hero):

    user_state = create_or_retrieve()
    user_state['hero_name'] = hero
    session.modified = True  

    return render_template('hero.html',
        user_data=user_state
    )




if __name__ == '__main__':
  app.run(host='0.0.0.0', port=80, debug=True)