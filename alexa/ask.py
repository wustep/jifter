from flask import Flask, render_template, logging
from flask_ask import Ask, statement, question, session

app = Flask(__name__)
ask = Ask(app, '/ask')
logging.getLogger('flask_ask').setLevel(logging.DEBUG)

@ask.launch
def start_jifter_intent():
    print("launched")
    #welcome_msg = render_template(app_open)
    return question("Test")

@ask.intent('AMAZON.FallbackIntent')
def fallback():
    return question("I did not understand that")

@ask.intent('PriceRangeIntent')
def price_range(min_price, max_price, currency):
    #speech_text = render_template(close_app)
    return question(str(max_price))

@ask.intent('PriceAroundIntent')
def price_range(price, currency):
    #speech_text = render_template(close_app)
    return question(str(price))

@ask.intent('YesIntent')
def pos_response():
    #response = get_api_response("no")
    return question("Yes works")

@ask.intent('NoIntent')
def neg_response():
    #response = get_api_response("yes")
    #logic about
    return question("No works")

@ask.intent('MaybeIntent')
def maybe_response():
    #response = get_api_response("maybe")
    return question("Maybe works")

@ask.intent('GetGiftsIntent')
def get_gift_list():
    # gift_score = 10;
    # gift_name = "Temp"
    #
    # if score > 66:
    #     speech_text = render_template(high_score_gift, gift_name)
    # elif score <= 66 and score >33:
    #     speech_text = render_template(med_score_gift, gift_name)
    # else:
    #     speech_text = render_template(low_score_gift, gift_name)

    return question("List of Gifts")

@ask.intent('FinishedIntent')
def finished_jifter():
    #speech_text = render_template(close_app)
    return statement("Finished")

@app.do_teardown_appcontext
def clear_user():
    return None

def get_api_response(userResponse):

    parameters = {"response": userResponse, "user_id": session.user.userId}
    response = requests.get(API_ENDPOINT, params=parameters)

    if response.status_code == 200:
        res_json = response.content
    else:
        res_json =  None

    return res_json

if __name__ == '__main__':
    print("Starting Alexa Skill")
    dotenv_path = Path(os.path.abspath(__file__)) / '../..' / '.env'
    load_dotenv(dotenv_path=dotenv_path)
    port = os.getenv("ALEXA_PORT")
    app.run(debug=True, port=int(port))
