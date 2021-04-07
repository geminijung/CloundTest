from flask import Flask
server = Flask(__name__)

@server.route("/")
def hello():
    return "Hello วรพล วรรณพุฒ 6006021613103 from Servers"

if __name__ == "__main__":
    server.run(host='0.0.0.0', port=80)