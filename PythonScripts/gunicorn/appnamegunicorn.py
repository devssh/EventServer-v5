

from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
debug=False
app.debug=debug
path_prefix="/"
port = 8010

CORS(app)

@app.route("/")
def home_page():
  return "Hello World! - App Name Gunicorn"


if __name__ == "__main__":
  print("Running on port " + str(port))
  app.run(port=port, debug=debug)

