from flask import Flask
existing_models = ['Beedle', 'Crossroads', 'M2', 'Panique']

app = Flask(__name__)

@app.route("/")
def hello():
    return "Welcome to Flatiron Cars"


@app.route("/<model>")
def models(model):
    # case-insensitive match against known models
    if any(model.lower() == m.lower() for m in existing_models):
        return f"Flatiron {model} is in our fleet!"
    else:
        return f"No models called {model} exists in our catalog"


if __name__ == "__main__":
    app.run(debug=True, port=5555)
