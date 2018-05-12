from flask import Flask
from flask import jsonify
from flask import request
from flask import render_template
from sentiment_analyzer import analyzer

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("hello.html")


@app.route("/api/")
def api():
    input_text = request.args.get("text")

    if input_text is None:
        return jsonify(error="Empty Argument", results={})
    else:
        input_text = input_text.replace("\"", "")
        return jsonify(
            input=input_text,
            results=analyzer.sentiment_analyzer(input_text)
        )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)