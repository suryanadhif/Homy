from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS


app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": "*"}})

@app.route("/")
def home():
    return send_from_directory("views", "index.html")

@app.route("/api/data")
def get_data():
    return {
        "status": "success",
        "data": [
            {
                "id": 1,
                "name": "Rumah Minimalis"
            },
            {
                "id": 2,
                "name": "Rumah Modern"
            }
        ]
    }

@app.route("/views/<path:filename>")
def static_files(filename):
    return send_from_directory("views", filename)

if __name__ == "__main__":
    app.run(debug=True)