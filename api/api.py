from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/start')
def start():
    '''
    Starts a user's session and returns a question.
    '''
    return jsonify({})

@app.route('/answer')
def answer():
    '''
    Answers a user's question and returns a new question, their
    current list of recommendations (capped at 10), and whether
    there are more questions left.
    '''
    return jsonify({})

@app.route('/undo')
def undo():
    '''
    Undos the user's response to the last question, returning
    the question again with their current list of recommendations.
    '''
    return jsonify({})

@app.route('/end')
def end():
    '''
    Ends & deletes the user's session.
    '''
    return jsonify({})

if __name__ == '__main__':
    app.run(debug=True)
