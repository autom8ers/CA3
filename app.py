from flask import Flask, jsonify
from calculator import Calculator  

app = Flask(__name__)
calculator = Calculator()

@app.route('/calc/add/<int:x>/<int:y>')
def add(x, y):
    result = calculator.add(x, y)
    return jsonify({'operation': 'add', 'result': result})

@app.route('/calc/multi/<int:x>/<int:y>')
def multi(x, y):
    result = calculator.multi(x, y)
    return jsonify({'operation': 'multi', 'result': result})


if __name__ == '__main__':
    app.run(debug=True, port=5000)
