from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/test")
def test():
    return "<p>Hello, Test!</p>"

if __name__ == '__main__':
    # L'application Flask est exécutée en mode débogage sur le port 5000
    app.run(host='0.0.0.0', port=5000, debug=True)
