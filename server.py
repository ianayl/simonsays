from flask import Flask, request, render_template, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

with app.test_request_context():
    print(url_for("static", filename="styles.css"))


@app.route("/home1", methods=["GET", "POST"])
def home1():
    name = None
    if request.method == "POST":
        name = request.form.get("task")
    return render_template("home1.html", name=name)

@app.route("/simonsays/")
def simonsays():
    return render_template("simonsays.html")

with app.test_request_context():
    print(url_for("static", filename="simonsays.css"))


if __name__ == "__main__":
    app.run(debug=True)
