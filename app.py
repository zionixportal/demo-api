from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/demo")
def demo():
    return jsonify({
        "message": "api stoped by @zioniiix\nFor paid api's contact @frappeash (encore ), @zioniiix (zionix)"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
