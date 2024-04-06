# peizashi marsa
from flask import Flask, url_for, request, render_template

app = Flask(__name__)


@app.route('/')
def f():
    return "<title>hello</title><h1>Миссия Колонизация Марса<h1>"


@app.route('/test_carousel')
def return_carousel():
    pics = [(f"{url_for('static', filename='img/1.jpeg')}", "first"),
                        (f"{url_for('static', filename='img/2.jpeg')}", "second"),
                        (f"{url_for('static', filename='img/3.jpeg')}", "third")
                        ]
    return render_template('test_carousel.html', title='Карусель', pics=pics)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
