from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0", port='5000')


@app.route('/')
def home():
    return 'Hello World!'