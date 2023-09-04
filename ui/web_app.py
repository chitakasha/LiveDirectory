import os
import json
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    """The home page of the web app."""

    # Get the current state of the Live Directory
    with open("data/state.json", "r") as f:
        current_state = json.load(f)

    return render_template("index.html", current_state=current_state)

@app.route("/generate")
def generate():
    """The page that generates text based on the golden ratio."""

    # Get the prompts from the inbox
    with open("data/inbox/prompts.json", "r") as f:
        prompts = json.load(f)

    # Generate text based on the golden ratio
    generated_text = generate_text(prompts, current_state)

    # Update the current state
    current_state['last_generated_text'] = generated_text

    # Save the updated state back to the JSON file
    with open("data/state.json", "w") as f:
        json.dump(current_state, f, indent=4)

    return render_template("generate.html", generated_text=generated_text)

if __name__ == "__main__":
    app.run(debug=True)

