import sqlite3
from flask import Flask, render_template

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/")
def index():
    conn = get_db_connection()
    data = conn.execute("SELECT * FROM characters").fetchall()
    conn.close()

    print(data)

    return render_template("characters.html", characters=data)


@app.route("/characters/<name>")
def character_info(name):
    conn = get_db_connection()
    data = conn.execute("SELECT * FROM characters WHERE c_name = ?", (name,)).fetchall()
    conn.close()

    print("Parametric query", data[0])

    return render_template("character_info.html", characters=data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
