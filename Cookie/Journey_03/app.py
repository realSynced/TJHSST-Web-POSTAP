from flask import Flask, session, render_template
import sqlite3

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


# ----------------------------
# DATABASE CONNECTION FUNCTION

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

# ----------------------------
# DEFAULT / LANDING ROUTE
#   (prompts to choose a hero)

@app.route('/')
def default_page():
  return render_template('index.html')

# ----------------------------
# CHOOSEN HERO
#   (exists to set cookie on the server)

@app.route('/hero/<hero>')
def set_hero(hero):

    user_state = create_or_retrieve()
    user_state['hero_name'] = hero
    session.modified = True  

    return render_template('hero.html',
        user_data=user_state
    )


# ----------------------------
# LOCATIONS

@app.route('/places/<location>')
def place_page(location):

  # DATABASE SELECTION
  conn = get_db_connection()
  data = conn.execute('''
    SELECT route_2 
    FROM links WHERE route_1 = ?
    ''',(location,)).fetchall()
  conn.close()

  # GENERATE TEMPLATE
  return render_template('places.html',outgoing_links=data)



# ----------------------------
# MAIN FUNCTION

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=80, debug=True)