import sqlite3
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn


def update_database(name, wit, strength, attack, defense, magic):
    print("Update database called with parameters:")
    print(
        f"Name: {name}, Wit: {wit}, Strength: {strength}, Attack: {attack}, Defense: {defense}, Magic: {magic}"
    )
    conn = get_db_connection()
    conn.execute(
        "UPDATE characters SET c_wit = ?, c_strength = ?, c_attack = ?, c_defense = ?, c_magic = ? WHERE c_name = ?",
        (wit, strength, attack, defense, magic, name),
    )
    conn.commit()
    conn.close()


@app.route("/heros")
def heros():
    conn = get_db_connection()
    data = conn.execute("SELECT * FROM characters").fetchall()
    conn.close()
    if request.method == "POST":
        name = request.form.get("name")
        wit = request.form.get("wit")
        strength = request.form.get("strength")
        attack = request.form.get("attack")
        defense = request.form.get("defense")
        magic = request.form.get("magic")

        update_database(name, wit, strength, attack, defense, magic)
        return

    return render_template("index.html", heroes=data)


@app.route("/hero/<hero_name>")
def specific_hero(hero_name):
    conn = get_db_connection()
    data = conn.execute(
        "SELECT * FROM characters WHERE c_name = ?", (hero_name,)
    ).fetchall()
    conn.close()
    # Here you would typically fetch hero details from a database or an API
    # For simplicity, we will just return the hero name
    return render_template("hero.html", hero=data[0])


@app.route("/hero_backend", methods=["POST"])
def hero_backend():
    name = request.form.get("name")
    wit = request.form.get("wit")
    strength = request.form.get("strength")
    attack = request.form.get("attack")
    defense = request.form.get("defense")
    magic = request.form.get("magic")

    print(
        f"Received data: name={name}, wit={wit}, strength={strength}, attack={attack}, defense={defense}, magic={magic}"
    )

    update_database(name, wit, strength, attack, defense, magic)

    return render_template("redirect.html")


if __name__ == "__main__":
    app.run(debug=True)
