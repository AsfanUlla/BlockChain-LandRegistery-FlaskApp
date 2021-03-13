from flask import Flask, render_template, request
from views import GetRecords, ServeRecords

app = Flask(__name__)


def build_app():
    app.add_url_rule(
        "/",
        view_func=GetRecords.as_view("all-records")
    )

    app.add_url_rule(
        "/records/",
        view_func=ServeRecords.as_view("serve-records")
    )

    return app

