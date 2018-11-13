from flask_ask import statement, question
from flask_ask import session as ask_session, request as ask_request
from flask import render_template

from app import ask
from app.display import display_type, display_round
from app.mechanics import create_date_obj, display_date


@ask.launch
def set_up_skill():
    output = render_template("welcome")
    ask_session.attributes["last_speech"] = output
    if "DISPLAY_TYPE" not in ask_session.attributes:
        ask_session.attributes["DISPLAY_TYPE"] = display_type()
    print(ask_session.attributes["DISPLAY_TYPE"])
    text2 = ask_session.attributes["DISPLAY_TYPE"]
    return question(output).display_render(
        **display_round, text={"primaryText": {"type": "RichText", "text": text2}}
    )


@ask.intent("getRak")
def get_rak(user_date):
    # convert date to date object
    user_date_obj = create_date_obj(user_date)
    # get display
    user_display = display_info(user_date_obj)
    return question("what").display_render(
        **display_round,
        text={"primaryText": {"type": "RichText", "text": user_display}},
    )


@ask.intent("AMAZON.FallbackIntent")
def fallback():
    output = render_template("error")
    ask_session.attributes["last_speech"] = output
    return question(output)


@ask.intent("AMAZON.RepeatIntent")
def repeat():
    repeat_speech = ask_session.attributes["last_speech"]
    return question(repeat_speech)


@ask.intent("AMAZON.HelpIntent")
def help():
    output = render_template("help")
    ask_session.attributes["last_speech"] = output
    return question(output)


@ask.intent("AMAZON.CancelIntent")
@ask.intent("AMAZON.StopIntent")
@ask.intent("AMAZON.NoIntent")
def goodbye():
    return statement("Good bye")


@ask.session_ended
def session_ended():
    return "{}", 200


def display_info(user_date_obj):
    user_display = display_date(user_date_obj)
    return user_display
