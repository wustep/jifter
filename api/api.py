import os
from flask import Flask, jsonify, request, abort
from dotenv import load_dotenv
from pathlib import Path

import store
from questions import get_question, get_last_question
from gifts import get_recommendations

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/start', methods=["POST"])
def start():
    '''
    Starts a user's session and returns a question.
    '''
    data = request.get_json()
    session = data.get("session", 0)
    if session:
        result = store.create_user(session)
        question = get_question()
        store.add_question(question)
        return jsonify({"question": question, "products": []})
    else:
        abort(412)

@app.route('/price', methods=["POST"])
def price():
    '''
    Sets a user's price range.
    '''
    data = request.get_json()
    session = data.get("session", 0)
    price = data.get("price", {})
    if session:
        price_set = {}
        if price and "min" in price:
            price_set["min"] = int(price["min"])
        if price and "max" in price:
            price_set["max"] = int(price["max"])
        if store.set_price(session, price_set):
            result = {"success": True}
            result["price"] = price
            return jsonify(result)
    abort(412)

@app.route('/answer', methods=["POST"])
def answer():
    '''
    Answers a user's question and returns a new question, their
    current list of recommendations (capped at 10), and whether
    there are more questions left.
    '''
    data = request.get_json()
    session = data.get("session", 0)
    response = data.get("response", 0)
    if session and response:
        if answer_question(session, response):
            question = get_question(session)
            store.add_question(session, question)
            return jsonify({"question": question, "products": []})
    return jsonify(question)

@app.route('/send', methods=["POST"])
def send():
    '''
    Sends the user's list of recommendations to their text or email.
    '''
    return jsonify({})

@app.route('/end', methods=["POST"])
def end():
    '''
    Deletes a user session if it exists.
    Reports success regardless of whether user exists, as long as it is provided.
    '''
    data = request.get_json()
    session = data.get("session", 0)
    if session:
        delete_user(session)
        return jsonify({"success": True})
    abort(412)

if __name__ == '__main__':
    dotenv_path = Path(os.path.abspath(__file__)) / '../..' / '.env'
    load_dotenv(dotenv_path=dotenv_path)
    port = os.getenv("API_PORT")
    app.run(debug=True, port=int(port))
