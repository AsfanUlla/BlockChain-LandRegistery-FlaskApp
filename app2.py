from flask import Flask, render_template, request
from views import GetRecords, ServeRecords, SignUp, Login
from flask_cors import CORS

app = Flask(__name__)

origins = ["http://18.191.238.75"]

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

    return app

