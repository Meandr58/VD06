from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/quote')
def get_quote():
    try:
        response = requests.get('http://api.quotable.io/random')
        response.raise_for_status()  # Проверка на ошибки
        data = response.json()
        return jsonify({
            'content': data['content'],
            'author': data['author']
        })
    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
