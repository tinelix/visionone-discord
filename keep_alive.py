from flask import Flask
from flask import request
from flask import session
from flask import url_for
from threading import Thread

import os
from dotenv import load_dotenv
dotenv_path = os.path.join(os.path.dirname(__file__), '.secret')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

app = Flask('')

@app.route('/')
def main():
    return "Your bot is alive!"


def run():
    app.run(host="0.0.0.0", port=8080)

def keep_alive():
    server = Thread(target=run)
    server.start()
