from flask import Flask, render_template, request, jsonify
app = Flask(__name__)
count = 0
@app.route('/template')
def hello_world():
    # count += 1
    return render_template('index.html', count=0)

@app.route('/store-data', methods=['POST'])
def store_data():
    data = request.json
    # Process the data as needed
    print( "Data received:", data)
    return jsonify({"message": "Data received", "data": data})

app.debug=True
if __name__ == '__main__':
    app.run()