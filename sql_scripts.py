import sqlite3

def get_all_articles():
    conn = sqlite3.connect('blog.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM articles')
    articles = cursor.fetchall()
    conn.close()
    
    return articles

def get_all_genres():
    conn = sqlite3.connect('blog.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM categories')
    categories = cursor.fetchall()
    conn.close()
    
    return categories

def get_article(article_id):
    conn = sqlite3.connect('blog.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM articles WHERE id=?', [article_id] )
    articles = cursor.fetchone()
    conn.close()
    
    return articles


def get_articles_genre(category_id):
    conn = sqlite3.connect('blog.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM articles WHERE category_id=?', [category_id] )
    articles = cursor.fetchall()
    conn.close()
    
    return articles


def search_articles(search_query):
    conn = sqlite3.connect('blog.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM articles WHERE title LIKE ? ', ['%' + search_query + '%'])
    articles = cursor.fetchall()
    conn.close()
    
    return articles
