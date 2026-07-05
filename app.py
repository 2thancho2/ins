from flask import Flask, request

app = Flask(__name__)

VERIFY_TOKEN = "iamthebest"

@app.route("/webhook", methods=["GET"])
def verify():
    print("===== ALL ARGS =====")
    print(request.args)
    print("====================")

    mode = request.args.get("hub.mode")
    token = request.args.get("hub.verify_token")
    challenge = request.args.get("hub.challenge")

    print("mode =", repr(mode))
    print("token =", repr(token))
    print("challenge =", repr(challenge))
    print("verify_token =", repr(VERIFY_TOKEN))

    if mode == "subscribe" and token == VERIFY_TOKEN:
        print("SUCCESS")
        return challenge, 200

    print("FAILED")
    return "Forbidden", 403

@app.route("/webhook", methods=["POST"])
def webhook():
    print(request.json)
    return "EVENT_RECEIVED", 200

app.run(port=5000)