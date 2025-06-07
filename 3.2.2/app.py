from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route('/template')
def hello_world():
    racoonFacts=["Raccoons are nocturnal animals.", "Raccoons are omnivores.", "Raccoons are carnivores.", "Raccoons have a highly developed sense of touch.", "Raccoons are known for their dexterous front paws.", "Raccoons can rotate their hind feet 180 degrees."]
    return render_template('index.html', racoonFacts=racoonFacts[random.randint(0, len(racoonFacts)-1)])

app.debug=True
if __name__ == '__main__':
    app.run()