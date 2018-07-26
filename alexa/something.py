from flask import Flask
from flask import render_template
from flask_ask import Ask, statement, qeustion, session

app = Flask(__name__)
ask = Ask(app, '/')


@ask.launch
def start_jifter_intent():
    welcome_msg = render_template(app_open)
    #TODO: start store for user
    return question(welcome_msg)


@ask.intent('AMAZON.NoIntent')
def pos_response():
    response = get_api_response("no")
    return question(next_question)

@ask.intent('AMAZON.YesIntent')
def neg_response():
    response = get_api_response("yes")
    #logic about
    return question(next_question)

@ask.intent('MaybeIntent')
def maybe_response():
    response = get_api_response("maybe")

@ask.intent('GetGiftsIntent')
def get_gift_list():
    gift_score = 10;
    gift_name = "Temp"

    if score > 66:
        speech_text = render_template(high_score_gift, gift_name)
    elif score <= 66 and score >33:
        speech_text = render_template(med_score_gift, gift_name)
    else:
        speech_text = render_template(low_score_gift, gift_name)

    return statement(speech_text)

@ask.intent('FinishedIntent')
def finished_jifter():
    speech_text = render_template(close_app)
    return statement(speech_text)

@do_teardown_appcontext
def clear_user():
    #destroy user

def get_api_response(userResponse):

    parameters = {"response": userResponse, "user_id": session.user.userId}
    response = requests.get(API_ENDPOINT, params=parameters)

    if response.status_code == 200:
        res_json = response.content
    else:
        res_json =  None

    return res_json


if __name__ == '__main__':
    app.run()
