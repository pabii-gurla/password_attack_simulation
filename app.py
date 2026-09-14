from flask import Flask, request
import time

app = Flask(__name__)

CORRECT_USERNAME = "admin"
CORRECT_PASSWORD = "letmein"

MAX_ATTEMPTS = 3
BLOCK_TIME = 30

attempts = {}

@app.route("/login", methods=["POST"])
def login():
    client_ip = request.remote_addr
    current_time = time.time()

    if client_ip not in attempts:
        attempts[client_ip] = {
            "count":0,
            "blocked_until": 0
        }

    user = attempts[client_ip]

    if current_time < user["blocked_until"]:
        return "Too mant login attempts. Try again later.", 429

    username = request.form.get("username")
    password = request.form.get("password")

    if username == CORRECT_USERNAME and password == CORRECT_PASSWORD:
        user["count"] = 0
        return "Welcome! Login Successful."

    user["count"] += 1

    if user["count"]>= MAX_ATTEMPTS:
        user["blocked_until"] = current_time + BLOCK_TIME
        user["count"] = 0

    return "Too many login attempts. Try again later.", 429

    return "Invalid username or password", 401

if __name__ == "__main__":
    app.run()
