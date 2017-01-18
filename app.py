from flask import Flask, request, make_response

app = Flask('tcguaruja')
app = Flask(__name__.split('.')[0])

@app.route('/')
def root():
    return 'Olá mundo'


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)