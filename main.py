from flask import Flask, render_template, request
import json

app = Flask(__name__)

# Load the vocabulary once at startup
with open('vocab.json', 'r') as f:
    blockchain_dict = json.load(f)

@app.route('/', methods=['GET'])
def index():
    # Sort terms alphabetically for display
    sorted_terms = sorted(blockchain_dict.items())
    return render_template('index.html', dictionary=sorted_terms)

if __name__ == '__main__':
    app.run(debug=True)
