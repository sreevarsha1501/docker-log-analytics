from flask import Flask
import logging

app = Flask(__name__)

logging.basicConfig(
    filename='/logs/app.log',
    level=logging.INFO
)

@app.route("/")
def home():

    logging.info("User visited Home Page")

    return "Docker Log Analytics Running"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
