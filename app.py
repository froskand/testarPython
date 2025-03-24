from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Cloud! This is a simple deployment test."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
