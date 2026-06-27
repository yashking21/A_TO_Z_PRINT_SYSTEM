from flask import Flask, render_template, request
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    file = request.files["file"]

    if file.filename != "":
        file.save(os.path.join(UPLOAD_FOLDER, file.filename))
        return "Upload successful!"

    return "No file selected"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)