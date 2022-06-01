from flask import Flask, redirect, url_for, render_template
from src.ipvc import iCITY, returno

app = Flask(__name__, template_folder='template')


@app.route('/')
def home():
    return render_template('index.html', city=iCITY, returno=returno)


if __name__ == '__main__':
    app.run(debug=True)
