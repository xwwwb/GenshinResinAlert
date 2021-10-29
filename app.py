from flask import Flask, request
from getInfo.main import main
import json

app = Flask(__name__)

path = "./config.json"
with open(path, 'r+') as f:
    json_data = json.load(f)


@app.route('/api', methods=['GET', 'POST'])
def hello_world():  # put application's code here
    if request.method == 'GET':
        password = request.args.get("password")
        if password == json_data.get("password"):
            return main()
        else:
            return "你的访问密码不正确"


if __name__ == '__main__':
    app.run()
