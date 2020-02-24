from flask import Flask

app = Flask(__name__)

@app.route('/')         # 'www.stada.n;/flask' zou ook kunnen
def hello():
    return "Hello world"

if __name__ == "__name__":
    app.run(debug=True)