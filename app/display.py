from flask_ask import context


display_round = dict(template="BodyTemplate1", title="Myth Quiz", backButton="HIDDEN")


def display_type():
    display_type = context.Viewport.shape
    return display_type
