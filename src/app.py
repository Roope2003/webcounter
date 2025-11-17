from flask import Flask, redirect, render_template, request
from counter import Counter

app = Flask(__name__)
cnt = Counter()

@app.route("/")
def index():
    return render_template("index.html", value=cnt.value)

@app.route("/increment", methods=["POST"])
def increment():
    cnt.increase()
    return redirect("/")
@app.route("/reset", methods=["POST"])
def reset():
    cnt.reset()
    return redirect("/")

@app.route("/set", methods=["POST"])
def set_counter():
    value = request.form.get("value")
    if value is None:
        json_body = request.get_json(silent=True)
        value = json_body.get("value") if json_body else None

    if value is None:
        return "Missing 'value' in request", 400

    try:
        value = int(value)
    except (TypeError, ValueError):
        return "Invalid value; expected integer", 400
    cnt.set_value(value)
    return redirect("/")