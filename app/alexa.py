from flask_ask import statement, question
from flask_ask import session as ask_session, request as ask_request
from flask import render_template

from app import ask


@ask.launch
def set_up_skill():
    # output = render_template("welcome")
    # ask_session.attributes["last_speech"] = output
    return question("hmmm")


@ask.intent("getRak")
def get_rak():
    return question("what")
