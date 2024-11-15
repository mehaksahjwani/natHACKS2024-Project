from flask import Flask 

app = Flask(__name__)

@app.route("/fatigue")
def fatigue():
    return "the person is tired"

if __name__ == "__main__":
    app.run(debug=True)