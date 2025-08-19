from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, Flask Todo App!'

@app.route('/api')
def api():
    return jsonify({'message': 'This is API response'})

if __name__ == '__main__':
    app.run(debug=True)
