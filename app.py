from flask import Flask, render_template, request
from sql_scripts import *

app = Flask(__name__)  # Створюємо веб–додаток Flask
@app.route("/")  # Вказуємо url-адресу для виклику функції
def index():
    articles = get_all_articles()
    return render_template("index.html", articles=articles)  # html-сторінка, що повертається у браузер
@app.context_processor
def get_context():
    genres = get_all_genres()
    return {'genres': genres}  

@app.route("/search")  # Вказуємо url-адресу для виклику функції
def search():
    query = request.args.get('query', '')  # Отримуємо параметр з url-адреси
    articles = search_articles(query)
    return render_template("search.html", articles=articles)  # html-сторінка, що повертається у браузер


@app.route("/genre/<int:genre_id>")  # Вказуємо url-адресу для виклику функції
def genre_page(genre_id):
    articles = get_articles_genre(genre_id)
    return render_template("genre_page.html", articles=articles)  # html-сторінка, що повертається у браузер


@app.route('/article/<int:article_id>')
def article_page(article_id):
    article = get_article(article_id)
    return render_template("article_page.html", article=article)



if __name__ == "__main__":
    app.config['TEMPLATES_AUTO_RELOAD'] = True  # автоматичне оновлення шаблонів
    app.run(debug=True)  # Запускаємо веб-сервер з цього файлу в режимі налагодження

