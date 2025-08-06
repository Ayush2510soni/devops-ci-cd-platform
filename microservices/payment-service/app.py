from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/payment")
def get_payment():
    return jsonify({"id": 101, "amount": 299.99, "status": "Success"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)

