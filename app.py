from flask import Flask, render_template, request, redirect,session
import os
import json

app = Flask(__name__)

app.secret_key="tajammulpatel2010"

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/")
def home():

    with open("stock.json", "r") as file:
        stock = json.load(file)

    return render_template("index.html", stock=stock)


@app.route("/admin", methods=["GET", "POST"])
def admin():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        if username == "TAJ" and password == "tajammulpatel2010":
            return redirect("/dashboard")

        return "Wrong Username or Password"

    return render_template("admin.html")


@app.route("/dashboard")
def dashboard():

    if not session.get("admin"):
        return redirect("/admin")
    
    return    
    return render_template("dashboard.html")


@app.route("/stock")
def stock():
    return render_template("stock.html")


@app.route("/upload", methods=["POST"])
def upload():

    file = request.files["file"]

    if file.filename != "":
        file.save(os.path.join(UPLOAD_FOLDER, file.filename))
        return "Upload successful!"

    return "No file selected"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)