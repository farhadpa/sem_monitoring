from flask import Flask, request
from flask_cors import CORS
from threading import Thread
import time
import os
from send_request import send_request
from test_data import test_data


app = Flask(__name__)
cors = CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"
running = False # Flag to control the service
task_thread = None
# secret key to authorize the request. with a default value. this is not secure and should be changed
# the default value added later because the QPC environment variables were not loaded in the container.
secret_key = os.getenv("secret_key", "sample123456key")
# URL of the service to monitor
SERVICE_URL = "http://semproxy.40387376.qpc.hal.davecutting.uk/service"


def service():
    global running
    while running:
        for data in test_data:
            payload = data["payload"]
            result = data["result"]
            send_request(SERVICE_URL, payload, result)
        time.sleep(600)


@app.route("/start", methods=["POST"])
def start_monitoring():
    global running, task_thread, secret_key
    api_key = request.headers.get("Authorization")
    # check if the api key is correct and supplied in the request
    if secret_key != api_key or api_key == None :
        return "Not authorized"
    if not running:
        running = True
        task_thread = Thread(target=service)
        task_thread.start()
        return "Function started"
    return "Function is already running"


@app.route("/stop", methods=["POST"])
def stop_function():
    global running, task_thread, secret_key
    # check if the api key is correct and supplied in the request
    api_key = request.headers.get("Authorization")
    if secret_key != api_key or api_key == None:
        return "Not authorized"
    if running:
        running = False
        task_thread.join()
        return "function stoped"
    return "function is not running"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
