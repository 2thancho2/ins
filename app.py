from flask import Flask, request
import os
import json

app = Flask(__name__)

VERIFY_TOKEN = "iamthebest"


@app.route("/")
def home():
    return "Instagram Bot Server Running!"


@app.route("/webhook", methods=["GET"])
def verify():
    mode = request.args.get("hub.mode")
    token = request.args.get("hub.verify_token")
    challenge = request.args.get("hub.challenge")

    if mode == "subscribe" and token == VERIFY_TOKEN:
        print("✅ Webhook 인증 성공")
        return challenge, 200

    return "Forbidden", 403


@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()

    print("========== EVENT ==========")
    print(json.dumps(data, indent=4, ensure_ascii=False))
    print("===========================")

    return "EVENT_RECEIVED", 200


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000))
    )
