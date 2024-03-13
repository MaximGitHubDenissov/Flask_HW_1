from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def index():
    context = {'title': 'Шаблон',
               'header': 'Это шаблон'
               }
    return render_template('index.html', **context)


@app.route('/main/')
def main():
    context = {'title': 'Главная страница',
               'header': 'Интернет магазин одежды'}
    return render_template('main.html', **context)


@app.route('/clothes/')
def clothes():
    context = {'title': 'Одежда',
               'header': 'Одежда'
               }
    return render_template('clothes.html', **context)


@app.route('/jacket/')
def jacket():
    context = {'title': 'Куртка',
               'header': 'Куртка'
               }
    return render_template('jacket.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
