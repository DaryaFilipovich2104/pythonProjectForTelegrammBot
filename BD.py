# import sqlite3
#
# conn = sqlite3.connect('Bot_movies.db')
# cursor = conn.cursor()
# cursor.execute(
#     '''CREATE TABLE IF NOT EXISTS movies (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, genre TEXT, description TEXT, link TEXT)''')
#
# while True:
#     def insert_movies(genre, name, description):
#         name = input('Введите название фильма: ')
#         genre = input('Введите жанр фильма: ')
#         description = input('Введите описание фильма: ')
#         conn.execute(''' INSERT INTO movies (name, description) VALUES(?, ?, ?) ''', (name, genre, description))
#         # conn.commit()
#
#
#     def show_for_genre(id_genre):
#         id_genre = input('Введите жанр фильма: ')
#         cursor.execute('''SELECT name, description, link from movies WHERE genre=?''', id_genre)
#         k = cursor.fetchall()
#         print(k)
