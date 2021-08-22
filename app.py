from flask import Flask, render_template, request
from views import GetRecords, ServeRecords, SignUp, Login, BulkUpdate
from flask_cors import CORS

app = Flask(__name__)

origins = ["http://18.191.238.75", "http://127.0.0.1", "http://127.0.0.1:5000", "http://localhost", "http://localhost:5000"]

CORS(app,
    origins=origins)


def build_app():
    app.add_url_rule(
        "/",
        view_func=GetRecords.as_view("all-records")
    )

    app.add_url_rule(
        "/records/",
        view_func=ServeRecords.as_view("serve-records")
    )

    app.add_url_rule(
        "/signup/",
        view_func=SignUp.as_view("signup")
    )

    app.add_url_rule(
        "/login/",
        view_func=Login.as_view("login")
    )

    app.add_url_rule(
        "/bulk_update/",
        view_func=BulkUpdate.as_view("bulk-update")
    )

    return app

