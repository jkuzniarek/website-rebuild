from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "Hello World!"

@app.route('/hello2')
def hello2():
    return "Good Bye, Cruel World!"

@app.route('/post/<postid>')
def post(postid):
    return "Hello " + postid

app.debug = True
if __name__ == '__main__':
    app.run()
