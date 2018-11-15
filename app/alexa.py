from flask_ask import statement, question
from flask_ask import session as ask_session, request as ask_request
from flask import render_template
from random import choice

from app import ask
from app.display import display_type, display_format, display_round, display_rectangle
from app.mechanics import create_date_obj, display_date, get_rak_of, day_of_year
from app.data import christmas_calendar


@ask.launch
def set_up_skill():
    output = render_template("welcome")
    ask_session.attributes["last_speech"] = output
    if "DISPLAY_TYPE" not in ask_session.attributes:
        ask_session.attributes["DISPLAY_TYPE"] = display_type()

    _display_type = ask_session.attributes["DISPLAY_TYPE"]
    if _display_type == "NO_DISPLAY":
        return question(output)
    else:
        _display_format = display_format(_display_type)

        return question(output).display_render(
            **_display_format,
            text={"primaryText": {"type": "RichText", "text": "start"}},
        )


@ask.intent("getRak")
def get_rak(user_date):
    # convert date to date object
    user_date_obj = create_date_obj(user_date)
    # get display
    user_display = display_info(user_date_obj)
    _display_type = ask_session.attributes["DISPLAY_TYPE"]
    # _display_format = display_format(_display_type)
    _day_of_year = day_of_year(user_date)

    if 335 > int(_day_of_year):
        random_rak = choice(list(christmas_calendar))
        rak = f"Sorry its not christmas yet, but here's a sneak peak at the christmas calender. {christmas_calendar[random_rak]}"
    else:
        rak = get_rak_of(_day_of_year)

    if _display_type == "NO_DISPLAY":
        return statement(
            f"<speak><voice name='Salli'><prosody rate='90%'>{rak}</prosody></voice></speak>"
        )
    else:
        _display_format = display_format(_display_type)

    return statement(
        f"<speak><voice name='Salli'><prosody rate='90%'>{rak}</prosody></voice></speak>"
    ).display_render(
        **_display_format,
        text={
            "primaryText": {"type": "RichText", "text": user_display},
            "secondaryText": {"type": "RichText", "text": rak},
        },
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
