from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    # The uploaded project contains the Arsha page customized for Olympic Analytics.
    return render_template("index_flask_ready.html")


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


@app.route("/story")
def story():
    return render_template("story.html")


if __name__ == "__main__":
    app.run(debug=True)
