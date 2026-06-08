from flask import Flask
from flask_cors import CORS

app = Flask(__name__)

CORS(
    app,
    resources={
        r"/*": {
            "origins": "http://localhost:3000"
        }
    }
)

@app.route("/")
def home():
    return {
        "message": "Homy Backend Server Running"
    }

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

if __name__ == "__main__":
    app.run(debug=True)