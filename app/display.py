from flask_ask import context
from app.mechanics import display_date


display_round = dict(
    template="BodyTemplate1", title="Random Acts of Kindness", backButton="HIDDEN"
)
display_rectangle = dict(
    template="BodyTemplate6",
    title="Random Acts of Kindness - Christmas edition",
    backButton="HIDDEN",
)


display_format_dict = {
    "type": {
        "ROUND": {
            "template": "BodyTemplate1",
            "title": "Random Acts of Kindness",
            "backButton": "HIDDEN",
        },
        "RECTANGLE": {
            "template": "BodyTemplate2",
            "title": "Random Acts of Kindness - Christmas edition",
            "backButton": "HIDDEN",
        },
    }
}


def display_type():
    if "Viewport" not in context:
        display_type = "NO_DISPLAY"
    else:
        display_type = context.Viewport.shape
    return display_type


def display_format(display_type):
    return display_format_dict["type"][display_type]


def display_info(user_date_obj):
    user_display = display_date(user_date_obj)
    return user_display
