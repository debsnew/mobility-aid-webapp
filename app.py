# imports Flask
from flask import Flask

# creates Flask app
app = Flask(__name__)

# registered route to app
@app.route("/") 
def hello_world():
  return "Hello world"

# if running as python app.py then start the app
if __name__ == "__main__":
  app.run(host='0.0.0.0',debug=True)