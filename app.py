from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Dev web block'


if __name__ == '__main__':
    app.run()