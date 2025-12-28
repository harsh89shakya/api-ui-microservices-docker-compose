from flask import Flask, jsonify
app = Flask(__name__)
@app.route("/api-services")
def hello_api():
    return jsonify({
        "message": "Hello from API Service"
    })
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)