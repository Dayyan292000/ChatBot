from flask import Flask, render_template, request, jsonify
import json
import urllib.parse

app = Flask(__name__)

def read_responses():
    with open("responses.json", "r") as file:
        responses = json.load(file)
    return responses

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get_response", methods=["POST"])
def get_response():
    user_message_encoded = request.get_data().decode("utf-8")[13:]
    user_message = urllib.parse.unquote(user_message_encoded)    
    user_message = user_message.strip()
    
    #Capitalise first letter
    user_message = user_message[0].upper() + user_message[1:]
    print(f"Received User Message: {user_message}")

    responses = read_responses()

    # Simple logic: find the first response that contains the user's message
    bot_response = responses.get(user_message, "Sorry, I don't understand.")

    return jsonify({"bot_response": bot_response})

if __name__ == "__main__":
    app.run(debug=True)
