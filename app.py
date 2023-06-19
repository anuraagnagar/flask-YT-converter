from flask import Flask,  render_template, request, redirect, url_for, flash

import os

app = Flask(__name__, template_folder="templates", static_folder="static")

app.config["DEBUG"] = True
app.config["SECRET_KEY"] = os.environ["SECRET_KEY"]


@app.route("/", methods=["GET", "POST"])
@app.route("/home", methods=["GET", "POST"])
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(port=5500)
