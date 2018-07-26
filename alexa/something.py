from flask import Flask
from flask import render_template
from flask_ask import Ask, statement, qeustion

app = Flask(__name__)
ask = Ask(app, '/')

@ask.launch
def start_jifter_intent():
    welcome_msg = render_template(app_open)
    #start store for user
    return question(welcome_msg)


@ask.intent('AMAZON.NoIntent')
def pos_response():
    next_question = "Yes, Next question for user {}".format(user_id)
    return question(next_question)

@ask.intent('AMAZON.YesIntent')
def neg_response():

    next_question = "No, Next question for user {}".format(user_id)
    return question(next_question)

@ask.intent('MaybeIntent')
def maybe_response():
    next_question = "Maybe, next question for user {}".format(user_id)

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


def get_api_response(userAnswer):

    send_json = {response: userAnswer}

    res_json = {}
    return res_json



if __name__ == '__main__':
    app.run()
