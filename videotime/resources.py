from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/")
def hello():
    return "VideoMe!"

@app.route("/process")
def process_video():
    content = request.json
