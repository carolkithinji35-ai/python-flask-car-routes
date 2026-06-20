from flask import Flask
existing_models = ['Beedle', 'Crossroads', 'M2', 'Panique']


app = Flask(__name__)


@app.route("/")
def hello():
    return "<h1>Welcome to Flatiron Cars</h1>"


@app.route("/<model>")
def models(model):
    for existing_model in existing_models:
        if model.lower() in existing_models:
            return f"Flatiron {model} is in our fleet!"
        else:
            return f"No model called {model} exists in our catalog"

if __name__ == "__main__":
    app.run(debug=True, port=5555)