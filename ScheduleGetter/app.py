from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)


@app.route('/')
def root_page():
    return render_template('index.html')

@app.route('/get_schedule_from_ion/<date>', methods=['GET'])
def get_schedule_from_ion_route(date=None):
    if date is None:
        return jsonify({"error": "No date provided"}), 400

    schedule = get_schedule_from_ion(date)
    print(f"Schedule for {date}: {schedule}")
    return jsonify(schedule)


def get_schedule_from_ion(date=None):

    url = f"https://ion.tjhsst.edu/api/schedule/{date}?format=json"
    response = requests.get(url)

    print(f"Requesting schedule from ION: {url}")
    if response.status_code != 200:
        print(f"Error fetching schedule: {response.status_code}")
        return {"error": "Failed to fetch schedule from ION"}

    return response.json()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)