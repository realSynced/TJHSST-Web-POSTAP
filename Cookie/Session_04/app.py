from flask import Flask, render_template, session

app = Flask(__name__)
app.secret_key = '12345678'

def get_session_data():
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
def index():

    # EXTRACT AND POSSIBLY INIT THE SESSION DATA
    user_state = get_session_data()

    # GET THE DATA - THIS PASSES BY REFERENCE
    user_state['visits'] += 1

    # RENDER A TEMPLATE
    return render_template('index.html',
        user_data=user_state
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)