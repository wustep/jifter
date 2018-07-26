import os
from flask import Flask, jsonify, request
from dotenv import load_dotenv
from pathlib import Path

import store
from questions import get_question
from gifts import get_recommendations

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/start')
def start():
    '''
    Starts a user's session and returns a question.
    '''
    data = request.get_json()
    session = data.get(session, 0)
    if session:
        result = store.create_user(session)
        return jsonify({question: questions.get_question()})
    else:
        abort(412)

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

@app.route('/send')
def send():
    '''
    Sends the user's list of recommendations to their text or email.
    '''
    return jsonify({})

@app.route('/end')
def end():
    '''
    Ends & deletes the user's session.
    '''
    return jsonify({})

if __name__ == '__main__':
    dotenv_path = Path(os.path.abspath(__file__)) / '../..' / '.env'
    load_dotenv(dotenv_path=dotenv_path)
    port = os.getenv("API_PORT")
    app.run(debug=True, port=int(port))
