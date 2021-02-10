import sqlite3


def create_db():
    #Создаем базу ссылок сайта
    db = sqlite3.connect('url_from_search.db')
    cur = db.cursor() 
    #Добавляем в БД столбцы
    cur.execute("""
                CREATE TABLE IF NOT EXISTS url_from_search ( 
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    Title TEXT,
                    Url TEXT
                    )""")


def add_db(html, title): # добавление ссылки в базу данных
    db = sqlite3.connect('url_from_search.db')
    cur = db.cursor() 
    #print('add db - ' + html)
    cur.execute(f"INSERT INTO url_from_search (Title, Url) VALUES (?, ?)", (title, html))
    db.commit()



