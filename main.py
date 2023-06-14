from flask import Flask
app = Flask(__name__)
@app.route('/hello/', methods=['GET', 'POST'])
def welcome():
    return "Welcome to MS class!"
@app.route('/joke/', methods=['GET', 'POST'])
def joke():
    return "Hello World 2!"
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
