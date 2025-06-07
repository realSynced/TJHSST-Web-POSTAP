from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# 0 is gray
# 1 is yellow
# 2 is green

# /getwords/?color=0&char=a
word_list = open("../supplemental/enable1.txt").read().splitlines()


getwords_data = {
    "word": "",
    "colors": [],
}


def interpret_color(color: int):
    if color == 0:
        return False
    elif color == 1:
        return "Maybe"
    elif color == 2:
        return True


def getRule():
    print("Fetching rule from getwords_backend...")
    response = requests.get("http://127.0.0.1:5000/getwords_backend")
    print("Response from getwords_backend:", response.json())
    return response.json()


def filter_words():
    wordle = getRule()
    wordle_word = wordle["word"]
    colors = wordle["colors"]

    interpreted_colors = []
    index_of_true = []
    index_of_false = []
    index_of_maybe = []

    cutdown_list = [word for word in word_list if len(word) == 5]

    for i in colors:
        interpreted_colors.append(interpret_color(i))

    print("Interpreted colors:", interpreted_colors)

    for i, color in enumerate(interpreted_colors):
        if color is True:
            index_of_true.append(i)
        elif color is False:
            index_of_false.append(i)
        elif color == "Maybe":
            index_of_maybe.append(i)

    print("Index of True (green):", index_of_true)
    print("Index of False (gray):", index_of_false)
    print("Index of Maybe (yellow):", index_of_maybe)

    # Green letters: Character is at the correct position in the word
    for j in index_of_true:
        cutdown_list = [word for word in cutdown_list if word[j] == wordle_word[j]]

    print("After filtering for green letters:", cutdown_list[:10])

    # Gray letters: Character is not in the word at all
    for j in index_of_false:
        cutdown_list = [word for word in cutdown_list if wordle_word[j] not in word]

    print("After filtering for gray letters:", cutdown_list[:10])

    # Yellow letters: Character is in the word but not at the right position
    for j in index_of_maybe:
        cutdown_list = [
            word
            for word in cutdown_list
            if (wordle_word[j] in word and word[j] != wordle_word[j])
        ]

    print("After filtering for yellow letters:", cutdown_list[:10])

    # requests.post(
    #     "http://127.0.0.1:5000/getwords_filtered", json={"filtered_words": cutdown_list}
    # )

    return cutdown_list


@app.route("/getwords")
def index():
    # print("Accessing /getwords endpoint")
    # # Call the filter_words function to get the filtered list
    # filtered_words = filter_words()
    # print("Filtered words:", filtered_words)

    return render_template("index.html")


@app.route("/getwords_backend", methods=["GET", "POST"])
def getwords():

    if request.method == "POST":
        print("Received POST request")
        data = request.json
        print("Received JSON data:", data)
        getwords_data["word"] = data.get("word", "")
        getwords_data["colors"] = data.get("colors", [])
        print("Data after processing:", getwords_data)
        filtered_words = filter_words()
        print("Filtered words:", filtered_words)
        return jsonify({"filtered_words": filtered_words})

    return jsonify(getwords_data)


@app.route("/getwords_filtered", methods=["GET", "POST"])
def getwords_filtered():
    print("Accessing /getwords_filtered endpoint")
    # if request.method == "POST":
    #     print("Received POST request")
    #     data = request.json
    #     print("Received JSON data:", data)
    #     return jsonify({"filtered_words": data})

    return jsonify({"filtered_words": filter_words()})


if __name__ == "__main__":
    app.run(debug=True)
