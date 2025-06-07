from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

word_list = open("../supplemental/enable1.txt").read().splitlines()


@app.route("/<words>")
def hello_world(words=None):
    if words is None:
        return jsonify({"error": "No date provided"}), 400

    filtered_words = not_these_characters(words)

    return jsonify(filtered_words)


def not_these_characters(words=None):
    if words is None:
        return jsonify({"error": "No words provided"}), 400

    words = list(words)

    print(words)

    words_without_word = [
        word for word in word_list if all(char not in word for char in words)
    ]
    print(words_without_word[:10] if words_without_word else "No matching words")

    return words_without_word


app.debug = True
if __name__ == "__main__":
    app.run()
