from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

@app.route('/')
def index():
    with open('vocab.json', 'r') as file:
        data = json.load(file)
    return render_template('index.html', glossary=data)

@app.route('/api/glossary')
def api_glossary():
    with open('vocab.json', 'r') as file:
        data = json.load(file)
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
